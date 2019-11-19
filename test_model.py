import tflearn
from alexnet_small import alexnet
import cv2 as cv
import numpy as np

X = np.zeros((1,150,150,3),dtype=np.uint8)

X[0]=cv.imread('test//test0.jpg')

print(X)
network=alexnet()

model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                    max_checkpoints=1, tensorboard_verbose=2,tensorboard_dir='log')

model.load('model_alexnet-400')

prediction = model.predict(X)

print('prediction:',prediction)
