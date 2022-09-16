## Basic Face Detection
The detection of the face is an essential feature for this monitoring system. Though this detection could serve as an attendance recording procedure at the intial stage of the monitoring process, the availability of the student through out the monitoring session is highly important.
Also, the monitoring system ensures that the student solely does his work. Here is when the detection of multiple faces comes to play.

### **Overview Of the Tested Face Detection Stategies**

| Detection Strategy | Description | Speed _FPS_ | Limitations | Positives|Improvements|
|:---|:---|:---|:---|:---|:---|
| `HAAR Classifier` | | | Detection of Non-Faces as Faces at some instances <br> No detection of faces when the lighting is less| |- Asynchronous Programming<br> - Multi-Threading|
| `Multi-Task CNN`| | | | |- Asynchronous Programming<br> - Multi-Threading|
| `MediaPipe Model`| | Mean: 40 <br> Max: 160+ | | | |

### The Background Of the Selected _MediaPipe Face Detection_ Model
### Resources
- [MediaPipe Face Detection Model](https://google.github.io/mediapipe/solutions/face_detection)  
- [Blaze Face](https://arxiv.org/abs/1907.05047)
- [MobileNetV1/V2](https://ai.googleblog.com/2018/04/mobilenetv2-next-generation-of-on.html)



