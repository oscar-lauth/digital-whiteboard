# raspb pi + cam gets img

# format of either RBGArray or other PIL? or pure IMG (jpg)

# python code to clean and parse

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Oscar\AppData\Local\Programs\Tesseract-OCR/tesseract.exe'


raw_img = Image.open("test2.jpg")
roi_img=raw_img
# raw_img.show()
# w, h = raw_img.size
# print(w,h)
# roi_img = raw_img.crop((1370,1100,2600,2300))
# roi_img.show()

print(pytesseract.image_to_data(roi_img))
# print(pytesseract.image_to_pdf_or_hocr(roi_img))
print(pytesseract.image_to_string(roi_img))

