import numpy as np
from scipy import misc
import requests
from io import BytesIO
##import urllib.request
##import cv2 as cv

def fetch_img(url):
    
    try:
        res = requests.get(url)
        img = misc.imread(BytesIO(res.content))
##        urllib.request.urlretrieve(data[0],'test/temp.jpg')
##        temp=cv.imread('test/temp.jpg')
        return img
    except Exception as e:
        pass

def main():
    url='https://www.thefamouspeople.com/profiles/images/nikola-tesla-3.jpg'
    img=fetch_img(url)
    print(img.shape)

if __name__ == '__main__':
    main()

