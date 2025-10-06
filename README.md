# 🔗 LinkSpider

> **`🐍 Python`** **`🌐 Web Crawling`** **`📊 Visualization`** **`🔗 Network Analysis`**

A powerful website link analysis tool that crawls websites and generates visual link graphs. Built with Python, NetworkX, and BeautifulSoup.

---

## ✨ Features

- **🕷️ Website Crawling**: Automatically crawl websites up to specified depth
- **📈 Link Graph Visualization**: Generate PNG visualizations of website link structures  
- **💾 JSON Export**: Save crawl data for further analysis
- **⏸️ Interrupt Handling**: Automatically save progress on Ctrl+C interruption
- **🎯 Same-Domain Filtering**: Focus on internal links within the target domain
- **🎚️ Configurable Depth**: Control crawl depth from 1 to 5 levels

---

## 🚀 Installation

### 📋 Prerequisites
- **`🐍 Python 3.7+`**
- **`📦 pip package manager`**

### 📥 Dependencies
```bash
pip install requests beautifulsoup4 networkx matplotlib lxml
```

# 📁 Project structure
```linkspider/
├── main.py                 # Main entry point
├── spider/
│   ├── crawler.py         # Website crawling logic
│   ├── parser.py          # HTML link extraction
│   ├── visualizer.py      # Graph visualization
│   └── __init__.py
├── utils/
│   └── url_utils.py       URL normalization utilities
└── README.md
```

# 💻 Usage
## 🟢 Basic crawl
`python main.py --url https://example.com --depth 2 --output graph.png`

## 🔵 Advanced
`python main.py --url https://example.com --depth 3 --output my_analysis.png`

`python main.py --url https://example.com --depth 4 --output deep_graph.png\`

# ⚙️ Parameters
```
--url: Starting URL (required)

--depth: Crawl depth (1-5, default: 2)

--output: Output PNG filename (default: graph.png)
```

# ⚡ Quick Start
1) Install dependencies:
   ```pip install requests beautifulsoup4 networkx matplotlib lxml```
2) Run your first crawl:
   ```python main.py --url https://httpbin.org --depth 1 --output my_first_graph.png```
3) Check the results:
   `🖼️ my_first_graph.png` - Visual graph

   `📄 httpbin_org_graph.json` - Raw data
