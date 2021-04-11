import cv2
import numpy as np


inputpic = cv2.imread('inputpic')
graypic = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

filtered = cv2.bilateralFilter(graypic,11,150,150)

new = cv2.adaptiveThreshold(filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)
new = cv2.cvtColor(new, cv2.COLOR_GRAY2BGR)

draw = cv2.bitwise_and(inputpic, new)
cv2.imshow('drawing', draw)
