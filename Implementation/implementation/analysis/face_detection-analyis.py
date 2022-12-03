from datetime import datetime
import time
import requests
import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


# For WebCam input
FPS = []
cap = cv2.VideoCapture(0)
img_num = 1
with mp_face_detection.FaceDetection(
        model_selection=0,  # short range model
        min_detection_confidence=0.5) as face_detection:  # Take a value that performs such that faces outside 1 m are detected are less detected
    while cap.isOpened() and img_num <= 100:
        detection = False
        detection_type = {
            "main-type": "None",
            "sub-type": "None",
            "time-stamp": "None"
        }
        init = time.time()
        success, image = cap.read()
        if not success:
            print("No Camera Detected")
            break
        print(f'Detection of Image {img_num}')
        image.flags.writeable = False
        # image  = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)
        detection_type["main-type"] = "face"
        detection_type["sub-type"] = "single-face"
        image.flags.writeable = True
        # print(results.detections)
        if results.detections:
            if len(results.detections) > 1:
                print(f"Multiple Faces Detected: {len(results.detections)}")
                detection_type["sub-type"] = "multiple-face"
                detection = True
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
        else:
            print("No Face Detected")
            detection_type["sub-type"] = "no-face"
            detection = True
            # break
        detection_type["time-stamp"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print(f"Detection Type: {detection_type}")
        img_num += 1
        cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        fps = (1)/(time.time() - init)
        print('Fps: {}'.format(fps))
        FPS.append(fps)
    if detection:
        url = "http://localhost:3000/"
        x = requests.post(url, json=detection_type)

    cap.release()
    cv2.destroyAllWindows()
    print("Range: "+str(min(FPS))+"fps - "+str(max(FPS))+" fps")
    print("Mean FPS: "+str(sum(FPS)/len(FPS))+" fps")
