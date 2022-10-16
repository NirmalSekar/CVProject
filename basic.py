import cv2 as cv

img = cv.imread('Images/test.jpg')


resized = cv.resize(img, (500,500))
cv.imshow('image', resized)

# converting the image to gray scale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# Blur the image

blurry = cv.GaussianBlur(resized,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blurry', blurry)



# canny edge detector

canny = cv.Canny(blurry, 75, 125)
cv.imshow('canny', canny)


# Dialting the image
dilated = cv.dilate(resized, (5,5),iterations=1)
cv.imshow('dilate', dilated)
 

# eroding

erode = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('erode', erode)  


# cropping 
cropped = resized[50:200, 200:400]
cv.imshow('Cropped', cropped)





cv.waitKey(0)