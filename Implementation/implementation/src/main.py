from cv2 import VideoCapture, waitKey, destroyAllWindows
from face_detector import FaceDetector
from lip_movement_detector import LipMovementDetector
from head_orientation_detector import HeadOrientationDetector

cap = VideoCapture(0)
face_detector = FaceDetector()
lip_movement_detector = LipMovementDetector()
head_orientation_detector = HeadOrientationDetector()

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
        # lip-movement-detection
        frame, lip_movement_detections = lip_movement_detector.collect_frame(
            cap)
        video, speak_state = lip_movement_detector.detect()
        print("Lip Movement State : ", speak_state)
        # if speak_state == 'speaking':
        #     # break
        # head-orientation-detection
        head_orientation_detector.set_threshold_angle(50)
        det = head_orientation_detector.detect(image)
        if not det:
            continue
        else:
            print("Head Orientation Angle Exceeded: ", det)
            break
        # continue
cap.release()
