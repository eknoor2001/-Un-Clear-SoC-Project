#importing libraries
import numpy as np 
import cv2

original= cv2.imread("inputpic.jpeg")

#resizing image
original = cv2.resize(original , (300 , 300))

#converting to gray colorspace
grayimg = cv2.cvtColor(original , cv2.COLOR_BGR2GRAY)
rows, cols  = grayimg.shape


#translations
M = np.float32([[1,0,10],[0,1,10]])
dst = cv2.warpAffine(grayimg,M,(cols,rows))
cv2.imshow('img',dst)

M = np.float32([[1,0,0],[0,1,10]])
dst = cv2.warpAffine(grayimg,M,(cols,rows))
cv2.imshow('img',dst)

M = np.float32([[1,0,10],[0,1,0]])
dst = cv2.warpAffine(grayimg,M,(cols,rows))
cv2.imshow('img',dst)

M = np.float32([[1,0,20],[0,1,20]])
dst = cv2.warpAffine(grayimg,M,(cols,rows))
cv2.imshow('img',dst)`

#rotations
M = cv2.getRotationMatrix2D((cols/2,rows/2),10,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)

M = cv2.getRotationMatrix2D((cols/2,rows/2),-10,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)

M = cv2.getRotationMatrix2D((cols/2,rows/2),20,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)

M = cv2.getRotationMatrix2D((cols/2,rows/2),15,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)

#blur
blur = cv2.blur(image , (5,5))
cv2.imshow("blur1",blur)

#gaussianblur
gblur = cv2.GaussianBlur(image,(11,11) , 0)
cv2.imshow("gblur",gblur)


