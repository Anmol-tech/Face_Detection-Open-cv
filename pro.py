import cv2
import os 

path = 'test_data/'
fi = os.listdir(path)[0]
img  = cv2.imread(path + '1.jpg')
print(img)