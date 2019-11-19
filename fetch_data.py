import numpy as np
import to_database as db
from scipy import misc
import requests
from io import BytesIO
##import urllib.request
##import cv2 as cv

def main():
    raw_data = db.select_url()
    db.close_conn()
    imgs = np.zeros((len(raw_data),150,150,3),dtype=np.uint8)
    labels = np.zeros((len(raw_data),2),dtype=np.uint8)
    count=0

    for data in raw_data:
##        print(data)
        try:
            res = requests.get(data[0])
            temp = misc.imread(BytesIO(res.content))
    ##        urllib.request.urlretrieve(data[0],'test/temp.jpg')
    ##        temp=cv.imread('test/temp.jpg')
            imgs[count] = temp
            
            if data[1] == True:
                labels[count]=[1,0]
            elif data[1] == False:
                labels[count]=[0,1]
            
            print(count+1,'image(s) loaded out of',len(raw_data))
            count+=1
        except Exception as e:
            print(e)

    training_data = [imgs,labels]
##    print(labels)
##    print(training_data)
##    np.save('training_data.npy',training_data)
    return training_data

if __name__ == '__main__':
    main()
