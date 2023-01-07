# head-orientation-detection
        head_orientation_detector.set_threshold_angle(50)
        det = head_orientation_detector.detect(image)
        if not det:
            continue
        else:
            print("Head Orientation Angle Exceeded: ", det)
            break