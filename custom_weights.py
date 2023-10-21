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
# cap.set(3, 1280)  # 3 = width
# cap.set(4, 720)  # 4 = height
cap.set(3, 600)  # 3 = width
cap.set(4, 400)  # 4 = height

# rf_box = Roboflow(api_key="cIMps5GQKQXOUmHb153T")
# project_box = rf_box.workspace().project("box-object-detection")
# model_box = project_box.version(2).model

model_box = YOLO('BDM\\best.pt')
classNames = ['box']

# variables for box photo & barcode photo
box_capture = True
barcode_capture = True

while True:
    success, img = cap.read()
    results = model_box(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)
            # if (conf >= 0.7):
            #     cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # above is for normal rectangle below is for rounded rectangle

            # x1, y1, x2, y2 = box.xyxy[0]
            # w, h = x2-x1, y2-y1
            # bbox= int(x1), int(y1), int(w), int(h)
            # cvzone.cornerRect(img, (x1, y1, w, h))

            # Confidence level
            conf = math.ceil((box.conf[0] * 100)) / 100
            print(conf)

            # Class Name
            cls = int(box.cls[0])
            print(cls)

            # Printing Confidence and Class Name
            if(conf >= 0.5):
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(0, y1)), scale=0.5, thickness=1)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()