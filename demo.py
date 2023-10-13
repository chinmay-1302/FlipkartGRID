import math
import numpy as np
import cv2
import ultralytics
from ultralytics import YOLO
from roboflow import Roboflow

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# rf = Roboflow(api_key="IVSHuHgHQgB8LzgQaid4")
# project = rf.workspace().project("box-object-detection")
# model = project.version(2).model

# # infer on a local image
# print(model.predict("box-pile.jpg", confidence=80, overlap=30).json())

# rf = Roboflow(api_key="IVSHuHgHQgB8LzgQaid4")
# project = rf.workspace().project("barc_det")                
# model = project.version(3).model

# # infer on a local image
# print(model.predict("qr-test.jpg", confidence=80, overlap=30).json())