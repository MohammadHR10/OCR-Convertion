# main.py

from utils.pdf_to_images import convert_pdf_to_images
from utils.ocr_engine import run_ocr_on_image
from utils.file_io import save_text_output, clean_temp_image
from config import PDF_PATH, IMAGE_OUTPUT_DIR, TEXT_OUTPUT_DIR
import os

def main():
    print("[INFO] Starting OCR pipeline...")

    for filename in os.listdir(PDF_PATH):
        if filename.endswith('.pdf'):
            pdf_file = os.path.join(PDF_PATH, filename)
            print(f"[INFO] Processing {filename}...")

            image_paths = convert_pdf_to_images(pdf_file, IMAGE_OUTPUT_DIR)
            print(f"[INFO] {len(image_paths)} pages extracted from PDF.")

            for i, image_path in enumerate(image_paths):
                print(f"[OCR] Page {i+1}/{len(image_paths)}")
                text = run_ocr_on_image(image_path)
                save_text_output(text, TEXT_OUTPUT_DIR, filename, page_number=i+1)
                clean_temp_image(image_path)  # save space

    print("[DONE] All PDFs processed.")

if __name__ == "__main__":
    main()
