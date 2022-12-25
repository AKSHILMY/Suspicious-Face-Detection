from turtle import left
import cv2
import mediapipe as mp
from sympy import Plane, Point3D, Line3D
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
maxima = 0
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        if results.pose_landmarks:
            print(image.shape)
            nose_coordinates = {'x': results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image.shape[0], 'y': results.pose_landmarks.landmark[
                mp_pose.PoseLandmark.NOSE].y * image.shape[1], 'z': results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z * image.shape[2]}
            left_ear_coordinates = {'x': results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].x * image.shape[0], 'y': results.pose_landmarks.landmark[
                mp_pose.PoseLandmark.LEFT_EAR].y * image.shape[1], 'z': results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].z * image.shape[2]}

            right_ear_coordinates = {'x': results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].x * image.shape[0], 'y': results.pose_landmarks.landmark[
                mp_pose.PoseLandmark.RIGHT_EAR].y * image.shape[1], 'z': results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].z * image.shape[2]}

            nose_point = Point3D(
                nose_coordinates['x'], nose_coordinates['y'], nose_coordinates['z'], evaluate=False)
            print(f'N: {nose_point}')

            right_ear_point = Point3D(
                right_ear_coordinates['x'], right_ear_coordinates['y'], right_ear_coordinates['z'], evaluate=False)
            print(f'R: {right_ear_point}')

            left_ear_point = Point3D(
                left_ear_coordinates['x'], left_ear_coordinates['y'], left_ear_coordinates['z'], evaluate=False)
            print(f'L: {left_ear_point}')

            LR = Line3D(right_ear_point, left_ear_point)
            M = (left_ear_point+right_ear_point)/2
            # Get the line that passes through N and the Line LR
            lineP = Line3D(M, nose_point)
            # print(M in LR)qq

            z_plane = Plane(Point3D(0, 0, 1000), Point3D(
                0, 0, -1000), Point3D(0, 1000, 0))

            # get the angle between line P and z plane
            rad_angle = z_plane.angle_between(lineP)
            degree_angle = rad_angle*180/np.pi
            print(degree_angle)
            if np.abs(degree_angle) > maxima:
                maxima = np.abs(degree_angle)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Pose', image)
        cv2.flip(image, 1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
print(f'Maximum Angle: {maxima}')
cv2.destroyAllWindows()
cap.release()
