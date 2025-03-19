# C:\Program Files\Tesseract-OCR
import cv2
import pytesseract

image = cv2.imread(r'.\images\print_vaga.png')

# Redimensionamento da imagem para padrão
width = image.shape[1]
height = image.shape[0]

escale = float(height/width)
resizedwidth = 1500
resizedheight = int(resizedwidth*escale)

image = cv2.resize(image, (resizedwidth, resizedheight), interpolation=cv2.INTER_AREA)

# cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

tesseractPath = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = tesseractPath + r"\tesseract.exe"

text = pytesseract.image_to_string(image, lang="por")

print(text)