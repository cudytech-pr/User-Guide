
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cudy Modular Manual PDF Exporter

Features:
1. Extract hierarchical Contents from the product index page.
2. Preserve original DOM order and heading hierarchy.
3. Exclude More Details and navigation links.
4. Render each chapter independently using Chromium.
5. Generate compact Contents with dotted leaders and page numbers.
6. Extract original Cudy Logo from the website.
7. Extract Front Panel image from the Overview page.
8. Generate a minimalist product cover.
9. Add hierarchical PDF bookmarks.
10. Add model name + Cudy Logo to body page headers.
11. Add continuous page numbers to body pages only.

Install:
    python -m pip install playwright pypdf reportlab pillow
    python -m playwright install chromium

Run:
    python export_manual.py --url "https://docs.cudy.com/user_guide/wireless_router/wr3600_h/" --output "WR3600_H_User_Guide.pdf"

Keep temporary files:
    python export_manual.py --url "https://docs.cudy.com/user_guide/wireless_router/wr3600_h/" --output "WR3600_H_User_Guide.pdf" --keep-temp
"""

from __future__ import annotations

import argparse
import asyncio
import re
import shutil
import sys

from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag

from PIL import Image

from playwright.async_api import (
    async_playwright,
    TimeoutError as PlaywrightTimeoutError,
)

from pypdf import PdfReader, PdfWriter

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Flowable,
)


# ==================================================
# Configuration
# ==================================================

PAGE_MARGIN = {
    "top": "18mm",
    "right": "14mm",
    "bottom": "18mm",
    "left": "14mm",
}

EXCLUDED_TITLES = {
    "more details",
    "back",
    "previous",
    "next",
    "home",
}

ASSET_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg",
    ".webp", ".ico", ".css", ".js", ".json",
    ".xml", ".zip", ".pdf", ".mp4", ".mp3",
    ".woff", ".woff2", ".ttf", ".eot",
}

FRONT_PANEL_PATTERN = re.compile(
    r"front[\s_-]*panel",
    re.IGNORECASE,
)

LOGO_PATTERN = re.compile(
    r"cudyicon\.webp",
    re.IGNORECASE,
)

BRAND_COLOR = "#008CFF"

# Body header
HEADER_LOGO_WIDTH = 18 * mm
HEADER_LOGO_HEIGHT = 7 * mm
HEADER_LEFT_MARGIN = 14 * mm
HEADER_RIGHT_MARGIN = 14 * mm
HEADER_TOP_MARGIN = 6 * mm
HEADER_LINE_COLOR = "#DDDDDD"

# Body footer
FOOTER_BOTTOM_MARGIN = 6 * mm

# Cover
COVER_LOGO_MAX_WIDTH = 20 * mm
COVER_LOGO_MAX_HEIGHT = 20 * mm

COVER_IMAGE_MAX_WIDTH = 165 * mm
COVER_IMAGE_MAX_HEIGHT = 105 * mm

# Contents
CONTENTS_LEFT_MARGIN = 20 * mm
CONTENTS_RIGHT_MARGIN = 20 * mm
CONTENTS_TITLE_FONT_SIZE = 21
CONTENTS_FONT_SIZE = 9.5
CONTENTS_LINE_HEIGHT = 12
CONTENTS_INDENT = 5 * mm


# ==================================================
# Data models
# ==================================================

@dataclass
class Chapter:
    title: str
    url: str


@dataclass
class TocNode:
    title: str
    level: int
    url: str | None = None
    children: list[TocNode] = field(default_factory=list)


# ==================================================
# General helpers
# ==================================================

def clean_title(text: str) -> str:
    return re.sub(
        r"\s+",
        " ",
        (text or "").replace("¶", "")
    ).strip()


def normalize_url(url: str) -> str:
    """Remove fragments and normalize URL paths."""

    url, _ = urldefrag(url)
    parsed = urlparse(url)

    path = re.sub(r"/+", "/", parsed.path)

    if path != "/" and not Path(path).suffix:
        path = path.rstrip("/") + "/"

    return parsed._replace(path=path).geturl()


def is_asset_url(url: str) -> bool:
    return Path(urlparse(url).path).suffix.lower() in ASSET_EXTENSIONS


def is_excluded_title(title: str) -> bool:
    title = clean_title(title).lower()

    return (
        title in EXCLUDED_TITLES
        or title.startswith("more details")
        or title.startswith("back to ")
    )


def escape_xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def walk_tree(nodes: list[TocNode]):
    """Walk the tree in original DOM order."""

    for node in nodes:
        yield node
        yield from walk_tree(node.children)

def collect_fragment_targets(
    nodes: list[TocNode],
) -> dict[str, list[str]]:
    """
    Collect internal HTML heading fragments by chapter URL.
    """

    targets = {}

    for node in walk_tree(nodes):

        if not node.url:
            continue

        base_url, fragment = urldefrag(node.url)

        if not fragment:
            continue

        base_url = normalize_url(base_url)

        targets.setdefault(base_url, [])

        if fragment not in targets[base_url]:
            targets[base_url].append(fragment)

    return targets

def first_page_index_in_subtree(
    node: TocNode,
    page_map: dict[str, int],
) -> int | None:
    """
    Resolve the page of the current node.

    A node with its own URL must use its own page.
    Only structural nodes without URLs inherit the first
    available page from their descendants.
    """

    if node.url:
        return page_map.get(node.url)

    for child in node.children:
        result = first_page_index_in_subtree(child, page_map)

        if result is not None:
            return result

    return None


def get_page_map(
    chapters: list[Chapter],
    page_counts: list[int],
    body_start_index: int,
    fragment_page_maps: list[dict[str, int]] | None = None,
) -> dict[str, int]:
    """
    Map chapter URLs to absolute, zero-based PDF page indexes.

    Each chapter starts immediately after the previous chapter.
    """

    if len(chapters) != len(page_counts):
        raise ValueError("Chapter and page count mismatch.")

    page_map = {}
    current_page = body_start_index
    fragment_page_maps = fragment_page_maps or [{} for _ in chapters]

    if len(fragment_page_maps) != len(chapters):
        raise ValueError("Chapter and fragment page map count mismatch.")

    for chapter, count, fragment_pages in zip(
        chapters, page_counts, fragment_page_maps
    ):

        if count < 1:
            raise ValueError(
                f"Invalid page count for chapter: {chapter.title}"
            )

        page_map[chapter.url] = current_page

        # Internal heading destinations are relative to the chapter PDF.
        for fragment, local_page_index in fragment_pages.items():
            page_map[f"{chapter.url}#{fragment}"] = (
                current_page + local_page_index
            )

        current_page += count

    return page_map


# ==================================================
# Extract hierarchical Contents from the DOM
# ==================================================

async def extract_chapters(
    page,
    index_url: str,
) -> tuple[list[TocNode], list[Chapter]]:

    print("\nOpening product index page...")

    await page.goto(
        index_url,
        wait_until="domcontentloaded",
        timeout=60000,
    )

    try:
        await page.wait_for_load_state("networkidle", timeout=15000)
    except PlaywrightTimeoutError:
        pass

    actual_index_url = normalize_url(page.url)
    index = urlparse(actual_index_url)

    parts = [part for part in index.path.split("/") if part]

    category_prefix = (
        "/" + "/".join(parts[:2]) + "/"
        if len(parts) >= 2
        else index.path.rsplit("/", 1)[0] + "/"
    )

    article = page.locator(
        "article.md-content__inner"
    )

    if not await article.count():
        article = page.locator(
            ".md-content__inner.md-typeset"
        )

    if not await article.count():
        raise RuntimeError("Cannot find product index article.")

    elements = await article.locator(
        "h1, h2, h3, h4, h5, h6, a[data-preview]"
    ).evaluate_all(
        """elements => elements.map(el => {

            if (/^H[1-6]$/.test(el.tagName)) {
                return {
                    type: 'heading',
                    level: Number(el.tagName.substring(1)),
                    title: (el.innerText || el.textContent || '')
                        .replace(/\\s+/g, ' ')
                        .replace(/¶/g, '')
                        .trim()
                };
            }

            return {
                type: 'link',
                title: (el.innerText || el.textContent || '')
                    .replace(/\\s+/g, ' ')
                    .trim(),
                href: el.getAttribute('href') || ''
            };
        })"""
    )

    print(
        f"Found {sum(x['type'] == 'heading' for x in elements)} headings "
        f"and {sum(x['type'] == 'link' for x in elements)} chapter links."
    )

    roots: list[TocNode] = []
    heading_stack: list[TocNode] = []
    chapters: list[Chapter] = []
    seen_urls: set[str] = set()

    for item in elements:

        # ------------------------------------------
        # Heading
        # ------------------------------------------

        if item["type"] == "heading":

            title = clean_title(item["title"])
            html_level = item["level"]

            if not title or html_level == 1:
                continue

            level = html_level - 2

            while (
                heading_stack
                and heading_stack[-1].level >= level
            ):
                heading_stack.pop()

            node = TocNode(title=title, level=level)

            if heading_stack:
                heading_stack[-1].children.append(node)
            else:
                roots.append(node)

            heading_stack.append(node)
            continue

        # ------------------------------------------
        # Link
        # ------------------------------------------

        title = clean_title(item["title"])
        href = (item.get("href") or "").strip()

        if not title or not href or is_excluded_title(title):
            continue

        if href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue

        raw_url = urljoin(actual_index_url, href)

        raw_url, fragment = urldefrag(raw_url)

        absolute_url = normalize_url(raw_url)

        node_url = (
            absolute_url + "#" + fragment
            if fragment
            else absolute_url
        )

        parsed = urlparse(absolute_url)

        if (
            parsed.scheme not in ("http", "https")
            or parsed.netloc.lower() != index.netloc.lower()
            or not parsed.path.startswith(category_prefix)
            or is_asset_url(absolute_url)
            or absolute_url == actual_index_url
        ):
            continue

        current_heading = (
            heading_stack[-1] if heading_stack else None
        )

        # Attach a same-title link to its heading.
        if (
            current_heading
            and current_heading.title.lower() == title.lower()
        ):
            current_heading.url = node_url

        else:

            parent_level = (
                current_heading.level if current_heading else -1
            )

            node = TocNode(
                title=title,
                level=parent_level + 1,
                url=node_url,
            )

            if current_heading:
                current_heading.children.append(node)
            else:
                roots.append(node)

        if absolute_url not in seen_urls:
            seen_urls.add(absolute_url)
            chapters.append(Chapter(title, absolute_url))

    if not chapters:
        raise RuntimeError("No valid chapter links found.")

    print("\nExtracted Contents:")
    print("-" * 60)

    for node in walk_tree(roots):
        marker = " [PAGE]" if node.url else ""
        print(f"{'    ' * node.level}- {node.title}{marker}")

    print("-" * 60)
    print(f"Unique chapter pages: {len(chapters)}")

    return roots, chapters


# ==================================================
# Wait for page content and images
# ==================================================

async def wait_for_page_content(page):

    await page.evaluate(
        """async () => {

            const delay = ms =>
                new Promise(resolve => setTimeout(resolve, ms));

            const step = Math.max(window.innerHeight, 600);

            for (
                let y = 0;
                y < document.body.scrollHeight;
                y += step
            ) {
                window.scrollTo(0, y);
                await delay(150);
            }

            window.scrollTo(0, 0);
            await delay(500);

            await Promise.all(
                Array.from(document.images).map(img => {

                    if (img.complete) {
                        return Promise.resolve();
                    }

                    return new Promise(resolve => {

                        const done = () => resolve();

                        img.addEventListener('load', done, {once: true});
                        img.addEventListener('error', done, {once: true});

                        setTimeout(done, 10000);
                    });
                })
            );

            if (document.fonts?.ready) {
                await document.fonts.ready;
            }
        }"""
    )


# ==================================================
# Extract Cudy Logo
# ==================================================

async def extract_logo(
    page,
    index_url: str,
    output_path: Path,
) -> Path | None:

    print("\nExtracting Cudy Logo...")

    await page.goto(
        index_url,
        wait_until="domcontentloaded",
        timeout=60000,
    )

    image_url = await page.evaluate(
        """() => {

            const elements = document.querySelectorAll(
                'img, source, a, [style*="background"]'
            );

            for (const el of elements) {

                const values = [
                    el.currentSrc,
                    el.src,
                    el.href,
                    el.getAttribute('src'),
                    el.getAttribute('srcset'),
                    el.getAttribute('href'),
                    el.getAttribute('style')
                ];

                for (const value of values) {

                    if (!value) continue;

                    const match = String(value).match(
                        /[^\\s"'(),]*cudyicon\\.webp[^\\s"'(),]*/i
                    );

                    if (match) {
                        return new URL(match[0], location.href).href;
                    }
                }
            }

            return null;
        }"""
    )

    if not image_url:
        print("  WARNING: cudyicon.webp not found.")
        return None

    try:
        response = await page.request.get(
            image_url,
            timeout=20000,
        )

        if not response.ok:
            raise RuntimeError(f"HTTP {response.status}")

        with Image.open(BytesIO(await response.body())) as image:

            logo = image.convert("RGBA")

            # Preserve the original transparency.
            alpha = logo.getchannel("A")

            # Recolor the Cudy logo with brand blue.
            blue_logo = Image.new(
                "RGBA",
                logo.size,
                (0, 140, 255, 0),
            )

            blue_logo.putalpha(alpha)

            # Save transparent PNG.
            blue_logo.save(
                output_path,
                format="PNG",
            )

        print(f"  Saved: {output_path.name}")
        return output_path

    except Exception as exc:
        print(f"  WARNING: Logo extraction failed: {exc}")
        return None


# ==================================================
# Extract Front Panel image
# ==================================================

async def extract_front_panel(
    page,
    overview_url: str,
    output_path: Path,
) -> Path:

    print("\nExtracting Front Panel image...")

    await page.goto(
        overview_url,
        wait_until="domcontentloaded",
        timeout=60000,
    )

    try:
        await page.wait_for_load_state("networkidle", timeout=15000)
    except PlaywrightTimeoutError:
        pass

    await wait_for_page_content(page)

    article = page.locator(
        "article.md-content__inner"
    )

    if not await article.count():
        article = page.locator(
            ".md-content__inner.md-typeset"
        )

    if not await article.count():
        raise RuntimeError("Cannot find Overview article.")

    images = await article.locator("img").evaluate_all(
        """images => images.map((img, index) => ({
            index,
            alt: img.alt || '',
            title: img.title || '',
            src: img.currentSrc || img.src || '',
            width: img.naturalWidth || 0,
            height: img.naturalHeight || 0
        }))"""
    )

    if not images:
        raise RuntimeError("No images found on the Overview page.")

    selected = next(
        (
            item for item in images
            if FRONT_PANEL_PATTERN.search(
                " ".join([
                    item["alt"],
                    item["title"],
                    item["src"],
                ])
            )
        ),
        None,
    )

    # Fallback: largest meaningful image.
    if selected is None:

        candidates = [
            item for item in images
            if item["width"] >= 250 and item["height"] >= 100
        ]

        if not candidates:
            raise RuntimeError(
                "Cannot identify a suitable Front Panel image.\n"
                + "\n".join(x["src"] for x in images)
            )

        selected = max(
            candidates,
            key=lambda x: x["width"] * x["height"],
        )

        print(
            "  WARNING: No explicit Front Panel label found. "
            "Using the largest image. Please verify it."
        )

    print(f"  Selected: {selected['alt'] or selected['src']}")

    image = article.locator("img").nth(selected["index"])

    await image.scroll_into_view_if_needed()

    await image.screenshot(
        path=str(output_path),
        animations="disabled",
        timeout=20000,
    )

    if not output_path.exists() or not output_path.stat().st_size:
        raise RuntimeError("Failed to save Front Panel image.")

    print(f"  Saved: {output_path.name}")

    return output_path


# ==================================================
# Extract cover assets and model name
# ==================================================

async def extract_cover_assets(
    browser,
    index_url: str,
    chapters: list[Chapter],
    temp_dir: Path,
) -> tuple[str, Path | None, Path]:

    overview = next(
        (
            chapter for chapter in chapters
            if chapter.title.lower() == "overview"
            or "overview" in chapter.url.lower()
        ),
        None,
    )

    if overview is None:
        raise RuntimeError("Cannot find the Overview chapter.")

    logo_path = temp_dir / "cudy_logo.png"
    front_panel_path = temp_dir / "front_panel.png"

    page = await browser.new_page(
        viewport={"width": 1440, "height": 1000}
    )

    try:
        logo = await extract_logo(
            page, index_url, logo_path
        )

        await extract_front_panel(
            page, overview.url, front_panel_path
        )

        await page.goto(
            index_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        model_name = clean_title(
            await page.locator(
                "article.md-content__inner h1"
            ).first.text_content() or ""
        )

        if not model_name:
            slug = urlparse(index_url).path.rstrip("/").split("/")[-1]
            model_name = slug.replace("_", " ").upper()

        print(f"\nModel: {model_name}")

        return model_name, logo, front_panel_path

    finally:
        await page.close()


# ==================================================
# Clean webpage before PDF rendering
# ==================================================

async def clean_page(page):

    await page.evaluate(
        """() => {

            const selectors = [
                '#preview-panel',
                '#preview-full-page',
                '#preview-full-manual',
                '.preview-panel',
                '.preview-overlay',
                '[data-preview-panel]'
            ];

            selectors.forEach(selector => {
                document.querySelectorAll(selector).forEach(el => el.remove());
            });

            document.querySelectorAll('a[data-preview]').forEach(a => {
                a.removeAttribute('data-preview');
            });

            document.querySelectorAll('img').forEach(img => {
                img.loading = 'eager';
            });
        }"""
    )

    await page.add_style_tag(
        content="""

        @media print {

            html, body {
                background: #fff !important;
            }

            .md-header,
            .md-tabs,
            .md-sidebar,
            .md-footer,
            .md-top,
            .md-search,
            .md-nav,
            .md-select,
            .md-content__button,
            .md-header__button,
            .md-footer-meta {
                display: none !important;
            }

            .md-main,
            .md-main__inner,
            .md-content,
            .md-content__inner,
            article,
            main {
                max-width: 100% !important;
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }

            #preview-panel,
            #preview-panel *,
            #preview-full-page,
            #preview-full-manual {
                display: none !important;
                border: none !important;
                outline: none !important;
                box-shadow: none !important;
            }

            img,
            picture,
            figure,
            figure img,
            .md-typeset img {
                border: 0 !important;
                outline: 0 !important;
                box-shadow: none !important;
            }

            a:has(img),
            a:has(picture),
            a:has(figure) {
                border: 0 !important;
                outline: 0 !important;
                box-shadow: none !important;
                background: transparent !important;
                text-decoration: none !important;
            }

            img::before,
            img::after,
            figure::before,
            figure::after,
            a:has(img)::before,
            a:has(img)::after {
                content: none !important;
                display: none !important;
                border: 0 !important;
                box-shadow: none !important;
            }

            [style*="position: fixed"] {
                border-left: none !important;
                border-right: none !important;
                box-shadow: none !important;
            }

            a {
                color: inherit !important;
            }

            img,
            table,
            pre,
            blockquote,
            .admonition,
            figure {
                break-inside: avoid;
            }

            h1, h2, h3 {
                break-after: avoid;
            }

            thead {
                display: table-header-group;
            }

            tr {
                break-inside: avoid;
            }
        }
        """
    )


# ==================================================
# Render individual chapter PDF
# ==================================================

async def render_chapter(
    browser,
    chapter: Chapter,
    temp_dir: Path,
    number: int,
    fragments: list[str] | None = None,
) -> tuple[Path, dict[str, str]]:

    page = await browser.new_page(
        viewport={"width": 1440, "height": 1000},
        device_scale_factor=1,
    )

    output = temp_dir / f"chapter_{number:03d}.pdf"
    fragments = fragments or []
    marker_map: dict[str, str] = {}

    try:
        print(f"\n[{number}] Rendering: {chapter.title}")

        await page.goto(
            chapter.url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        try:
            await page.wait_for_load_state("networkidle", timeout=20000)
        except PlaywrightTimeoutError:
            print("  Network idle timeout; continuing.")

        await clean_page(page)
        await wait_for_page_content(page)

        if fragments:

            marker_map = await page.evaluate(
                """(fragments) => {

                    const result = {};

                    fragments.forEach((fragment, index) => {

                        const target =
                            document.getElementById(fragment) ||
                            document.querySelector(
                                `[name="${CSS.escape(fragment)}"]`
                            );

                        if (!target) {
                            console.warn(
                                'Heading not found:',
                                fragment
                            );
                            return;
                        }

                        const marker =
                            `CUDYTOC${String(index + 1).padStart(5, '0')}`;

                        const span = document.createElement('span');

                        span.textContent = marker;

                        span.style.cssText = `
                            position: absolute;
                            font-size: 1px;
                            line-height: 1px;
                            color: #ffffff;
                            opacity: 0.01;
                            pointer-events: none;
                        `;

                        target.insertAdjacentElement(
                            'afterbegin',
                            span
                        );

                        result[marker] = fragment;
                    });

                    return result;
                }""",
                fragments,
            )

        await page.pdf(
            path=str(output),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=False,
            margin=PAGE_MARGIN,
        )

        print(f"  Saved: {output.name}")
        return output, marker_map

    except Exception as exc:
        raise RuntimeError(
            f"Failed to render chapter: {chapter.title}\n"
            f"URL: {chapter.url}\n"
            f"Reason: {exc}"
        ) from exc

    finally:
        await page.close()


# ==================================================
# Image drawing helper
# ==================================================

def draw_contain(
    c,
    image_path: Path,
    x: float,
    y: float,
    max_width: float,
    max_height: float,
):
    """Draw an image while preserving its aspect ratio."""

    image = ImageReader(str(image_path))
    image_width, image_height = image.getSize()

    scale = min(
        max_width / image_width,
        max_height / image_height,
    )

    width = image_width * scale
    height = image_height * scale

    c.drawImage(
        image,
        x + (max_width - width) / 2,
        y + (max_height - height) / 2,
        width=width,
        height=height,
        preserveAspectRatio=True,
        mask="auto",
    )


# ==================================================
# Generate minimalist cover PDF
# ==================================================

def build_cover_pdf(
    model_name: str,
    logo_path: Path | None,
    front_panel_path: Path,
    output_path: Path,
) -> int:

    width, height = A4

    c = canvas.Canvas(
        str(output_path),
        pagesize=A4,
    )

    # Cudy Logo
    if logo_path and logo_path.exists():
        draw_contain(
            c,
            logo_path,
            20 * mm,
            height - 42 * mm,
            COVER_LOGO_MAX_WIDTH,
            COVER_LOGO_MAX_HEIGHT,
        )

    # Title
    title_size = (
        20 if len(model_name) > 20
        else 23 if len(model_name) > 14
        else 27
    )

    c.setFillColor(colors.HexColor(BRAND_COLOR))
    c.setFont("Helvetica-Bold", title_size)
    c.drawCentredString(
        width / 2,
        height - 83 * mm,
        "User Guide",
    )

    c.drawCentredString(
        width / 2,
        height - 100 * mm,
        model_name,
    )

    # Front Panel
    draw_contain(
        c,
        front_panel_path,
        (width - COVER_IMAGE_MAX_WIDTH) / 2,
        53 * mm,
        COVER_IMAGE_MAX_WIDTH,
        COVER_IMAGE_MAX_HEIGHT,
    )

    # Copyright
    c.setFillColor(colors.HexColor("#888888"))
    c.setFont("Helvetica", 8)
    c.drawCentredString(
        width / 2,
        20 * mm,
        "© 2026 Shenzhen Cudy Technology Co., Ltd.",
    )

    c.save()

    return len(PdfReader(str(output_path)).pages)


# ==================================================
# Dotted leader for Contents
# ==================================================

class DottedLeader(Flowable):

    def __init__(self, width: float, height: float = 12):
        super().__init__()
        self.width = width
        self.height = height

    def wrap(self, available_width, available_height):
        return self.width, self.height

    def draw(self):

        self.canv.saveState()
        self.canv.setStrokeColor(colors.HexColor("#AAAAAA"))
        self.canv.setLineWidth(0.6)
        self.canv.setDash(1, 2)

        self.canv.line(
            0,
            self.height / 2,
            self.width,
            self.height / 2,
        )

        self.canv.restoreState()


# ==================================================
# Generate hierarchical Contents PDF
# ==================================================

def build_contents_pdf(
    roots: list[TocNode],
    page_map: dict[str, int],
    body_start_index: int,
    output_path: Path,
) -> int:

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ContentsTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=CONTENTS_TITLE_FONT_SIZE,
        leading=25,
        alignment=1,
        textColor=colors.HexColor("#222222"),
        spaceAfter=7 * mm,
    )

    level_styles = [
        ParagraphStyle(
            f"ContentsLevel{level}",
            parent=styles["Normal"],
            fontName="Helvetica-Bold" if level == 0 else "Helvetica",
            fontSize=max(8.5, CONTENTS_FONT_SIZE - level * 0.2),
            leading=CONTENTS_LINE_HEIGHT,
            textColor=colors.HexColor(
                "#222222" if level == 0 else "#444444"
            ),
            leftIndent=level * CONTENTS_INDENT,
        )
        for level in range(7)
    ]

    page_style = ParagraphStyle(
        "ContentsPageNumber",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=CONTENTS_LINE_HEIGHT,
        alignment=2,
        textColor=colors.HexColor("#555555"),
    )

    story = [
        Spacer(1, 5 * mm),
        Paragraph("Contents", title_style),
    ]

    rows = []

    for node in walk_tree(roots):

        page_index = first_page_index_in_subtree(
            node,
            page_map,
        )

        if page_index is None:
            continue

        page_number = page_index - body_start_index + 1

        if page_number < 1:
            continue

        style = level_styles[
            min(node.level, len(level_styles) - 1)
        ]

        rows.append([
            Paragraph(escape_xml(node.title), style),
            DottedLeader(36 * mm, CONTENTS_LINE_HEIGHT),
            Paragraph(str(page_number), page_style),
        ])

    if rows:
        table = Table(
            rows,
            colWidths=[122 * mm, 36 * mm, 12 * mm],
            hAlign="LEFT",
        )

        table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (2, 0), (2, -1), "RIGHT"),
            ("LEFTPADDING", (0, 0), (-1, -1), 1),
            ("RIGHTPADDING", (0, 0), (-1, -1), 1),
            ("TOPPADDING", (0, 0), (-1, -1), 1.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
        ]))

        story.append(table)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=CONTENTS_RIGHT_MARGIN,
        leftMargin=CONTENTS_LEFT_MARGIN,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )

    doc.build(story)

    return len(PdfReader(str(output_path)).pages)

# ==================================================
# Add body headers and page numbers
# ==================================================

def add_headers_and_page_numbers(
    input_pdf: Path,
    output_pdf: Path,
    body_start_index: int,
    model_name: str,
    logo_path: Path | None,
):
    """
    Add model name on the left, Cudy Logo on the right,
    and continuous page numbers at the bottom.

    Cover and Contents pages remain unchanged.
    """

    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()

    writer.clone_document_from_reader(reader)

    total_pages = len(writer.pages)
    body_total = total_pages - body_start_index

    logo = (
        ImageReader(str(logo_path))
        if logo_path and logo_path.exists()
        else None
    )

    for index, page in enumerate(writer.pages):

        if index < body_start_index:
            continue

        width = float(page.mediabox.width)
        height = float(page.mediabox.height)

        packet = BytesIO()

        c = canvas.Canvas(
            packet,
            pagesize=(width, height),
        )

        # ------------------------------------------
        # Header: model name on the left
        # ------------------------------------------

        header_y = height - HEADER_TOP_MARGIN - 3 * mm

        c.setFillColor(colors.HexColor("#444444"))
        c.setFont("Helvetica-Bold", 8.5)

        c.drawString(
            HEADER_LEFT_MARGIN,
            header_y,
            model_name,
        )

        # ------------------------------------------
        # Header: Cudy Logo on the right
        # ------------------------------------------

        if logo:

            image_width, image_height = logo.getSize()

            scale = min(
                HEADER_LOGO_WIDTH / image_width,
                HEADER_LOGO_HEIGHT / image_height,
            )

            logo_width = image_width * scale
            logo_height = image_height * scale

            logo_x = width - HEADER_RIGHT_MARGIN - logo_width
            logo_y = height - HEADER_TOP_MARGIN - logo_height

            c.drawImage(
                logo,
                logo_x,
                logo_y,
                width=logo_width,
                height=logo_height,
                preserveAspectRatio=True,
                mask="auto",
            )

        # ------------------------------------------
        # Header separator
        # ------------------------------------------

        line_y = height - 14 * mm

        c.setStrokeColor(colors.HexColor(HEADER_LINE_COLOR))
        c.setLineWidth(0.5)

        c.line(
            HEADER_LEFT_MARGIN,
            line_y,
            width - HEADER_RIGHT_MARGIN,
            line_y,
        )

        # ------------------------------------------
        # Footer: continuous page numbers
        # ------------------------------------------

        page_number = index - body_start_index + 1

        c.setFillColor(colors.HexColor("#666666"))
        c.setFont("Helvetica", 8)

        c.drawCentredString(
            width / 2,
            FOOTER_BOTTOM_MARGIN,
            f"{page_number} / {body_total}",
        )

        c.save()
        packet.seek(0)

        overlay = PdfReader(packet).pages[0]
        page.merge_page(overlay)

    with open(output_pdf, "wb") as f:
        writer.write(f)

# ==================================================
# 新增 PDF 内部标题页码识别函数
# ==================================================

def find_fragment_pages(
    pdf_path: Path,
    marker_map: dict[str, str],
) -> dict[str, int]:
    """
    Find the actual PDF page containing each internal heading marker.

    Returns:
        {fragment: zero_based_local_page_index}
    """

    reader = PdfReader(str(pdf_path))

    result = {}

    for page_index, page in enumerate(reader.pages):

        text = page.extract_text() or ""

        for marker, fragment in marker_map.items():

            if fragment in result:
                continue

            if marker in text:
                result[fragment] = page_index

    return result

# ==================================================
# Add hierarchical PDF bookmarks
# ==================================================

def add_tree_bookmarks(
    writer: PdfWriter,
    nodes: list[TocNode],
    page_map: dict[str, int],
    parent_ref=None,
):

    for node in nodes:

        page_index = first_page_index_in_subtree(
            node,
            page_map,
        )

        current_parent = parent_ref

        if page_index is not None:
            current_parent = writer.add_outline_item(
                node.title,
                page_index,
                parent=parent_ref,
            )

        add_tree_bookmarks(
            writer,
            node.children,
            page_map,
            current_parent,
        )


# ==================================================
# Merge cover, Contents and chapter PDFs
# ==================================================

def merge_pdfs(
    roots: list[TocNode],
    chapters: list[Chapter],
    chapter_pdfs: list[Path],
    cover_pdf: Path,
    contents_pdf: Path,
    output_path: Path,
    fragment_page_maps: list[dict[str, int]] | None = None,
) -> tuple[int, int]:

    if len(chapters) != len(chapter_pdfs):
        raise ValueError("Chapter PDF count mismatch.")

    writer = PdfWriter()

    # Cover
    cover_reader = PdfReader(str(cover_pdf))
    for page in cover_reader.pages:
        writer.add_page(page)

    cover_pages = len(cover_reader.pages)

    # Contents
    contents_reader = PdfReader(str(contents_pdf))
    for page in contents_reader.pages:
        writer.add_page(page)

    contents_pages = len(contents_reader.pages)

    writer.add_outline_item("Contents", cover_pages)

    # Body
    body_start_index = cover_pages + contents_pages

    chapter_page_counts = [
        len(PdfReader(str(path)).pages) for path in chapter_pdfs
    ]
    page_map = get_page_map(
        chapters,
        chapter_page_counts,
        body_start_index,
        fragment_page_maps,
    )

    for pdf_path in chapter_pdfs:
        reader = PdfReader(str(pdf_path))
        for page in reader.pages:
            writer.add_page(page)

    # Hierarchical bookmarks
    add_tree_bookmarks(writer, roots, page_map)

    # Validate before writing/returning.
    expected_body_pages = sum(chapter_page_counts)
    actual_body_pages = len(writer.pages) - body_start_index

    if expected_body_pages != actual_body_pages:
        raise RuntimeError(
            "PDF page count mismatch: "
            f"Expected {expected_body_pages}, "
            f"got {actual_body_pages}."
        )

    with open(output_path, "wb") as f:
        writer.write(f)

    return body_start_index, contents_pages    

# ==================================================
# Generate Contents with stable page numbers
# ==================================================

def generate_contents(
    roots: list[TocNode],
    chapters: list[Chapter],
    chapter_page_counts: list[int],
    cover_page_count: int,
    contents_path: Path,
    fragment_page_maps: list[dict[str, int]] | None = None,
) -> int:
    """
    Recalculate Contents until its page count stabilizes.
    """

    contents_page_count = 1

    for _ in range(10):

        body_start = cover_page_count + contents_page_count

        page_map = get_page_map(
            chapters,
            chapter_page_counts,
            body_start,
            fragment_page_maps,
        )

        new_count = build_contents_pdf(
            roots,
            page_map,
            body_start,
            contents_path,
        )

        if new_count == contents_page_count:
            return new_count

        contents_page_count = new_count

    raise RuntimeError(
        "Contents page count did not stabilize after 10 attempts."
    )


# ==================================================
# Main export process
# ==================================================

async def export_manual(
    index_url: str,
    output_path: Path,
    keep_temp: bool = False,
):

    index_url = normalize_url(index_url)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp_dir = output_path.parent / f"{output_path.stem}_temp"
    temp_dir.mkdir(parents=True, exist_ok=True)

    cover_path = temp_dir / "cover.pdf"
    contents_path = temp_dir / "contents.pdf"
    merged_path = temp_dir / "merged.pdf"

    print("\n" + "=" * 60)
    print("CUDY MODULAR MANUAL PDF EXPORTER")
    print("=" * 60)

    async with async_playwright() as p:

        browser = await p.chromium.launch()

        try:

            # --------------------------------------
            # Extract chapters
            # --------------------------------------

            index_page = await browser.new_page()

            try:
                roots, chapters = await extract_chapters(
                    index_page,
                    index_url,
                )
            finally:
                await index_page.close()

            # --------------------------------------
            # Extract cover assets
            # --------------------------------------

            (
                model_name,
                logo_path,
                front_panel_path,
            ) = await extract_cover_assets(
                browser,
                index_url,
                chapters,
                temp_dir,
            )

            # --------------------------------------
            # Render chapters
            # --------------------------------------

            fragment_targets = collect_fragment_targets(roots)
            chapter_pdfs = []
            chapter_fragment_page_maps = []

            for number, chapter in enumerate(chapters, start=1):

                pdf_path, marker_map = await render_chapter(
                    browser,
                    chapter,
                    temp_dir,
                    number,
                    fragments=fragment_targets.get(chapter.url, []),
                )

                chapter_pdfs.append(pdf_path)
                chapter_fragment_page_maps.append(
                    find_fragment_pages(pdf_path, marker_map)
                )

        finally:
            await browser.close()

    # ==================================================
    # Build cover
    # ==================================================

    print("\nGenerating cover...")

    cover_page_count = build_cover_pdf(
        model_name,
        logo_path,
        front_panel_path,
        cover_path,
    )

    # ==================================================
    # Get chapter page counts
    # ==================================================

    chapter_page_counts = [
        len(PdfReader(str(path)).pages)
        for path in chapter_pdfs
    ]

    # ==================================================
    # Generate Contents
    # ==================================================

    print("\nGenerating Contents...")

    contents_page_count = generate_contents(
        roots,
        chapters,
        chapter_page_counts,
        cover_page_count,
        contents_path,
        chapter_fragment_page_maps,
    )

    # ==================================================
    # Merge PDFs and bookmarks
    # ==================================================

    print("\nMerging PDFs...")

    body_start_index, contents_page_count = merge_pdfs(
        roots,
        chapters,
        chapter_pdfs,
        cover_path,
        contents_path,
        merged_path,
        chapter_fragment_page_maps,
    )

    # ==================================================
    # Add headers and page numbers
    # ==================================================

    print("\nAdding body headers and page numbers...")

    add_headers_and_page_numbers(
        merged_path,
        output_path,
        body_start_index,
        model_name,
        logo_path,
    )

    # ==================================================
    # Cleanup
    # ==================================================

    if not keep_temp:
        shutil.rmtree(temp_dir, ignore_errors=True)

    # ==================================================
    # Export summary
    # ==================================================

    final_reader = PdfReader(str(output_path))

    total_pages = len(final_reader.pages)
    body_pages = total_pages - body_start_index

    print("\n" + "=" * 60)
    print("PDF EXPORT COMPLETED")
    print("=" * 60)

    print(f"Output: {output_path.resolve()}")
    print(f"Model: {model_name}")
    print(f"Chapters: {len(chapters)}")
    print(f"Cover pages: {cover_page_count}")
    print(f"Contents pages: {contents_page_count}")
    print(f"Body pages: {body_pages}")
    print(f"Total PDF pages: {total_pages}")

    print("=" * 60)


# ==================================================
# Command line
# ==================================================

def main():

    parser = argparse.ArgumentParser(
        description="Cudy Modular Manual PDF Exporter"
    )

    parser.add_argument(
        "--url",
        required=True,
        help="Product index page URL",
    )

    parser.add_argument(
        "--output",
        default="User_Manual.pdf",
        help="Output PDF file",
    )

    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Keep intermediate PDF files",
    )

    args = parser.parse_args()

    try:
        asyncio.run(
            export_manual(
                args.url,
                Path(args.output),
                args.keep_temp,
            )
        )

    except KeyboardInterrupt:
        print("\nExport cancelled.")
        sys.exit(130)

    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
