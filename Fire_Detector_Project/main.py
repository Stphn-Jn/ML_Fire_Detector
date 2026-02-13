import cv2
from ultralytics import YOLO

# 1. Load your newly trained model
# Ensure 'best.pt' is in the SAME folder as this script
model = YOLO('best.pt') 

# 2. Set the Source
# Use 0 for Webcam, or 'video.mp4' for a video file
cap = cv2.VideoCapture(0) 

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run detection
    results = model(frame, stream=True)

    for r in results:
        for box in r.boxes:
            # Get coordinates and dimensions
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            h, w, _ = frame.shape
            
            # Feature: Calculate Intensity %
            fire_area = (x2 - x1) * (y2 - y1)
            intensity = (fire_area / (h * w)) * 100

            # Feature: Danger Level Logic
            color = (0, 255, 0) # Default Green (Safe)
            status = "Low: Small Fire"
            
            if intensity > 30:
                status, color = "CRITICAL: LARGE FIRE", (0, 0, 255) # Red
            elif intensity > 10:
                status, color = "WARNING: MEDIUM FIRE", (0, 165, 255) # Orange

            # Draw UI Elements
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{status} ({intensity:.1f}%)", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Display the live window
    cv2.imshow('Live Fire & Intensity Monitor', frame)

    # Press 'q' to stop the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()