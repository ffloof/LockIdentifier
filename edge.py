import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read Image
image = cv2.imread('lock11.png')

# Lock 1 = 110 -> 45
# Lock 2 = 99 -> 25
# Lock 3 = 88 -> 15
# Lock 4 = -> 39
# Lock 5 = -> 39 (kinda ez)
# Lock 6 = -> 40
# Lock 7 = -> 40 (kinda ez)
# Lock 8 = -> 100 (60 - 100 all work just slightly better at higher vals)


# Bilateral Filter and Greyscale
blurred = cv2.bilateralFilter(image,100,75,75)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)


#plt.hist(gray.ravel(),256,[0,256]); plt.show()

# Binary Threshold
(T, threshInv) = cv2.threshold(gray, 40, 255,
    cv2.THRESH_BINARY_INV)

cv2.imshow("Blurred Greyscale", gray)
cv2.imshow("Threshold", threshInv)

cv2.waitKey(0)
