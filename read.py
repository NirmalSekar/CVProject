import cv2 as cv

img = cv.imread('test.jpg')

cv.imshow('testing_image', img)

cv.waitKey(0)