import cv2
import numpy as np

# read image as grayscale
img = cv2.imread('lock.png', cv2.IMREAD_GRAYSCALE)

# threshold to binary
thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,401,35)

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# find contours - write black over all small contours
letter = morph.copy()
cntrs = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
for c in cntrs:
    area = cv2.contourArea(c)
    if area < 100:
        cv2.drawContours(letter,[c],0,(0,0,0),-1)

# do canny edge detection
edges = cv2.Canny(letter, 200, 200)

# show results
cv2.imshow("Threshold", thresh)
cv2.imshow("Morphology", morph)
#cv2.imshow("???", letter)
#cv2.imshow("CannyEdge", edges)
cv2.waitKey(0)