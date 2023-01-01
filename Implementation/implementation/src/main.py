from cv2 import VideoCapture
from face_detector import FaceDetector
from lip_movement_detector import LipMovementDetector

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
    if face_detection_type["suspicious"] == "True":
        print("Suspicious")
        break
    else:
        frame, lip_movement_detections = lip_movement_detector.collect_frame(
            cap)


cap.release()
