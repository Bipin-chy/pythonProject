import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\\Users\\chaud\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

from PIL import Image


img = Image.open('qoute.png')
output = tess.image_to_string(img)
print(output)

file = open('detectedText.txt','a+')
file.write(output)
file.close()