import cv2
import numpy as np


img = cv2.imread('Resources/hole.jpg')
width,height = 1627,1279

pts1 = np.float32([[100,100],[width-100,100],[100,height-200],[width-100,height-100]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("original",img)
cv2.imshow("output",imgOutput)

cv2.waitKey(0)