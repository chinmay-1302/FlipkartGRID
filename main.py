import math
import numpy as np
import cv2
import cvzone
from ultralytics import YOLO
import torch

cap = cv2.VideoCapture(1)
cap.set(3, 1280)  # 3 = width
cap.set(4, 720)  # 4 = height

model_box = YOLO('BDM\\best.pt')
classNames = ['box']

# model_barcode = YOLO('BCDM\\best.pt')
# classNames = ['0']

# variables for box photo & barcode photo
box_capture = True
barcode_capture = True

while True:
    success, img = cap.read()
    img = img[00:400,00:600]
    results = model_box(img, stream=True)
    # results = model_barcode(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)

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
                # calculations for sending stuff to robot
                # for sending center point to robot
                x_center = int((x1+x2)/2)
                y_center = int((y1+y2)/2)
                image = cv2.circle(img, (x_center,y_center), radius=0, color=(255, 0, 0), thickness=8)

                x_robot = int(300 - x_center)
                y_robot = int(400 - y_center)
            # break

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()