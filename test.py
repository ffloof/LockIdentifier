from keras_segmentation.predict import model_from_checkpoint_path
import matplotlib.pyplot as plt

model = model_from_checkpoint_path("./checkpoints/test")

out = model.predict_segmentation(
	inp="./dataset/1.jpg",
	out_fname="./dataset/result1.png"
)

plot.imshow(out)
