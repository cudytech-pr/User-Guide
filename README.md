# Cudy User Guide

<p align="center">
  <strong>Official Product Documentation</strong><br>
  User manuals, setup guides, and technical documentation for Cudy products.
</p>

<p align="center">
  <a href="#english">English</a> |
  <a href="#中文">简体中文</a>
</p>

<p align="center">
  <a href="https://docs.cudy.com/">Documentation Website</a> ·
  <a href="https://github.com/cudytech-pr/User-Guide">GitHub Repository</a>
</p>

---

<a id="english"></a>

# English

## Overview

**Cudy User Guide** is the official documentation repository for Cudy networking products.

It provides product manuals, setup instructions, feature descriptions, and troubleshooting guides to help users understand, configure, and manage their Cudy devices.

The documentation is built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), and published as an online documentation website.

- **Documentation Website:** https://docs.cudy.com/
- **GitHub Repository:** https://github.com/cudytech-pr/User-Guide

## Documentation Scope

Documentation is organized by product category and model, and may include:

- Product overviews and hardware information
- Installation and initial setup
- Web interface and app configuration
- Network and wireless settings
- Advanced features and functionality
- Troubleshooting and FAQs

## Getting Started

Follow these steps to set up the documentation project locally.

### Prerequisites

Make sure the following tools are installed:

- Python 3.10 or later
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/cudytech-pr/User-Guide.git
cd User-Guide
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Documentation Locally

```bash
mkdocs serve
```

Open the local development server:

http://127.0.0.1:8000/

MkDocs automatically reloads the site when documentation files are modified.

### 5. Build the Documentation

```bash
mkdocs build
```

The generated static website is saved in the `site/` directory.

## Download PDF Manuals

Use the **Cudy PDF Exporter** to generate a PDF manual directly from a product's online documentation page.

The exporter runs locally on your computer. You do not need to clone the entire documentation repository or set up a MkDocs environment.

### Prerequisites

- Python 3.10 or later
- An internet connection
- The `export_manual.py` script from this repository

### 1. Download the Export Script

1. Open the [Cudy User Guide repository](https://github.com/cudytech-pr/User-Guide).
2. Locate `export_manual.py`.
3. Open the file and click **Raw**.
4. Save it to a folder on your computer.

For example:

```text
Cudy-PDF-Exporter/
└── export_manual.py
```

### 2. Install Python Dependencies

Open a terminal or Command Prompt in the folder containing `export_manual.py`.

Install the required Python packages:

```bash
python -m pip install playwright pypdf reportlab pillow
```

### 3. Install Chromium

The exporter uses Playwright to render web pages. Install its Chromium browser:

```bash
python -m playwright install chromium
```

This step is required even if Playwright has already been installed.

### 4. Generate a PDF Manual

Run the following command:

```bash
python export_manual.py --url "https://docs.cudy.com/user_guide/switch/gs1024e/" --output "GS1024E_User_Guide.pdf"
```

Replace the URL with the online documentation page for your product.

**Command options:**

| Option | Required | Description |
|---|---|---|
| `--url` | Yes | URL of the product documentation homepage |
| `--output` | No | Output PDF filename or path. Defaults to `User_Manual.pdf`. |
| `--keep-temp` | No | Keep intermediate files after export. |

### 5. Find Your PDF

Once the export is complete, the PDF is saved to the specified output path.

For example:

```text
Cudy-PDF-Exporter/
├── export_manual.py
└── GS1024E_User_Guide.pdf
```

Temporary files are automatically cleaned up after a successful export unless `--keep-temp` is specified.

**Note:** The exporter accesses the online documentation and its resources, so an internet connection is required. PDF generation and processing take place locally on your computer.

## Documentation Workflow

The typical documentation workflow is:

```text
Edit Markdown Files
        ↓
Preview Locally
        ↓
Check Content and Links
        ↓
Build Documentation
        ↓
Commit and Push Changes
        ↓
Deploy to Documentation Website
```

## Contributing

To maintain documentation quality and consistency:

1. Follow the existing directory structure and naming conventions.
2. Use clear, concise, and user-friendly language.
3. Keep terminology consistent across products.
4. Verify product-specific features and specifications before publishing.
5. Check images, links, formatting, and navigation.
6. Preview changes locally and verify the build before submitting changes.

For product-specific differences, always refer to the corresponding model specifications.

## Troubleshooting

| Issue | Suggested Solution |
|---|---|
| `python` is not recognized | Reinstall Python and enable **Add Python to PATH** during installation. |
| `ModuleNotFoundError` | Install the required packages using `python -m pip install playwright pypdf reportlab pillow`. |
| Chromium executable not found | Run `python -m playwright install chromium`. |
| PDF export fails to load a page | Check the documentation URL and your internet connection. |

## License

Please refer to the repository for applicable licensing and usage terms.

---

<a id="中文"></a>

# 简体中文

## 项目简介

**Cudy User Guide** 是 Cudy 网络设备的官方产品文档仓库。

项目提供产品用户手册、安装配置指南、功能说明及故障排查文档，帮助用户了解、配置和管理 Cudy 产品。

文档网站基于 [MkDocs](https://www.mkdocs.org/) 和 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 构建并发布。

- **在线文档：** https://docs.cudy.com/
- **GitHub 仓库：** https://github.com/cudytech-pr/User-Guide

## 文档范围

项目按照产品类别和具体机型组织文档，主要包括：

- 产品概览与硬件信息
- 设备安装与初始配置
- Web 管理界面及 App 配置
- 网络与无线设置
- 高级功能与特性说明
- 常见问题与故障排查

## 本地运行

### 环境要求

请确保已安装：

- Python 3.10 或更高版本
- pip
- Git

### 1. 克隆项目

```bash
git clone https://github.com/cudytech-pr/User-Guide.git
cd User-Guide
```

### 2. 创建虚拟环境

```bash
python -m venv .venv
```

激活虚拟环境：

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. 安装依赖

```bash
python -m pip install -r requirements.txt
```

### 4. 启动本地预览

```bash
mkdocs serve
```

浏览器访问：

http://127.0.0.1:8000/

修改 Markdown 文件后，页面会自动刷新。

### 5. 构建文档

```bash
mkdocs build
```

构建完成后，生成的网站文件位于 `site/` 目录。

## 下载 PDF 用户手册

使用仓库中的 **Cudy PDF Exporter**，即可直接从产品在线文档页面生成 PDF 用户手册。

PDF 导出脚本在本地运行，无需克隆整个文档仓库，也无需配置 MkDocs 环境。

### 环境要求

- Python 3.10 或更高版本
- 可正常访问互联网
- 从本仓库下载的 `export_manual.py` 脚本

### 1. 下载导出脚本

1. 打开 [Cudy User Guide GitHub 仓库](https://github.com/cudytech-pr/User-Guide)。
2. 找到 `export_manual.py` 文件。
3. 打开文件，点击 **Raw**。
4. 将脚本保存到电脑上的一个文件夹中。

例如：

```text
Cudy-PDF-Exporter/
└── export_manual.py
```

### 2. 安装 Python 依赖

在存放 `export_manual.py` 的文件夹中打开终端或命令提示符。

执行以下命令：

```bash
python -m pip install playwright pypdf reportlab pillow
```

### 3. 安装 Chromium 浏览器

PDF 导出脚本使用 Playwright 渲染网页，因此还需要安装 Chromium：

```bash
python -m playwright install chromium
```

即使已经安装 Playwright，也需要执行这一步。

### 4. 生成 PDF 用户手册

执行以下命令：

```bash
python export_manual.py --url "https://docs.cudy.com/user_guide/switch/gs1024e/" --output "GS1024E_User_Guide.pdf"
```

将示例 URL 替换为对应产品的在线文档首页链接即可。

**命令参数说明：**

| 参数 | 是否必填 | 说明 |
|---|---|---|
| `--url` | 是 | 产品在线文档首页 URL |
| `--output` | 否 | PDF 输出文件名或路径，默认为 `User_Manual.pdf` |
| `--keep-temp` | 否 | 保留导出过程中生成的临时文件 |

### 5. 获取 PDF 文件

导出完成后，PDF 文件将保存到指定位置。

例如：

```text
Cudy-PDF-Exporter/
├── export_manual.py
└── GS1024E_User_Guide.pdf
```

导出成功后，脚本会自动清理临时文件；如果指定了 `--keep-temp`，则会保留这些文件。

**注意：** 导出过程需要访问在线文档及其相关资源，因此必须保持网络连接。PDF 的生成和处理均在本地电脑完成。

## 文档维护流程

```text
编辑 Markdown 文档
        ↓
本地预览
        ↓
检查内容与链接
        ↓
构建文档
        ↓
提交并推送代码
        ↓
发布至在线文档网站
```

## 文档贡献规范

为了保持文档质量和一致性，建议遵循以下规范：

1. 遵循现有的目录结构和文件命名规范。
2. 使用清晰、简洁、易理解的语言。
3. 保持不同产品之间的术语一致性。
4. 发布前核对具体机型的功能和技术规格。
5. 检查图片、链接、排版和导航。
6. 修改完成后，先进行本地预览和构建验证。

涉及不同机型的功能差异时，请以对应机型的实际规格为准。

## 常见问题

| 问题 | 解决方法 |
|---|---|
| 无法识别 `python` 命令 | 重新安装 Python，并在安装时勾选 **Add Python to PATH**。 |
| 出现 `ModuleNotFoundError` | 执行 `python -m pip install playwright pypdf reportlab pillow` 安装依赖。 |
| 找不到 Chromium 浏览器 | 执行 `python -m playwright install chromium`。 |
| PDF 导出时网页加载失败 | 检查文档 URL 是否正确，以及网络连接是否正常。 |

## 许可证

项目的具体许可和使用条款请参阅 GitHub 仓库中的相关说明。

---

<p align="center">
  <a href="https://docs.cudy.com/">Official Documentation</a> ·
  <a href="https://github.com/cudytech-pr/User-Guide">GitHub Repository</a>
</p>

<p align="center">
  © Cudy Technology. All rights reserved.
</p>