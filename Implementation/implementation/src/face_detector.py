from datetime import datetime
from detector import Detector
from cv2 import flip, imshow, waitKey, destroyAllWindows
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img_num = 0


class FaceDetector(Detector):
    def __init__(self):
        self.detection_type = {
            "main-type": "None",
            "sub-type": "None",
            "time-stamp": "None",
            "suspicious": "False"
        }

    def detect(self, image):
        self.detection_type["main-type"] = "face"
        self.detection_type["suspicious"] = "False"

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
                    self.detection_type["sub-type"] = "multiple-face"
                    self.detection_type["suspicious"] = "True"
                else:
                    print(
                        f"Single Faces Detected")
                    self.detection_type["sub-type"] = "single-face"

            else:
                print("No Face Detected")
                self.detection_type["sub-type"] = "no-face"
                self.detection_type["suspicious"] = "True"
            self.detection_type["time-stamp"] = datetime.now().strftime(
                "%m/%d/%Y, %H:%M:%S")
            print(f"Detection Type: {self.detection_type}")
            self.draw(image, results.detections)
            img_num += 1
            return self.detection_type

    def draw(self, image, detections):
        if detections:
            for detection in detections:
                mp_drawing.draw_detection(image, detection)
            imshow('MediaPipe Face Detection', flip(image, 1))
        if waitKey(1) & 0xFF == ord('q'):
            destroyAllWindows()
            exit(0)
