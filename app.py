# app.py
# -*- coding: utf-8 -*-
"""
Streamlit Universal File-to-Text Converter

A minimal Streamlit app that converts uploaded files (Word, Excel, PowerPoint,
PDF, HTML, etc.) into Markdown-formatted plain text using the MarkItDown library.
"""

import streamlit as st
from markitdown import MarkItDown
import base64
import os

st.set_page_config(
    page_title="Universal File-to-Text Converter",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Universal File-to-Text Converter")
st.write("Drag & drop your file below. It will be converted into plain text with Markdown formatting.")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a document",
    type=["docx", "pptx", "xlsx", "xlsm", "pdf", "html", "txt", "zip"],
    accept_multiple_files=False
)

def convert_to_text(file):
    """Convert uploaded file to markdown text."""
    md = MarkItDown()
    try:
        result = md.convert(file)
        if result and result.text_content:
            return result.text_content
        else:
            return "⚠️ Error: Conversion returned no text content."
    except Exception as e:
        return f"⚠️ An error occurred during conversion: {e}"

def download_link(text_content, filename="converted_text.txt"):
    """Generate a download link for converted text."""
    b64 = base64.b64encode(text_content.encode()).decode()
    href = f'<a href="data:text/plain;base64,{b64}" download="{filename}">📥 Download Converted File</a>'
    return href

if uploaded_file is not None:
    # Save temporarily (needed for markitdown)
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded: {uploaded_file.name}")

    # Convert file
    with st.spinner("Converting file..."):
        text_output = convert_to_text(uploaded_file.name)

    # Preview first 1000 chars
    st.subheader("🔍 Preview (first 1000 characters):")
    st.text(text_output[:1000])

    # Download link
    download_filename = os.path.splitext(uploaded_file.name)[0] + ".txt"
    st.markdown(download_link(text_output, download_filename), unsafe_allow_html=True)

    # Clean up temp file
    os.remove(uploaded_file.name)
