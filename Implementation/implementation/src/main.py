from cv2 import VideoCapture
from face_detector import FaceDetector
from lip_movement_detector import LipMovementDetector
import requests
from constant import Constants

cap = VideoCapture(0)
face_detector = FaceDetector()
lip_movement_detector = LipMovementDetector()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("No Camera Detected")
        break
    face_detection_type = face_detector.detect(image)
    print(face_detection_type)
    frame, lip_movement_detections = lip_movement_detector.collect_frame()
    try:
        if face_detection_type["suspicious"] == "True":
            print("Post Request")
            url = "http://localhost:3000/detections"
            requests.post(url, json=face_detection_type)
        # Send a post request to server along with the detection_type JSON object
    except requests.exceptions.ConnectionError:
        print("Connection Error")
cap.release()
