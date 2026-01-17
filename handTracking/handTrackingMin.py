import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)

mpHands = mp.
hands = mpHands.Hands()

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break