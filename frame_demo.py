import math
import time
import numpy as np
import cv2
import cvzone
import ultralytics
from ultralytics import YOLO
from roboflow import Roboflow
import torch

cap = cv2.VideoCapture(1)
cap.set(3, 1280)  # 3 = width
cap.set(4, 720)  # 4 = height

rf_box = Roboflow(api_key="cIMps5GQKQXOUmHb153T")
project_box = rf_box.workspace().project("box-object-detection")
model_box = project_box.version(2).model

# variables for box photo & barcode photo
box_capture = True
barcode_capture = True

while True:
    # time.sleep(10)
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    # loop for box detection
    print(model_box.predict(frame, confidence=25, overlap=30).json())
    # box_predict = model_box.predict(frame, confidence=50, overlap=30).json()['predictions'][0]["x"]
    if model_box.predict(frame, confidence=25, overlap=30).json()['predictions'] != [] :
        box_predict = model_box.predict(frame, confidence=25, overlap=30).json()['predictions'][0]
        x_coord = int(box_predict['x'])
        y_coord = int(box_predict['y'])
        width = int(box_predict['width'])
        height = int(box_predict['height'])
        conf = float(box_predict['confidence'])
        class_name = box_predict['class']
        print("\n")
        print(box_predict)

        # time.sleep(10)
        # code for rectangle
        start_point = (int(x_coord - (width/2)), int(y_coord-(height/2)))
        end_point = (int(x_coord + (width/2)), int(y_coord + (height/2)))
        color = (255,255,0)
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()