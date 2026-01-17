import cv2
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # 找到轮廓,参数：(img,轮廓检索模式/怎么找，轮廓近似方法/怎么存)
    for cnt in contours:
        area = cv2.contourArea(cnt) # area 轮廓的像素面积，单位：像素的平方
        print(area)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),5)
            peri = cv2.arcLength(cnt,True) # peri 轮廓周长perimeter，像素长度
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)  # 从原始轮廓cnt中提取特征轮廓点集，用更少的点，近似表示原轮廓（允许的最大误差 = 周长的 2%）
            objCor = len(approx) # len(approx): 轮廓点数（3：三角形，4：方形，大于4：圆）
            x, y, w, h = cv2.boundingRect(approx) # x,y: 包围该轮廓的最小外接矩形左上角坐标（像素坐标）/ w, h：该矩形的宽和高（像素）
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2) # 画出包围框

            if objCor == 3: objType = "Triangle"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio> 0.95 and aspRatio < 1.05: objType = "Square"
                else: objType = "Rectangle"
            elif objCor > 4 : objType = "Circle"
            else: objType = "None"

            cv2.putText(imgContour,objType,
                        (x+w//2,y+h//2),cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,(0,0,0),1)


path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlack = np.zeros_like(img)

getContours(imgCanny)

imgStack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlack]))

cv2.imshow("imgStack",imgStack)
cv2.waitKey(0)
cv2.destroyAllWindows()