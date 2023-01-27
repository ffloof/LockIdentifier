import cv2
import numpy as np
from matplotlib import pyplot as plt

def process_image(name, threshold, debug):
    # Read Image
    image = cv2.imread("./inputs/"+name)

    # Bilateral Filter then Greyscale
    blurred = cv2.bilateralFilter(image,100,75,75)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    # Binary Threshold
    (T, thresholded_image) = cv2.threshold(gray, threshold, 255,
        cv2.THRESH_BINARY)

    if debug:
        plt.hist(gray.ravel(),256,[0,256]); plt.show()
        cv2.imshow("Blurred Greyscale", gray)
        cv2.imshow("Threshold", thresholded_image)
        cv2.waitKey(0)
    else:
        cv2.imwrite("./outputs/"+name, thresholded_image)



# Lock 1 = 110 -> 45
# Lock 2 = 99 -> 25
# Lock 3 = 88 -> 15
# Lock 4 = -> 39
# Lock 5 = -> 39 (kinda ez)
# Lock 6 = -> 40
# Lock 7 = -> 40 (kinda ez)
# Lock 8 = -> 100 (60 - 100 all work just slightly better at higher vals)

data = {
    "lock1.jpg":45, 
    "lock2.jpg":25,
    "lock3.jpg":15,
    "lock4.jpg":39,
    "lock5.jpg":39, #ez
    "lock6.jpg":40,
    "lock7.jpg":40, #ez
    "lock8.jpg":100,
    "lock9.jpg":40, #Dont know what to do for this one
    "lock10.jpg":40, 
}

for name in data:
    process_image(name, data[name], False)
