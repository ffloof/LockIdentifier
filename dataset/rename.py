# simple script to prepare image names/formats for training
import os
from PIL import Image
import cv2
import numpy as np

# iterate over images convert jpg to png
# god help me the day someone uses .jpeg
directory1 = "./images/"
for filename in os.listdir(directory1):
	f = os.path.join(directory1, filename)
	if os.path.isfile(f):
		if ".jpg" in f: 
			im = Image.open(f)
			im.save(f.replace(".jpg",".png"))
			os.remove(f)

directory2 = "./annotations/"
# iterate over annotations and removes extraneous text
for filename in os.listdir(directory2):
	f = os.path.join(directory2, filename)
	if os.path.isfile(f):
		g = f.replace("_watershed_mask","")
		if "_watershed_mask" in f:
			os.rename(f,g)
		img = cv2.imread(g, cv2.IMREAD_GRAYSCALE)
		ret,th1 = cv2.threshold(img,0,255,cv2.THRESH_TRUNC)
		cv2.imwrite(g,th1)