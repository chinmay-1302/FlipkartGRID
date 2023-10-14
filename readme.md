## Flipkart GRID 5.0 - Robotics Challenge
This repo is to maintain the DL models & python application of our team for the Flipkart GRID 5.0 - Robotics Challenge

### 💻 Tech Stack
- OpenCV
- YOLOv8
- Roboflow

### 🧠 Models
- Box Detection Model
- Barcode Detection Model

### ⚙️ Working
1. Box Cart is placed below camera
2. Python application Begins
3. OpenCV takes snapshot of trolley
4. Trolley snapshot is passed to Box Detection Model (BDM)
5. BDM checks if cart contains any boxes
    i. If False, go to step 16
    ii. If True, continue
6. BDM identifies the "Best Box", the box with the highest confidence level out of all the boxes in the trolley
7. BDM sends the XY coordinates of the "Best Box" to Arduino
8. Wait till the robot lifts the "Best Box" and sends a response back to python application using Arduino
9. When response is received, OpenCV takes snapshot of the lifted "Best Box"
10. Box snapshot is passed to Barcode Detection Model (BDSM)
11. BDSM detects if the upper side of the box contains the barcode or not and stores the result as True or False
12. If False, then
    i. BDSM sends a signal to Arduino for rotating the box
    ii. Wait till the robot rotates the box and sends a response back to python application using Arduino
    iii. When response is received, OpenCV takes snapshot of the new upper side of box
    iv. Go to step 10
13. If True, then BDSM sends a True signal to Arduino for placing the Box on conveyer belt
14. Wait till the robot places the "Best Box" on conveyer belt and sends a response back to python application using Arduino
15. Go to step 3
16. End application

### 📚 References
- [Train Custom Model from scratch on Roboflow](https://docs.roboflow.com/train/train/train-from-scratch)
- [YOLOv8 Object Detection on a Custom Dataset](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/)
- [Box Detection Model - Roboflow](https://universe.roboflow.com/university-of-heidelberg/box-object-detection)
- [Barcode Detection Model - Roboflow](https://universe.roboflow.com/uniqueidwarehouse-xcp0o/barc_det)