# simple script to prepare image names/formats for training
import os
from PIL import Image
import numpy

# loop through images in raw, skip masks
rawdir = "./raw/"

i_val = "./images/validation"
a_val = "./annotations/validation"
i_test = "./images/testing"
a_test = "./annotations/testing"
i_train = "./images/training"
a_train = "./annotations/training"

for name in [i_val, a_val, i_test, a_test, i_train, a_train]:
	if !os.path.exists(name):
		os.makedirs(name)


i = 0
for filename in os.listdir(rawdir):
	i=i+1
	if "_mask.png" in filename:
		continue

	print(filename)
	# Copy input image to images folder convert to png
	im = Image.open(os.path.join(rawdir, filename))
	filename = filename.replace(".jpg", ".png").replace(".jpeg",".png")
	
	# Implements a 80% train, 10% test, 10% validation split
	if i % 10 == 0:
		imagedir=i_val
		annotdir=a_val
	elif i % 10 == 1:
		imagedir=i_test
		annotdir=a_test
	else:
		imagedir=i_train
		annotdir=a_train

	im.save(os.path.join(imagedir, filename)) #TODO: figure out if results should just have index instead of original name

	# Copy the corresponding output mask to annotations folder
	maskfile = filename[:filename.rfind(".")] + "_color_mask.png"
	im = Image.open(os.path.join(rawdir, maskfile))
	# For some reason PixelAnnotationTool adds a border of white pixels so those are removed here
	im = im.convert("RGBA")

	data = numpy.array(im)
	red, green, blue, alpha = data.T
	white_areas = (red == 255) & (blue == 255) & (green == 255)
	data[..., :-1][white_areas.T] = (255,0,0)
	im2 = Image.fromarray(data)
	im2 = im2.convert("RGB")

	im2.save(os.path.join(annotdir, filename))

# after this runs one needs to go to /images/training testing and validation and run
# `mogrify *.png` to fix srgb errors
