# C:\Program Files\Tesseract-OCR
import cv2
import pytesseract

image = cv2.imread('.\images\print_vaga.png')

tesseractPath = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = tesseractPath + r"\tesseract.exe"

text = pytesseract.image_to_string(image)

print(text)