import cv2
import numpy as np
from HandTrack import handDetector

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detector = handDetector(detectionCon=0.85)   # Add this line

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)

    cv2.imshow("Test", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
