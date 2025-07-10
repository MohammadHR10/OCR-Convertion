# utils/pdf_to_images.py

from pdf2image import convert_from_path
import os
from config import DPI, IMAGE_FORMAT

def convert_pdf_to_images(pdf_path, output_dir):
    if os.path.isfile(output_dir):
        os.remove(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    images = convert_from_path(pdf_path, dpi=DPI, fmt=IMAGE_FORMAT)
    image_paths = []

    for i, img in enumerate(images):
        print(f"[IMG] Saving page {i+1} to image...")
        img_path = os.path.join(output_dir, f"page_{i + 1}.{IMAGE_FORMAT}")
        img.save(img_path, IMAGE_FORMAT.upper())
        image_paths.append(img_path)

    return image_paths
