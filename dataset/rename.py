# simple script to prepare image names/formats for training
import os
from PIL import Image
import numpy

# loop through images in raw, skip masks
rawdir = "./raw/"
annotdir = "./annotations/"
imagedir = "./images/"
for filename in os.listdir(rawdir):
	if "_mask.png" in filename:
		continue
	# Copy input image to images folder convert to png
	im = Image.open(os.path.join(rawdir, filename))
	filename = filename.replace(".jpg", ".png")
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

	im2.save(os.path.join(annotdir, filename))
