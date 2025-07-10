# utils/ocr_engine.py

import pytesseract
from PIL import Image
from config import TESSERACT_LANG, TESSERACT_PSM

def run_ocr_on_image(image_path):
    custom_config = f'--psm {TESSERACT_PSM}'
    image = Image.open(image_path)
    return pytesseract.image_to_string(image, lang=TESSERACT_LANG, config=custom_config)
