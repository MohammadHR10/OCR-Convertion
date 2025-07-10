# config.py

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

PDF_PATH = os.path.join(OUTPUT_DIR, 'pdf')
IMAGE_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'images')
TEXT_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'text')

DPI = 150  
IMAGE_FORMAT = 'jpeg'  # 'jpeg' is smaller than 'png'
TESSERACT_LANG = 'eng'
TESSERACT_PSM = 3  # Fully automatic page segmentation
