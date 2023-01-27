import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read Image
image = cv2.imread('lock3.jpg')

# Lock 1 = 110 -> 45
# Lock 2 = 99 -> 25 
# Lock 3 = 88 -> 15

# Bilateral Filter and Greyscale
blurred = cv2.bilateralFilter(image,100,75,75)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

m = 30/22
a = 88
b = 15
average = gray.mean(axis=0).mean(axis=0)
estimatedthresh = m * (average-a) + b
#plt.hist(gray.ravel(),256,[0,256]); plt.show()

# Binary Threshold
(T, threshInv) = cv2.threshold(gray, estimatedthresh, 255,
    cv2.THRESH_BINARY_INV)

cv2.imshow("Blurred Greyscale", gray)
cv2.imshow("Threshold", threshInv)

cv2.waitKey(0)
print(average)