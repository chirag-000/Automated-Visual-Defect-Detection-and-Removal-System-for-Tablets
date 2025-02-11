# Automated-Visual-Defect-Detection-Removal-System-for-Tablets
The system uses machine learning, real-time communication, and embedded systems to perform defect detection and physical removal of defective units. This project demonstrates the integration of computer vision, microcontroller programming, and mechanical design for a complete automated manufacturing solution.

I have integrated a custom YOLOv8 model for visual inspection. The is designed to detect any defects in tablets moving along a conveyor belt and immediately remove the defective ones using a servo motor controlled by an STM32 microcontroller. Additionally, I established serial communication between the STM32 and a wxWidgets application (to send data from computer computer to STM32 via usb port), allowing for real-time defect logging and management.

## Technologies Used
* **Machine Learning**: YOLOv8 (Ultralytics) for building the defect detection model.
* **Programming Languages**: Python (for ML inference), C++ (Arduino code for STM32), wxWidgets (C++ for GUI and serial communication).
* **Embedded System**: STM32 microcontroller for controlling the servo motor.
* **Hardware**:
    * Conveyor system where tablet moves, built with wooden planks, wheels, DC motor, elastic belt...
    * USB camera for real-time image capture
    * Servo motor for physical removal of defective tablets.


## Workflow
These steps represent the approach I followed to implement the system. However, other approaches or variations in hardware, software, and communication methods may also be used to achieve similar functionality.

### 1.  Dataset Creation
* Used [Google's Teachable Machine](https://teachablemachine.withgoogle.com/train/) to capture images with three classes:
    * No-defect (normal tablets)
    * Defected (damaged tablets)
    * Background (null category)
    
    and uploaded these images to Roboflow.
* Performed annotation, labeling, augmentation, and preprocessing on Roboflow. For all these steps I followed this [tutorial](https://youtu.be/wuZtUMEiKWY?si=PZ66WE1yqIztybXL).
* Dataset size: 11,832 images. The dataset can be accessed [here](https://universe.roboflow.com/fyp-qjwy0/tablet-defect-detection-er87f) by anyone.
* Exported the dataset and loaded it into Google Colab for training.

### 2.  Model Training & Exporting
* Trained the custom YOLOv8 model on Google Colab using Ultralytics YOLOv8 framework. You can check out the [code](https://github.com/chirag-000/Automated-Visual-Defect-Detection-and-Removal-System-for-Tablets/blob/main/defect_detection1.ipynb). I followed the same [tutorial](https://youtu.be/wuZtUMEiKWY?si=PZ66WE1yqIztybXL) mentioned above.
* Achieved 99.2% mAP (Mean Average Precision), in this [model](https://universe.roboflow.com/fyp-qjwy0/tablet-defect-detection-er87f/model/3).
* Exported the trained model (best.pt). Which can be done [this way](https://youtu.be/WbomGeoOT_k?t=20&si=TR5ZRDD82689muMX).
