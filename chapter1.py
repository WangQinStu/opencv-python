import cv2

#可视化摄像头
cap = cv2.VideoCapture(0) #将视频路径更换为摄像头id即可
# 设置尺寸
cap.set(3, 640)
cap.set(4, 480)
# 设置亮度
cap.set(10, 10)
while True:
    ret, frame = cap.read()
    cv2.imshow("VIDEO",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
