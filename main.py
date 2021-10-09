from PIL import Image
from pytesseract import *

test_img = "33.png"
image=Image.open(test_img)
text = image_to_string(image,lang="kor")

with open("sample.txt","w") as f:
    f.write(text)
