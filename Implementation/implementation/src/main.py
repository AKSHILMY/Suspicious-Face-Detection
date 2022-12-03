from cv2 import VideoCapture
from face_detector import FaceDetector
import requests

cap = VideoCapture(0)
face_detector = FaceDetector()
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("No Camera Detected")
        break
    detection_type = face_detector.detect(image)
    print(detection_type)
    try:
        if detection_type["suspicious"] == "True":
            print("Post Request")
            url = "http://localhost:3000/detections"
            requests.post(url, json=detection_type)
        # Send a post request to server along with the detection_type JSON object
    except requests.exceptions.ConnectionError:
        print("Connection Error")
cap.release()
