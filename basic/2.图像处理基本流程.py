import cv2
import numpy as np

img = cv2.imread("Resources/hole_rod.png")

kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #转为灰度图
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0) #高斯模糊
imgCanny = cv2.Canny(imgBlur,150,200) # Canny边缘检测
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) # 形态学闭运算-边缘膨胀（连接断裂的边缘 / 缝隙）
imgEroded = cv2.erode(imgDilation,kernel,iterations=1) # 形态学闭运算-边缘腐蚀（把形状收回，避免整体变胖）

"""图片分开显示"""
# cv2.imshow("Original",img)
# cv2.imshow("imgGray",imgGray)
# cv2.imshow("imgBlur",imgBlur)
# cv2.imshow("imgCanny",imgCanny)
# cv2.imshow("imgDilation",imgDilation)
# cv2.imshow("imgEroded",imgEroded)

"""图片合并为一个显示框"""
# hstack函数需要其中的图片dimension相同，所以要先转换
def bgr(x):
    return cv2.cvtColor(x,cv2.COLOR_GRAY2BGR) if x.ndim ==2 else x
# 为每张图添加说明
def label(img,text):
    cv2.putText(img,text,(10,30), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    return img
row1 = np.hstack((
    label(img.copy(), "Original"),
    label(bgr(imgGray), "Gray"),
    label(bgr(imgBlur), "Blur"),
))
row2 = np.hstack((
    label(bgr(imgCanny), "Canny"),
    label(bgr(imgDilation), "Dilation"),
    label(bgr(imgEroded), "Eroded"),
))
cv2.imshow("img",np.vstack([row1,row2]))
cv2.waitKey(0)
