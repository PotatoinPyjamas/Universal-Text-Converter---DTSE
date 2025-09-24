

# 📄 Universal File-to-Text Converter

A lightweight Streamlit app that converts uploaded files (Word, Excel, PowerPoint, PDF, HTML, TXT, ZIP, etc.) into **plain text with Markdown formatting**.  

Built with [Streamlit](https://streamlit.io/) and [MarkItDown](https://pypi.org/project/markitdown/).

---

## 🚀 Features
- Drag & drop file upload  
- Automatic conversion to Markdown-formatted text  
- Preview of the **first 1000 characters**  
- Download the full converted file as `.txt`  
- Supports common formats:
  - **Word** (`.docx`)
  - **PowerPoint** (`.pptx`)
  - **Excel** (`.xlsx`, `.xlsm`)
  - **PDF** (`.pdf`)
  - **HTML** (`.html`)
  - **Text** (`.txt`)
  - **ZIP archives** (contents extracted and processed)

---

## 📦 Installation (Local)

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/universal-file-to-text.git
cd universal-file-to-text
pip install -r requirements.txt
