# import math
# import time
# import numpy as np
# import cv2
# import cvzone
# import ultralytics
# from ultralytics import YOLO
# from roboflow import Roboflow
# import torch

# cap = cv2.VideoCapture(1)
# # cap.set(3, 1280)  # 3 = width
# # cap.set(4, 720)  # 4 = height
# cap.set(3, 600)  # 3 = width
# cap.set(4, 400)  # 4 = height

# rf_box = Roboflow(api_key="cIMps5GQKQXOUmHb153T")
# project_box = rf_box.workspace().project("box-object-detection")
# model_box = project_box.version(2).model

# # variables for box photo & barcode photo
# box_capture = True
# barcode_capture = True

# while True:
#     # time.sleep(10)
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     # loop for box detection
#     print(model_box.predict(frame, confidence=25, overlap=30).json())
#     # box_predict = model_box.predict(frame, confidence=50, overlap=30).json()['predictions'][0]["x"]
#     if model_box.predict(frame, confidence=25, overlap=30).json()['predictions'] != [] :
#         box_predict = model_box.predict(frame, confidence=25, overlap=30).json()['predictions'][0]
#         x_coord = int(box_predict['x'])
#         y_coord = int(box_predict['y'])
#         width = int(box_predict['width'])
#         height = int(box_predict['height'])
#         conf = float(box_predict['confidence'])
#         class_name = box_predict['class']
#         print("\n")
#         print(box_predict)

#         # time.sleep(10)
#         # code for rectangle
#         start_point = (int(x_coord - (width/2)), int(y_coord-(height/2)))
#         end_point = (int(x_coord + (width/2)), int(y_coord + (height/2)))
#         color = (255,255,0)
#         thickness = 2
#         frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
#         cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# Copilot Code - NMS
import math
import time
import numpy as np
import cv2
import cvzone
import ultralytics
from ultralytics import YOLO
from roboflow import Roboflow
import torch

cap = cv2.VideoCapture(0)
cap.set(3, 600)  # set width
cap.set(4, 400)  # set height

rf_box = Roboflow(api_key="cIMps5GQKQXOUmHb153T")
project_box = rf_box.workspace().project("box-object-detection")
model_box = project_box.version(2).model

# variables for box photo & barcode photo
box_capture = True
barcode_capture = True

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    # Detect boxes in the frame
    predictions = model_box.predict(frame, confidence=25, overlap=30).json()['predictions']

    # Apply non-maximum suppression to remove overlapping boxes
    if predictions:
        boxes = np.array([[box['x'], box['y'], box['x']+box['width'], box['y']+box['height'], box['confidence']] for box in predictions])
        indices = cv2.dnn.NMSBoxes(boxes[:, :4].astype(np.float32), boxes[:, 4], 0.5, 0.5)

        # Draw bounding boxes around the detected objects
        for i in indices:
            i = i[0]
            box = predictions[i]
            x_coord = int(box['x'])
            y_coord = int(box['y'])
            width = int(box['width'])
            height = int(box['height'])
            conf = float(box['confidence'])
            class_name = box['class']

            start_point = (int(x_coord - (width/2)), int(y_coord-(height/2)))
            end_point = (int(x_coord + (width/2)), int(y_coord + (height/2)))
            color = (255,255,0)
            thickness = 2
            frame = cv2.rectangle(frame, start_point, end_point, color, thickness)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Copilot Code - OpenCV's DNN module
# import cv2
# import numpy as np
# from roboflow import Roboflow

# cap = cv2.VideoCapture(1)
# cap.set(3, 600)  # set width
# cap.set(4, 400)  # set height

# rf_box = Roboflow(api_key="cIMps5GQKQXOUmHb153T")
# project_box = rf_box.workspace().project("box-object-detection")
# model_box = project_box.version(2).model

# # Load the pre-trained model using OpenCV's DNN module
# model = cv2.dnn.readNetFromDarknet(model_box.config, model_box.weights)
# model.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# model.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)

#     # Prepare the input image for the model
#     blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True, crop=False)

#     # Pass the input image through the model and get the output
#     model.setInput(blob)
#     output_layers = model.getUnconnectedOutLayersNames()
#     layer_outputs = model.forward(output_layers)

#     # Process the output to get the bounding boxes and class labels
#     boxes = []
#     confidences = []
#     class_ids = []
#     for output in layer_outputs:
#         for detection in output:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:
#                 center_x = int(detection[0] * 416)
#                 center_y = int(detection[1] * 416)
#                 width = int(detection[2] * 416)
#                 height = int(detection[3] * 416)
#                 left = int(center_x - width / 2)
#                 top = int(center_y - height / 2)
#                 boxes.append([left, top, width, height])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply non-maximum suppression to remove overlapping boxes
#     indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.5)

#     # Draw bounding boxes around the detected objects
#     for i in indices:
#         i = i[0]
#         left, top, width, height = boxes[i]
#         conf = confidences[i]
#         class_id = class_ids[i]
#         color = (255, 255, 0)
#         thickness = 2
#         cv2.rectangle(frame, (left, top), (left + width, top + height), color, thickness)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()