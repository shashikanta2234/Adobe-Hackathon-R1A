# 📘 Adobe Hackathon Round 1A – PDF Outline Extractor (Multilingual Support)

## 🚀 Overview

This project is a robust, Dockerized solution for extracting structured outlines from PDF documents. It identifies the **Title**, **H1**, **H2**, and **H3** headings along with their corresponding page numbers and also detects the **dominant language** of the document.

This solution is built for Round 1A of the Adobe India Hackathon 2025 — part of the “Connecting the Dots” Challenge.

---

## 🛠 Features

- ✅ Title & Heading Extraction (H1, H2, H3)
- 🌐 **Multilingual support** for Unicode PDFs (Hindi, Japanese, etc.)
- 🧠 **Language detection** using `langdetect`
- 📄 Page Number Mapping
- ⚡ High-speed Parsing (≤ 10 seconds for 50 pages)
- 📦 Lightweight, CPU-only (model size ≤ 200MB)
- 🔒 Runs fully offline – no internet dependency

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
  ],
  "language": "en"
}
```

---

## 🐳 How to Build and Run

### Step 1: Build Docker Image

```bash
docker build --platform linux/amd64 -t pdf_outline_extractor .
```
or 
```bash
sudo docker build --platform linux/amd64 -t pdf_outline_extractor .
```

### Step 2: Run the Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf_outline_extractor
```
or

```bash
sudo docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf_outline_extractor
```
> This will process all PDFs in `/app/input` and generate corresponding `.json` outline files in `/app/output`.

---

## 📦 Dependencies

```
Python 3.10+
PyMuPDF==1.23.7
langdetect==1.0.9
```

These are automatically installed inside the Docker container.

---

## 🔍 Approach Summary

- **Text Extraction**: Uses `PyMuPDF` to extract rich text and layout data.
- **Unicode-Aware Parsing**: Handles global languages via `unicodedata`.
- **Heading Detection**: Uses font size clustering to classify headings (H1–H3).
- **Language Detection**: Extracts dominant document language using `langdetect`.
- **Output**: Produces a structured JSON file for each input PDF.

---

## 👨‍💻 Author

Developed by hack_coders for Adobe India Hackathon 2025  
Engineering Student | AI & Document Intelligence Enthusiast
