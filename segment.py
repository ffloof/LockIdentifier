from keras_segmentation.models.unet import mobilenet_unet

model = mobilenet_unet(n_classes=2 ,  input_height=224, input_width=224)

model.summary()

model.train(
	train_images =  "./dataset/images/",
	train_annotations = "./dataset/annotations/",
	epochs=5,
	checkpoints_path = "./checkpoints/test",
)

#out = model.predict_segmentation(
#	inp="dataset1/images_prepped_test/0016E5_07965.png",
#	out_fname="./tmp/out.png"
#) 
#import matplotlib.pyplot as plt
#plt.imshow(out)

