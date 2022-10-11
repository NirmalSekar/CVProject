from cgitb import grey
import cv2 as cv
import numpy as np



blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

# blank[200:400, 200:400] = 0,0,255
# cv.imshow('Green',blank)
# cv.rectangle(blank,(0,0), (100,100),(0,255,0),thickness=2)
# cv.imshow('rectangle', blank)

cv.circle(blank,(0,100),(250,250),5, (0,255,0),2)
cv.waitKey(0)
