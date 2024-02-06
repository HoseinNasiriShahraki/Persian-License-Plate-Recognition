import cv2
from cv2 import filter2D
import numpy as np

img = cv2.imread('runs/detect/predict/crops/plate/image0.jpg')
(h, w) = img.shape[:2]
image_size = h*w
max = image_size / 2
mser = cv2.MSER_create()
mser.setMaxArea(int(image_size/10))
mser.setMinArea(50)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting to GrayScale
_, bw = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

regions, rects = mser.detectRegions(bw)

# With the rects you can e.g. crop the letters
for (x, y, w, h) in rects:
    cv2.rectangle(img, (x-2, y-2), (x+w+5, y+h+5), color=(255, 0, 255), thickness=1)
cv2.imshow("Image", img)
cv2.waitKey(0)