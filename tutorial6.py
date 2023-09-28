import numpy as np
import cv2

img = cv2.imread('F:/Learning Coding/OpenCV_tutorial/OpenCV-tutorial-practices/Chess_Board.png')
img = cv2.resize(img, (0,0), fx=0.35, fy=0.35)
#corner detection works on gray scale images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# (img, Number of corners found, quality of corners found, minimum distance between corners)
corners = np.int0(corners) # type: ignore

for corner in corners:
    x, y = corner.ravel() # type: ignore
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)
        
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
