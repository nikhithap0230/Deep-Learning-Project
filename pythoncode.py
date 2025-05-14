import cv2
import torch
from ultralytics import YOLO

# Load YOLOv8 model (Ensure you have a model trained for weapon detection)
model = r"C:\Users\nikit\Downloads\archive"
  # Replace "best.pt" with your trained model path

# Load CCTV image
image_path = r"C:\Users\nikit\OneDrive\Desktop\PROJECT\13.jpg"  # Replace with actual image path
image = cv2.imread(image_path)

# Perform detection
results = model(image)

# Draw bounding boxes on detected objects
if results:
    # Assuming 'results' contains the detections
    for result in results:
        # For each detected object (assuming 'result.boxes' exists)
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            confidence = box.conf[0]  # Confidence score
            label = f"Weapon {confidence:.2f}"

            # Draw rectangle and label
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Show image with detections
cv2.imshow("Weapon Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
