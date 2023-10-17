import math
import numpy as np
import cv2
import cvzone
import ultralytics
from ultralytics import YOLO
from roboflow import Roboflow

cap = cv2.VideoCapture(1)
cap.set(3, 1280)  # 3 = width
cap.set(4, 720)  # 4 = height

rf_box = Roboflow(api_key="IVSHuHgHQgB8LzgQaid4")
project_box = rf_box.workspace().project("box-object-detection")
model_box = project_box.version(2).model

rf_barcode = Roboflow(api_key="IVSHuHgHQgB8LzgQaid4")
project_barcode = rf_barcode.workspace().project("barc_det")                
model_barcode = project_barcode.version(3).model

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    # loop for box detection
    print(model_box.predict(frame, confidence=50, overlap=30).json())
    
    # loop for barcode detection
    # print(model_barcode.predict(frame, confidence=80, overlap=30).json())

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()