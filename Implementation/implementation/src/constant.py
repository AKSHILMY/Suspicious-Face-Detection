from cv2 import FONT_HERSHEY_SIMPLEX


class model:
    FRAME_SEQ_LEN = 25

    # Add keys to this hash for supporting other action classes. e.g. CLASS_HASH = {'other': 0, 'speech': 1, 'chew': 2, 'laugh': 3}
    CLASS_HASH = {
        'silent': 0,
        'speaking': 1
    }
    model = "implementation\models\model.h5"
    cv_font = FONT_HERSHEY_SIMPLEX
