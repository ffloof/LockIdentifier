import cv2
import numpy as np

# read image as grayscale
image = cv2.imread('lock.png')

blurred = cv2.bilateralFilter(image,25,55,55)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

#(T, threshInv) = cv2.threshold(gray, 60, 255,
#    cv2.THRESH_BINARY_INV)

th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV,11,2)
th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY_INV,11,2)

cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)
cv2.imshow("Threshold Mean", th2)
cv2.imshow("Threshold Gaussian", th3)

cv2.waitKey(0)