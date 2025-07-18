
import os
import json
import fitz  # PyMuPDF
import unicodedata
from collections import defaultdict
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # ensure reproducibility

def is_heading_candidate(text):
    if len(text) < 2:
        return False
    letters = sum(1 for c in text if unicodedata.category(c).startswith("L"))
    return letters > 0

def detect_language(sample_texts):
    sample = " ".join(sample_texts[:20])
    try:
        return detect(sample)
    except:
        return "unknown"

def process_pdf(filepath):
    doc = fitz.open(filepath)
    headings = []
    fonts = defaultdict(int)

    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" not in b:
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    text = s["text"].strip()
                    if not is_heading_candidate(text):
                        continue
                    size = round(s["size"], 1)
                    fonts[size] += 1
                    headings.append({
                        "text": text,
                        "size": size,
                        "page": i + 1
                    })

    if not fonts:
        return json.dumps({"title": "Untitled", "outline": [], "language": "unknown"}, indent=2)

    sizes_sorted = sorted(fonts.items(), key=lambda x: (-x[0], -x[1]))
    level_map = {}
    if len(sizes_sorted) > 0:
        level_map[sizes_sorted[0][0]] = "H1"
    if len(sizes_sorted) > 1:
        level_map[sizes_sorted[1][0]] = "H2"
    if len(sizes_sorted) > 2:
        level_map[sizes_sorted[2][0]] = "H3"

    title_candidates = [h["text"] for h in headings if h["size"] == sizes_sorted[0][0] and h["page"] == 1]
    title = title_candidates[0] if title_candidates else "Untitled"

    outline = [
        {"level": level_map[h["size"]], "text": h["text"], "page": h["page"]}
        for h in headings if h["size"] in level_map
    ]

    language = detect_language([h["text"] for h in headings])

    return json.dumps({
        "title": title,
        "outline": outline,
        "language": language
    }, indent=2)

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            json_output = process_pdf(input_path)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(json_output)

if __name__ == "__main__":
    main()