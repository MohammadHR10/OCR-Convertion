# 🧠 OCR PDF Conversion Pipeline

A modular Python pipeline for converting scanned PDFs into searchable, structured `.txt` files using Tesseract OCR. Ideal for extracting large volumes of text from legal, academic, or archival documents.

---

## 📦 Features

- **PDF to Images**: Converts each PDF page to high-resolution PNGs
- **Image Preprocessing**: (Optional) Enhances images for better OCR accuracy
- **OCR Processing**: Extracts text from images using Tesseract
- **Structured Output**: Saves each page's text as a separate `.txt` file

---

## 📁 Project Structure

```
OCR-Convertion/
├── ocr_pipeline_project/
│   ├── config.py
│   ├── main.py
│   ├── utils/
│   │   ├── pdf_to_images.py
│   │   ├── image_processing.py
│   │   ├── ocr_engine.py
│   │   └── file_io.py
│   └── output/
│       ├── pdf/      # Original PDFs
│       ├── images/   # Converted images from PDF
│       └── text/     # Final OCR output as .txt files
├── requirements.txt
└── README.md
```

---

## 🛠️ Requirements

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- See `requirements.txt` for Python dependencies

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MohammadHR10/OCR-Convertion.git
cd OCR-Convertion
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate    # Windows
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

- **macOS (Homebrew):**
  ```bash
  brew install tesseract
  ```
- **Ubuntu:**
  ```bash
  sudo apt install tesseract-ocr
  ```
- **Windows:**
  Download from [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH.

---

## 📄 Usage

1. **Place your PDF file(s) inside:**
   ```
   ocr_pipeline_project/output/pdf/
   ```
2. **Run the main script:**
   ```bash
   python ocr_pipeline_project/main.py
   ```
3. **Find output text files in:**
   ```
   ocr_pipeline_project/output/text/
   ```

---

## 🧹 (Optional) Zip the Results

To bundle all `.txt` files into a zip archive:

```bash
cd ocr_pipeline_project/output/text
zip -r extracted_texts.zip ./*.txt
```

---

## 📄 License

This project is licensed under the MIT License.
