import cv2
import pytesseract

img = cv2.imread("dataset/img_115.png")
d = pytesseract.image_to_string(img)
print(d)