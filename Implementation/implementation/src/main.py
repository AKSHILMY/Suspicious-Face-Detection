from cv2 import VideoCapture, waitKey, destroyAllWindows
from face_detector import FaceDetector
from lip_movement_detector import LipMovementDetector
from head_orientation_detector import HeadOrientationDetector
import requests
import json

import re, uuid
 
# joins elements of getnode() after each 2 digits.
# using regex expression
print ("The MAC address in formatted and less complex way is : ", end="")
mac_addr = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
cap = VideoCapture(0)
face_detector = FaceDetector()
lip_movement_detector = LipMovementDetector()
head_orientation_detector = HeadOrientationDetector()

detection = False
detection_type = {"device":str(mac_addr),"face":"False","lip":"False","head":"False"}


while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("No Camera Detected")
        break
    face_detection_type = face_detector.detect(image)
    print(face_detection_type)
    if face_detection_type["suspicious"] == "True":
        print("Suspicious")
        detection = True
        detection_type['face'] = "True"
        # break
    else:
        # lip-movement-detection
        if not detection:
            try:
                frame, lip_movement_detections = lip_movement_detector.collect_frame(
                    cap)
                video, speak_state = lip_movement_detector.detect()
                print("Lip Movement State : ", speak_state)
                if speak_state == 'speaking':
                    detection = True
                    detection_type['lip'] = "True"
                    # break
                # head-orientation-detection
                head_orientation_detector.set_threshold_angle(50)
                det = head_orientation_detector.detect(image)
                if not det:
                    continue
                else:
                    print("Head Orientation Angle Exceeded: ", det)
                    detection = True
                    detection_type['head'] = "True"
            except:
                pass
            # break
        # continue
    if detection:
        try:
            det_json = json.dumps(detection_type)
            res = requests.post(url='http://127.0.0.1:5000/', data=det_json,headers = {'Content-Type': 'application/json'})
            print("Sending Request: ")
            if res.ok:
                print("Done")
        except:
            pass
    detection_type['face'] = "False"
    detection_type['lip'] = "False"
    detection_type['head'] = "False"
    detection = False
cap.release()
destroyAllWindows()
