import cv2
import numpy as np

# read image as grayscale
image = cv2.imread('lock.png')

blurred = cv2.bilateralFilter(image,25,55,55)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

(T, threshInv) = cv2.threshold(gray, 47, 255,
    cv2.THRESH_BINARY_INV)

cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)
cv2.imshow("Threshold", threshInv)

cv2.waitKey(0)