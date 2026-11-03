document.addEventListener("DOMContentLoaded", () => {

    // --- 1. 移动端检测与退出逻辑 ---
    const MOBILE_MAX_WIDTH = 960;

    if (window.innerWidth <= MOBILE_MAX_WIDTH) {
        document.querySelectorAll("a[data-preview]").forEach(link => {
            link.removeAttribute("data-preview");
        });
        return;
    }

    // --- 2. 创建预览面板 ---
    const panel = document.createElement("div");
    panel.id = "preview-panel";

    panel.innerHTML = `
      <div class="preview-header">
        <span class="title">View the Details</span>

        <div class="preview-header-actions">
          <a id="preview-full-page"
             href="#"
             target="_blank"
             rel="noopener noreferrer">
            Open in Full Page ↗
          </a>
          <button id="preview-close" aria-label="Close preview">✕</button>
        </div>
      </div>

      <div id="preview-resizer" aria-hidden="true"></div>

      <div class="preview-body">
        <div class="content"></div>
      </div>
    `;

    document.body.appendChild(panel);

    const closeBtn = panel.querySelector("#preview-close");
    const contentDiv = panel.querySelector(".content");
    const resizer = panel.querySelector("#preview-resizer");
    const fullPageLink = panel.querySelector("#preview-full-page");

    // --- 3. 布局 header/footer ---
    function layoutPanel() {
        const headerEl = document.querySelector(
            "header, .md-header, .md-header__inner"
        );
        const footerEl = document.querySelector("footer, .md-footer");

        const headerH = headerEl
            ? headerEl.getBoundingClientRect().height
            : 0;

        const footerH = footerEl
            ? footerEl.getBoundingClientRect().height
            : 0;

        panel.style.top = headerH + "px";
        panel.style.height = Math.max(
            200,
            window.innerHeight - headerH - footerH
        ) + "px";
    }

    layoutPanel();
    window.addEventListener("resize", layoutPanel);
    setTimeout(layoutPanel, 500);

    // --- 4. 打开 / 关闭预览面板 ---
    function openPanel() {
        document.body.classList.add("preview-open");
        panel.classList.add("open");
        layoutPanel();

        const mainContent = document.querySelector(".md-content");

        if (mainContent) {
            const previewWidth = getComputedStyle(document.documentElement)
                .getPropertyValue("--preview-width")
                .trim();

            mainContent.style.width = `calc(100% - ${previewWidth})`;
        }

        try {
            document.dispatchEvent(new CustomEvent("md-sidebar:close"));
        } catch (e) {}
    }

    function closePanel() {
        document.body.classList.remove("preview-open");
        panel.classList.remove("open");

        const mainContent = document.querySelector(".md-content");

        if (mainContent) {
            mainContent.style.width = "";
        }
    }

    closeBtn.addEventListener("click", closePanel);

    document.addEventListener("keydown", e => {
        if (e.key === "Escape") {
            closePanel();
        }
    });

    document.addEventListener("click", e => {
        if (
            panel.classList.contains("open") &&
            !panel.contains(e.target) &&
            !e.target.closest("[data-preview]")
        ) {
            closePanel();
        }
    });

    // --- 5. 加载预览内容 ---
    function loadPreview(url, anchor = "") {

        // 判断是否为图片链接
        const isImageURL = href =>
            /\.(jpe?g|png|gif|webp|bmp|svg)(\?.*)?$/i.test(href);

        // 更新全页面打开链接
        // 指向当前正在预览的页面，而不是外层页面
        const previewURL = new URL(url, window.location.href);

        fullPageLink.href =
            previewURL.pathname +
            previewURL.search +
            previewURL.hash;

        fetch(previewURL.pathname + previewURL.search)
            .then(res => {
                if (!res.ok) {
                    throw new Error("Unable to load the page.");
                }
                return res.text();
            })
            .then(html => {
                const doc = new DOMParser().parseFromString(
                    html,
                    "text/html"
                );

                const pageContent =
                    doc.querySelector(".md-content") || doc.body;

                contentDiv.innerHTML = pageContent.innerHTML;

                openPanel();

                // 定位到指定锚点
                if (anchor) {
                    setTimeout(() => {
                        const target = contentDiv.querySelector(
                            `#${CSS.escape(anchor)}`
                        );

                        if (target) {
                            target.scrollIntoView({
                                behavior: "smooth"
                            });
                        }
                    }, 60);
                }

                // 处理预览内容中的内部链接
                contentDiv.querySelectorAll("a").forEach(a => {
                    const href = a.getAttribute("href");

                    if (
                        !href ||
                        href.startsWith("http") ||
                        href.startsWith("mailto:") ||
                        href.startsWith("javascript:")
                    ) {
                        return;
                    }

                    // 图片链接不拦截，保留默认行为
                    if (isImageURL(href)) {
                        return;
                    }

                    a.addEventListener("click", ev => {
                        ev.preventDefault();

                        const newURL = new URL(
                            href,
                            previewURL
                        );

                        loadPreview(
                            newURL.pathname + newURL.search + newURL.hash,
                            newURL.hash.replace("#", "")
                        );
                    });
                });
            })
            .catch(err => {
                contentDiv.innerHTML = `
                  <div class="md-alert md-alert--error">
                    <strong>Preview failed:</strong>
                    ${String(err.message || err)}
                  </div>
                `;

                openPanel();
            });
    }

    // --- 6. 绑定 data-preview 链接 ---
    document.querySelectorAll("a[data-preview]").forEach(link => {
        link.addEventListener("click", e => {
            e.preventDefault();

            const full = new URL(link.href, window.location.href);

            loadPreview(
                full.pathname + full.search + full.hash,
                full.hash.replace("#", "")
            );
        });
    });

    // --- 7. 拖拽调整面板宽度 ---
    let isDragging = false;

    resizer.addEventListener("mousedown", e => {
        isDragging = true;
        document.body.classList.add("resizing");
        e.preventDefault();
    });

    document.addEventListener("mousemove", e => {
        if (!isDragging) return;

        const panelRight = window.innerWidth - e.clientX;

        let percent = (panelRight / window.innerWidth) * 100;
        percent = Math.min(80, Math.max(30, percent));

        panel.style.width = `${percent}%`;

        document.documentElement.style.setProperty(
            "--preview-width",
            `${percent}%`
        );

        const mainContent = document.querySelector(".md-content");

        if (
            mainContent &&
            document.body.classList.contains("preview-open")
        ) {
            mainContent.style.width = `calc(100% - ${percent}%)`;
        }
    });

    document.addEventListener("mouseup", () => {
        if (isDragging) {
            isDragging = false;
            document.body.classList.remove("resizing");
        }
    });

});