from datetime import datetime
from detector import Detector
import cv2
import time
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img_num = 0


class FaceDetector(Detector):
    def detect(self, image):
        detection_type["main-type"] = "face"
        global img_num
        model_select = 0
        min_detection_confidence = 0.5
        with mp_face_detection.FaceDetection(
                model_selection=model_select,  # short range model
                min_detection_confidence=min_detection_confidence) as face_detection:
            print(f'Detection of Image {img_num}')
            image.flags.writeable = False
            results = face_detection.process(image)
            image.flags.writeable = True
            if results.detections:
                if len(results.detections) > 1:
                    print(
                        f"Multiple Faces Detected: {len(results.detections)}")
                    detection_type["sub-type"] = "multiple-face"
                else:
                    print(
                        f"Single Faces Detected")
                    detection_type["sub-type"] = "single-face"

            else:
                print("No Face Detected")
                detection_type["sub-type"] = "no-face"
            detection_type["time-stamp"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            print(f"Detection Type: {detection_type}")
            img_num += 1
            return detection_type


detection_type = {
    "main-type": None,
    "sub-type": None,
    "time-stamp": None
}
cap = cv2.VideoCapture(0)
face_detector = FaceDetector()
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("No Camera Detected")
        break
    detection_type = face_detector.detect(image)
    print(detection_type)
