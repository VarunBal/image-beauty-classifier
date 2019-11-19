import tflearn
from tdg.alexnet.alexnet_small import alexnet
import cv2 as cv
import numpy as np

network=alexnet()

model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                    max_checkpoints=1, tensorboard_verbose=2,tensorboard_dir='log')

model.load('models//model_alexnet-400', weights_only=True)

def predict(img):
    X = np.zeros((1,150,150,3),dtype=np.uint8)
    
    img = cv.resize(img,(150,150))
    
    X[0] = img

    prediction = model.predict_label(X)

    return prediction

