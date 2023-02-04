# raspb pi + cam gets img

# format of either RBGArray or other PIL? or pure IMG (jpg)

# python code to clean and parse

from PIL import Image
import pytesseract
import cv2
import numpy as np

from picamera import PiCamera
import picamera.array

from time import sleep



def capture_img(roi):
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    output = picamera.array.PIRGBArray(camera,size=roi)
    camera.capture(output,'rgb',resize=roi)
    # camera.close()
    return output
print(capture_img(400,400))

# def get_roi():

# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Oscar\AppData\Local\Programs\Tesseract-OCR/tesseract.exe'


# cv_raw_img = np.array(Image.open("test.jpg").convert("RGB"))[:,:,::-1].copy()
# cv2.imshow("D",cv_raw_img)
# # roi_img=raw_img
# # raw_img.show()
# # w, h = raw_img.size
# # print(w,h)
# # roi_img = raw_img.crop((1370,1100,2600,2300))
# # roi_img.show()

# roi = cv2.selectROI(cv_raw_img,showCrosshair=False)
# print(roi)

# roi_img = cv_raw_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
# cv2.imshow("ROI",roi_img)
# cv2.imwrite("roi.jpg",roi_img)

# cv2.waitKey(0)

# print(pytesseract.image_to_data(roi_img))
# # print(pytesseract.image_to_pdf_or_hocr(roi_img))
# print(pytesseract.image_to_string(roi_img))


# Write function / module solely for setting initial ROI, then don't use any CV/NUMPY/ROI tool during actually running
