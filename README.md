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

### Dataset Creation

