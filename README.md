# 📘 Adobe Hackathon Round 1A – PDF Outline Extractor

## 🚀 Overview

This project is a lightweight, Dockerized solution for extracting structured outlines from PDF files. It automatically identifies the **Title**, **H1**, **H2**, and **H3** headings with their corresponding text and page numbers, outputting the result in a clean JSON structure.

This tool is the foundational component for building semantic, intelligent PDF applications as envisioned in the **“Connecting the Dots”** challenge by Adobe.

---

## 🛠 Features

- ✅ Title & Heading Extraction (H1, H2, H3)
- 📄 Page Number Mapping
- ⚡ High-speed Parsing (≤ 10 seconds for 50 pages)
- 📦 Lightweight, CPU-only (model size ≤ 200MB)
- 🔒 Runs fully offline – no internet dependency
- 🔁 Modular & extensible for Round 1B

---

## 🧱 Project Structure

```
.
├── main.py                # Core PDF processing logic
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── README.md              # Documentation (this file)
├── input/                 # Input directory (PDFs)
└── output/                # Output directory (JSONs)
```

---

## 🧪 Sample Output Format

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

## 🐳 How to Build and Run

### Step 1: Build Docker Image

```bash
docker build --platform linux/amd64 -t pdf_outline_extractor .
```

### Step 2: Run the Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf_outline_extractor
```

> This will process all PDFs in `/app/input` and generate corresponding `.json` outline files in `/app/output`.

---

## 📦 Requirements
All dependencies are installed inside the container. For reference:

```
Python 3.10+
PyMuPDF==1.23.7
```

---

## 🔍 Approach Summary
- **Text Extraction**: Uses `PyMuPDF` to extract raw text and layout information including font sizes.
- **Heuristics**: Heading levels are inferred based on relative font sizes and layout heuristics.
- **Title Detection**: The largest, most prominent early-page text is classified as the document title.
- **Output Generation**: JSON output is formatted exactly as per the provided ground truth sample.

---

## 👨‍💻 Authors
Developed by Team Hack_Coders for Adobe India Hackathon 2025  
Engineering Student | AI Enthusiast
