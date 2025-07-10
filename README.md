# 🧠 OCR PDF Conversion Pipeline

This project provides a modular OCR (Optical Character Recognition) pipeline using Python and Tesseract OCR to convert scanned PDFs into searchable and structured `.txt` files. It’s especially useful for extracting large volumes of text from legal, academic, or archival documents.

---

## 📁 Project Structure

OCR-Convertion/
├── ocr_pipeline_project/
│ ├── config.py
│ ├── main.py
│ ├── utils/
│ │ ├── pdf_to_images.py
│ │ ├── image_processing.py
│ │ ├── ocr_engine.py
│ │ └── file_io.py
│ └── output/
│ ├── pdf/ # Original PDFs
│ ├── images/ # Converted images from PDF
│ └── text/ # Final OCR output as .txt files
├── requirements.txt
└── README.md

---

## 🚀 How It Works

1. **PDF to Images**: Converts every page of a PDF into high-resolution PNG images using `pdf2image`.
2. **Image Preprocessing** _(optional)_: Enhances image quality for better OCR accuracy (e.g., grayscale, thresholding).
3. **OCR Processing**: Uses Tesseract to extract text from each image.
4. **File Output**: Saves the output of each page as a separate `.txt` file under `output/text/`.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MohammadHR10/OCR-Convertion.git
cd OCR-Convertion

### 2. Create and Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Install Tesseract

Make sure Tesseract OCR is installed and accessible in your system path.

macOS (Homebrew):
brew install tesseract

Ubuntu:
sudo apt install tesseract-ocr

### 📦 Running the Pipeline
### 1. Place your PDF file(s) inside:

ocr_pipeline_project/output/pdf/

### 2. Run the main script:

python ocr_pipeline_project/main.py

All output text files will be saved to:

ocr_pipeline_project/output/text/

### 🧹 Zipping the Results (Optional)
To bundle all .txt files into a .zip:

cd ocr_pipeline_project/output/text
zip -r extracted_texts.zip ./*.txt

### 📄 License
This project is licensed under the MIT License.
```
