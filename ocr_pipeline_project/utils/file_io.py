# utils/file_io.py

import os

def save_text_output(text, output_dir, base_pdf_name, page_number):
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(base_pdf_name)[0]
    file_path = os.path.join(output_dir, f"{base_name}_page_{page_number}.txt")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

def clean_temp_image(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)
