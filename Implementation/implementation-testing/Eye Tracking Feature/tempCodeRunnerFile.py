nose_coordinates = {'x': results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image.shape[0], 'y': results.pose_landmarks.landmark[
            #     mp_pose.PoseLandmark.NOSE].y * image.shape[1], 'z': results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z * image.shape[2]}
            # print(
            #     f'Nose coordinates: ('
            #     f'{nose_coordinates}'
            # )