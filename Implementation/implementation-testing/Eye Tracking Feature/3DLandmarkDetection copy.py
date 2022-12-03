from cvzone.FaceMeshModule import FaceMeshDetector
from cv2 import VideoCapture, waitKey, imshow, destroyAllWindows
cap = VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
i = 0
while cap.isOpened():
    success, image = cap.read()
    img, dets = detector.findFaceMesh(image, draw=True)
    if len(dets) == 0:
        print('No detections')
    # assume only 1 face per frame
    facial_points = dets[0]
    print('Facial points', facial_points)
    if waitKey(1) & 0xFF == ord('q'):
        print("End")
        break
    if i == 25:
        break
    else:
        i += 1


cap.release()
destroyAllWindows()
