## Basic Face Detection
The detection of the face is an essential feature for this monitoring system. Though this detection could serve as an attendance recording procedure at the intial stage of the monitoring process, the availability of the student through out the monitoring session is highly important.
Also, the monitoring system ensures that the student solely does his work. Here is when the detection of multiple faces comes to play.

### **Overview Of the Tested Face Detection Stategies**

| Detection Strategy| Mean Speed _FPS_ | Limitations | Positives|Improvements|
|:---|:---|:---|:---|:---|
| <a href= https://github.com/AKSHILMY/Suspicious-Face-Detection/blob/main/Implementation/Face%20Detection%20Feature/Face%20Detection%20using%20Haar.ipynb>`HAAR Classifier`</a> | ~ 1 | - Detection of Non-Faces as Faces at some instances <br> - No detection of faces when the lighting is less| |- Asynchronous Programming<br> - Multi-Threading|
| <a href= https://github.com/AKSHILMY/Suspicious-Face-Detection/blob/main/Implementation/Face%20Detection%20Feature/Face%20Detection%20using%20MTCNN.ipynb>`Multi-Task CNN`</a>| ~ 2 | | |- Asynchronous Programming<br> - Multi-Threading|
| <a href= https://github.com/AKSHILMY/Suspicious-Face-Detection/blob/main/Implementation/Face%20Detection%20Feature/Face%20Detection%20using%20Tensor%20Flow%20and%20Media%20Pipe.ipynb>`MediaPipe Face Detection Model`</a>| ~ 45 | | - Lightweight Object Detection <br> - Effective GPU utilization <br> - Quality Prediction <br> - Allows Estimation Face Rotation (roll angle) | |

### Resources
- [MediaPipe Face Detection Model](https://google.github.io/mediapipe/solutions/face_detection)  
- [Blaze Face](https://arxiv.org/abs/1907.05047)
- [MobileNetV1/V2](https://ai.googleblog.com/2018/04/mobilenetv2-next-generation-of-on.html)

_Note that this page is not yet fully update_<br>
Click <a href=https://github.com/AKSHILMY/Suspicious-Face-Detection#basic-face-detection>here</a> to return to main page
