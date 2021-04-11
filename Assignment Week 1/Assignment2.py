# for opening webcam using opencv only
import cv2

VideoIn = cv2.VideoCapture(0)

while (1):
    _, frame = VideoIn.read()
    cv2.imshow('frame' , frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
