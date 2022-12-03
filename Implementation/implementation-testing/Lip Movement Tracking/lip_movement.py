from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from skimage.transform import resize

import numpy as np
import cv2
import math

from cvzone.FaceMeshModule import FaceMeshDetector
# Add keys to this hash for supporting other action classes. e.g. CLASS_HASH = {'other': 0, 'speech': 1, 'chew': 2, 'laugh': 3}
CLASS_HASH = {
    'silent': 0,
    'speaking': 1
}


FRAME_SEQ_LEN = 25

detector = FaceMeshDetector(maxFaces=1)
shape_predictor = "E:\SEM 05 CSE19\The Deciding Project\Suspicious-Face-Detection\Implementation\implementation\models\shape_predictor_68_face_landmarks.dat"


def get_facial_landmark_vectors_from_frame(frame):
    print('Fetching face detections and landmarks...')
    # frame = frame.astype('uint8')
    img, dets = detector.findFaceMesh(frame, draw=True)
    if len(dets) == 0:
        print('No detections')
        return (None, None)
    # assume only 1 face per frame
    facial_points = dets[0]
    facial_points_vector = []
    for i in range(0, len(facial_points)):
        facial_points_vector.append(facial_points[i][0])
        facial_points_vector.append(facial_points[i][1])

    print('Returning ('+str(len(dets)) + ', ' + str(len(facial_points)) + ')')
    return (dets, facial_points, facial_points_vector)


def dist(p1, p2):
    p1_x = p1[0]
    p2_x = p2[0]
    p1_y = p1[1]
    p2_y = p2[1]
    dist = math.sqrt((p2_x - p1_x) ** 2 + (p2_y - p1_y) ** 2)
    return dist


def collect_frame():
    global cap, frames, frame_num, font, state, input_sequence
    while not cap.isOpened():
        cap = cv2.VideoCapture(0)
        cv2.waitKey(1000)
        print("Wait for the header")
    flag, frame = cap.read()
    print("Capturing frame: " + str(frame_num))
    if flag:
        (dets, facial_points_coordinates,
         facial_points_vector) = get_facial_landmark_vectors_from_frame(frame)
        if not dets or not facial_points_vector:
            return frame
        frames.append(frame)
        cv2.putText(frame, str(frame_num), (2, 10), font,
                    0.3, (255, 255, 255), 1, cv2.LINE_AA)
        # draw a box showing the detected face
        for k, d in enumerate(dets):
            left = d[234][0]
            right = d[454][0]
            top = d[10][1]
            bottom = d[152][1]
            cv2.rectangle(frame, (left, top),
                          (right, bottom), (0, 255, 0), 2)
            # draw the state label below the face
            cv2.rectangle(frame, (left, bottom), (right,
                          bottom + 10), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, state, (left + 2, bottom + 10 - 3),
                        font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        input_sequence.append(facial_points_vector)
    frame_num += 1
    return frame, dets

    # if len(frames) < 25:
    #     return False
    # else:
    #     print('Collected' + str(len(frames)) + ' frames from the web cam.')
    #     return True


def detect_lip_movement(input_sequence_list, model, dets):
    # get the most recent N sequences where N=FRAME_SEQ_LEN
    seq = input_sequence[-1 * FRAME_SEQ_LEN:]
    f = []
    for coords in seq:
        part_41 = (int(coords[2 * 41]), int(coords[2 * 41 + 1]))
        part_179 = (int(coords[2 * 179]), int(coords[2 * 179 + 1]))
        part_12 = (int(coords[2 * 12]), int(coords[2 * 12 + 1]))
        part_15 = (int(coords[2 * 15]), int(coords[2 * 15 + 1]))
        part_271 = (int(coords[2 * 271]), int(coords[2 * 271 + 1]))
        part_403 = (int(coords[2 * 403]), int(coords[2 * 403 + 1]))

        A = dist(part_41, part_179)
        B = dist(part_12, part_15)
        C = dist(part_271, part_403)

        avg_gap = (A + B + C) / 3.0

        f.append([avg_gap])

    scaler = MinMaxScaler()
    arr = scaler.fit_transform(f)

    x_data = np.array([arr])

    # y_pred is already categorized
    y_pred = model.predict_on_batch(x_data)

    # print('y_pred=' + str(y_pred) + ' shape=' + str(y_pred.shape))

    # convert y_pred from categorized continuous to single label
    return frame, y_pred


def get_label(y_pred):
    y_pred_max = y_pred[0].argmax()
    # if y_pred_max == 1 and y_pred[0][0] < speak_threshold:
    #     y_pred_max = 0

    # print('y_pred_max=' + str(y_pred_max))

    for k in CLASS_HASH:
        if y_pred_max == CLASS_HASH[k]:
            state = k
            break

    # redraw the label
    for i, d in enumerate(dets):
        # draw the state label below the face
        left = d[234][0]
        right = d[454][0]
        bottom = d[152][1]
        cv2.rectangle(frame, (left, bottom), (right,
                                              bottom + 10), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, state, (left + 2, bottom +
                    10 - 3), font, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
    return state


if __name__ == '__main__':
    frames = []
    cap = cv2.VideoCapture(0)
    frame_num = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    state = 'Processing'
    input_sequence = []
    model = "implementation\models\model.h5"
    model = load_model(model)

    while True:
        frame, dets = collect_frame()
        if len(input_sequence) >= FRAME_SEQ_LEN:
            frame, y_pred = detect_lip_movement(
                input_sequence, model, dets)
            print('y_pred=' + str(y_pred))
            get_label(y_pred)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
    print('End Detection')

cap.release()
cv2.destroyAllWindows()