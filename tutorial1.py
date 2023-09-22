import numpy as np 
import cv2
img=cv2.imread("F:/python/OpenCV_tutorial/logo.jpg",cv2.IMREAD_UNCHANGED)
img=cv2.resize(img,(0,0),fx=0.25, fy=0.25) #img=cv2.resize(img,(400,400))
#img=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) #img=cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()