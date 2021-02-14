import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_boxes(img))
# X, y, w,h

cv2.imshow('img', img)
cv2.waitKey(0)
