import numpy as np
import cv2 as cv
import glob

np_imgs = np.zeros((907,75,75,3),dtype=np.uint8)
count=0

for file in glob.glob('flickr_img\pro\*.jpg'):
##for file in glob.glob('test\*.jpg'):
    img = cv.imread(file)
    np_imgs[count]=(img)
    count += 1

np.save('img_data.npy',np_imgs)

