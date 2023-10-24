import math
import time
import numpy as np
import cv2
import cvzone
import ultralytics
from ultralytics import YOLO
from roboflow import Roboflow
import torch
import serial

SerialObj = serial.Serial('COM8') # COMxx  format on Windows
SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8   # Number of data bits = 8
SerialObj.parity  ='N'   # No parity
SerialObj.stopbits = 1   # Number of Stop bits = 1
time.sleep(3)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # 3 = width
cap.set(4, 720)  # 4 = height
# cap.set(3, 600)  # 3 = width
# cap.set(4, 400)  # 4 = height
# cv2.CAP_DSHOW
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print(width, height)

# rf_box = Roboflow(api_key="cIMps5GQKQXOUmHb153T")
# project_box = rf_box.workspace().project("box-object-detection")
# model_box = project_box.version(2).model

model_box = YOLO('BDM\\best.pt')
classNames = ['box']

# model_barcode = YOLO('BDSM\\best.pt')
# classNames = ['0']

# variables for box photo & barcode photo
box_capture = True
barcode_capture = True

while True:
    success, img = cap.read()
    img = img[00:400,00:600]
    # img = cv2.resize(img, (600, 400))
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
                # SerialObj.write(x_robot) #transmit 'A' (8bit) to micro/Arduino
                SerialObj.write(str(x_robot).encode())
                print(str(x_robot).encode())
                res = SerialObj.readline()
                print(res)
                time.sleep(10)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
SerialObj.close() # Close the port