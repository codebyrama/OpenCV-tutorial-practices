import cv2
import random
img=cv2.imread("F:\Learning Coding\OpenCV_tutorial\OpenCV-tutorial-practices\logo.jpg",-1)
print(img)
print(type(img))
print(img.shape) #rows,collumn, channel, 3 values representing the value
for i in range(100):
    for j in range(100):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
tag=img[320:860,10:1885]
img[0:540,10:1885]=tag
img[540:1080,10:1885]=tag
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()