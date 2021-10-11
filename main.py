from PIL import Image
from pytesseract import *
import cv2
from pytesseract import Output
import  matplotlib.pyplot as plt
from skimage.transform import resize


pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
config = ('-l kor+eng --oem 3 --psm 6')


img=cv2.imread("test.PNG")
#img=resize(img,(1000,1000))

#print(pytesseract.image_to_string("test.png",config=config))

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())