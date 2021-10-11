from PIL import Image
from pytesseract import *
import cv2
from pytesseract import Output
import  matplotlib.pyplot as plt
from skimage.transform import resize

import pyautogui

pyautogui.screenshot('test.png')
#1.  pyautogui를 이용하여 프로그램을 시작하고 클릭을 하면 그 위치를 기반으로 글자 인식
#2. 알맞은 크기의 박스를 생성하여 배치하면 그곳에 있는(세부설정으로 닉네임 나오는 구간을 설정)텍스트만 인식




pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
config = ('-l kor+eng --oem 3 --psm 11')


img=cv2.imread("test.PNG")
print(pytesseract.image_to_string("test.png",config=config))

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())