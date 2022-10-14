
import cv2 as cv
import numpy as np

# unit8 is the datatype of an image

blank = np.zeros((1000,1000,3), dtype='uint8')
img = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)


#1. Paint the image a certain color
# blank[200:450, 200:650] = 0,255,0
# cv.imshow('image', blank)


cv.rectangle(blank, (0,0),(250,250),(0,250,0), thickness=3)

#This can also be done as

cv.rectangle(img, (0,0), (img.shape[1]//2, img.shape[1]//2), (0,255,0), thickness = -1)
cv.imshow('rectangle', blank)
cv.imshow('rectangle2', img)

# draw a circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[1]//2), 40, (0,0,255), thickness=-1)
cv.imshow('circle', blank)

cv.waitKey(0)