from ultralytics import YOLO
import time

# Load model
model = YOLO('best.pt')

# Run inference with streaming
results = model(source=0, show=True, conf=0.6, save=True, stream=True)

# Process results
for result in results:
    # For each detection, get class names and write to file
    if result.boxes:  # Check if there are any detections
        with open("C:/Chirag/data.txt", "w") as file:  # Use write mode
            for box in result.boxes:
                class_name = result.names[int(box.cls)]
                if class_name == "defected": 
                    file.write("1\n") 
                else: 
                    file.write("0\n")
        time.sleep(1) # Introduce a delay