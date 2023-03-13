# simple script to prepare image names/formats for training
import os
from PIL import Image
import numpy

# loop through images in raw, skip masks
rawdir = "./raw/"

i = 0
for filename in os.listdir(rawdir):
	i=i+1
	if "_mask.png" in filename:
		continue
	# Copy input image to images folder convert to png
	im = Image.open(os.path.join(rawdir, filename))
	filename = filename.replace(".jpg", ".png")
	
	# Implements a 80% train, 10% test, 10% validation
	# TODO: we should ensure that all these directories exist earlier in the script
	if i % 10 == 0:
		imagedir="./images/validation/"
		annotdir="./annotations/validation/"
	elif i % 10 == 1:
		imagedir="./images/testing/"
		annotdir="./annotations/testing/"
	else:
		imagedir="./images/training/"
		annotdir="./annotations/training/"

	im.save(os.path.join(imagedir, filename)) #TODO: figure out if results should just have index instead of original name

	# Copy the corresponding output mask to annotations folder
	maskfile = filename[:filename.rfind(".")] + "_watershed_mask.png"
	im = Image.open(os.path.join(rawdir, maskfile))
	# For some reason PixelAnnotationTool adds a border of white pixels so those are removed here
	im = im.convert("RGBA")

	data = numpy.array(im)
	red, green, blue, alpha = data.T
	white_areas = (red == 255) & (blue == 255) & (green == 255)
	data[..., :-1][white_areas.T] = (255,0,0)
	im2 = Image.fromarray(data)

	im2.save(os.path.join(annotdir, filename))
