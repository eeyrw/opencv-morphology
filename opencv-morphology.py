import cv2
import numpy as np

rawImage = cv2.imread('yuan.png',0)
kernel = np.ones((15,15),np.uint8)
erosionImage = cv2.erode(rawImage,kernel,iterations = 1)
dilationImage = cv2.dilate(rawImage,kernel,iterations = 1)
openOperateImage=cv2.dilate(erosionImage,kernel,iterations = 1)
closeOperateImage=cv2.erode(dilationImage,kernel,iterations = 1)
cv2.imshow('Raw Image',rawImage)
cv2.imshow('Erosion',erosionImage)
cv2.imshow('Dilation',dilationImage)
cv2.imshow('Open Operation',openOperateImage)
cv2.imshow('Close Operation',closeOperateImage)
cv2.waitKey(0)