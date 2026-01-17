######################## READ IMAGE ############################
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/lena.png")
# # DISPLAY
# cv2.imshow("Lena Soderberg",img)
# cv2.waitKey(0)

######################### READ VIDEO #############################
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/test_ video.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

######################### READ WEBCAM  ############################
import cv2
#可视化摄像头
cap = cv2.VideoCapture(0) #将视频路径更换为摄像头id即可
# 设置尺寸
frameWidth = 480
frameHeight = 240
cap.set(3, frameWidth)
cap.set(4, frameHeight)
# 设置亮度
cap.set(10, 10)
while True:
    ret, frame = cap.read()
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
