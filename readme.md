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
01. Box Cart is placed below camera
02. Python application Begins
03. OpenCV takes snapshot of trolley
04. Trolley snapshot is passed to Box Detection Model (BDM)
05. BDM checks if cart contains any boxes
    1. If False, go to step 16
    2. If True, continue
06. BDM identifies the "Best Box", the box with the highest confidence level out of all the boxes in the trolley
07. BDM sends the XY coordinates of the "Best Box" to Arduino
08. Wait till the robot lifts the "Best Box" and sends a response back to python application using Arduino
09. When response is received, OpenCV takes snapshot of the lifted "Best Box"
10. Box snapshot is passed to Barcode Detection Model (BDSM)
11. BDSM detects if the upper side of the box contains the barcode or not and stores the result as True or False
12. If False, then
    1. BDSM sends a signal to Arduino for rotating the box
    2. Wait till the robot rotates the box and sends a response back to python application using Arduino
    3. When response is received, OpenCV takes snapshot of the new upper side of box
    4. Go to step 10
13. If True, then BDSM sends a True signal to Arduino for placing the Box on conveyer belt
14. Wait till the robot places the "Best Box" on conveyer belt and sends a response back to python application using Arduino
15. Go to step 3
16. End application

### 📚 References
- [Train Custom Model from scratch on Roboflow](https://docs.roboflow.com/train/train/train-from-scratch)
- [YOLOv8 Object Detection on a Custom Dataset](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/)
- [Box Detection Model - Roboflow](https://universe.roboflow.com/university-of-heidelberg/box-object-detection)
- [Barcode Detection Model - Roboflow](https://universe.roboflow.com/uniqueidwarehouse-xcp0o/barc_det)

### 💀 Unstable Stuff
- Run this in cmd for getting [support for opencv2's imshow](https://stackoverflow.com/questions/40207011/opencv-not-working-properly-with-python-on-linux-with-anaconda-getting-error-th):
    ```
    pip install opencv-contrib-python
    ```