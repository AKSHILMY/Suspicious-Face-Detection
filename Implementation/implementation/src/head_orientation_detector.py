from detector import Detector
import mediapipe as mp
from sympy import Plane, Point3D, Line3D
from math import pi
from constant import Constants
from cv2 import imshow, cvtColor, COLOR_RGB2BGR, COLOR_BGR2RGB, flip


mp_pose = mp.solutions.pose


class HeadOrientationDetector(Detector):
    def __init__(self):
        self.angle = None
        self.threshold_angle = Constants.default_threshold_angle_head_orientation
        self.pose = mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)

    def set_threshold_angle(self, angle):
        self.threshold_angle = angle

    def get_point(self, frame, results, pose_landmark):
        coordinates = {'x': results.pose_landmarks.landmark[pose_landmark].x * frame.shape[0], 'y': results.pose_landmarks.landmark[
            pose_landmark].y * frame.shape[1], 'z': results.pose_landmarks.landmark[pose_landmark].z * frame.shape[2]}
        point = Point3D(
            coordinates['x'], coordinates['y'], coordinates['z'], evaluate=False)
        print(f'P : {point}')
        return point

    def get_angle_of_orientation(self, line_p, z_plane):
        right_side_check = True
        # get the angle between line P and z plane
        rad_angle = z_plane.angle_between(line_p)
        degree_angle = rad_angle*180/pi
        print(degree_angle)
        if degree_angle < 0:  # left
            right_side_check = False
        return abs(degree_angle), right_side_check

    def draw_face(self, frame, results):
        # Draw the pose annotation on the image.
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        frame.flags.writeable = True
        frame = cvtColor(frame, COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # Flip the image horizontally for a selfie-view display.
        imshow('MediaPipe Pose', frame)
        flip(frame, 1)

    def detect(self, frame, draw=False):
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        frame.flags.writeable = False
        frame = cvtColor(frame, COLOR_BGR2RGB)

        results = self.pose.process(frame)
        if results.pose_landmarks:
            # print(frame.shape)

            nose_point = self.get_point(
                frame, results, mp_pose.PoseLandmark.NOSE)
            left_ear_point = self.get_point(
                frame, results, mp_pose.PoseLandmark.LEFT_EAR)
            right_ear_point = self.get_point(
                frame, results, mp_pose.PoseLandmark.RIGHT_EAR)
            # LR = Line3D(right_ear_point, left_ear_point)
            M = (left_ear_point+right_ear_point)/2
            # Get the line that passes through N and the Line LR
            line_p = Line3D(M, nose_point)
            # print(M in LR)qq

            z_plane = Plane(Point3D(0, 0, 1000), Point3D(
                0, 0, -1000), Point3D(0, 1000, 0))
            degree_angle, left_side = self.get_angle_of_orientation(
                line_p, z_plane)
            if draw:
                self.draw_face(frame, results)
            if degree_angle > self.threshold_angle:
                return {"angle": degree_angle, "side": left_side}
            return False

        # Draw the pose annotation on the image.
        # image.flags.writeable = True
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # mp_drawing.draw_landmarks(
        #     image,
        #     results.pose_landmarks,
        #     mp_pose.POSE_CONNECTIONS,
        #     landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # # Flip the image horizontally for a selfie-view display.
        # cv2.imshow('MediaPipe Pose', image)
