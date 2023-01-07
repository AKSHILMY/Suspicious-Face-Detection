# Suspicious Face Detection : A Monitoring System

## Application Scenario 

This project is based on the detection of suspicious behavior of a person analyzing the facial aspects of the respective person. The project primarily focuses the implementation to be done as a lab monitoring system. 
<br/>
The overview of the system is shown below.

<img src="./assets/images/Application_scenario.png?raw=true" alt="Application Scenario" height="400" /><br>

As observed in the above image, a computer installed with an application that runs in the background is provided to the user (student) and a web application is accessed by the officials. The application consists of real-time detection and algorithms that detect the suspicious behavior of the user and provide instant warnings to the officials. The detection algorithms focus on the certain important aspects of the face as well as some external aspects to make the detection possible.
	The detection details and warnings are sent from the computer to the remote server from which the details are updated to a database and also rendered to a web application. The warnings are notified to the officials by means of this web application. 


## Plan for the proposed Project
Note that there can be unexpected delays and changes to this plan. 

<img src="./assets/images/Plan.jpg?raw=true" alt="Plan"/>

## Basic Face Detection
The detection of the face is an essential feature for this monitoring system. Though this detection could serve as an attendance recording procedure at the initial stage of the monitoring process, the availability of the student through out the monitoring session is highly important. Also, the monitoring system ensures that the student solely does his work. Here is when the detection of multiple faces comes to play. <br>

<img src="./assets/images/face_detection.png?raw=true" alt="Face Detection"/><br/>
The frame of webcam input video is taken and processed for detection of faces in the frame using the `MediaPipe Face Detection` model. The face detection feature is done in two ways. One way is be the detection of no-faces and then the other way is the detection of multi-faces in input video frame. The model upon fed with an input frame results in a binary outcome , that is a at least a face is detected in the frame or not. If detected , then the system checks whether a single face or multi faces are detected. As per the needs of the system, multi faces being detected and no face being detected , both are considered as suspicious detections to be notified to the officials.

### Other algorithms and models
1. HAAR cascade classifier `HCC`
2. Multi-task Cascaded Convolutional Networks `MTCNN`


### **Overview Of the Tested Face Detection Stategies**

| Detection Strategy | Limitations | Positives|Improvements|
|:---|:---|:---|:---|
| <a href= https://github.com/AKSHILMY/Suspicious-Face-Detection/blob/main/Implementation/Face%20Detection%20Feature/Face%20Detection%20using%20Haar.ipynb>`HAAR Classifier`</a> | - Detection of Non-Faces as Faces at some instances <br> - No detection of faces when the lighting is less|- Simple & lightweight |- Asynchronous Programming<br> - Multi-Threading|
| <a href= https://github.com/AKSHILMY/Suspicious-Face-Detection/blob/main/Implementation/Face%20Detection%20Feature/Face%20Detection%20using%20MTCNN.ipynb>`Multi-Task CNN`</a>|- Inability to limit the distance of detection| |- Asynchronous Programming<br> - Multi-Threading|
| <a href= https://github.com/AKSHILMY/Suspicious-Face-Detection/blob/main/Implementation/Face%20Detection%20Feature/Face%20Detection%20using%20Tensor%20Flow%20and%20Media%20Pipe.ipynb>`MediaPipe Face Detection Model`</a>| | - Lightweight Object Detection <br> - Effective GPU utilization <br> - Quality Prediction <br> - Allows Estimation Face Rotation (roll angle) | |

## Head Orientation Detection
This system calculates a good estimation of the angle of orientation of the face of a student. The system utilizes `3D Coordinate Geometry` to achieve this estimation. 


### 3D Coordinate Plane
A 3D Coordinate plane is created using the 3D coordinates of the facial landmarks obtained using the `MediaPipe Pose Estimation`. The nose point landmark`N`, left `L` and right `R` ear landmarks are extracted as 3D points
`(x,y,z) coordinate tuple` from the results obtained using the model for a frame input from the webcam.

### Algorithm
<img src="./assets/images/head_orientation_detector.png?raw=true" alt="Head Orientation Detection" height=300/><br/>

- Get Nose point coordinates (N)
- Get Left and Right Ear point coordinates (L & R)
- Get 3D line vector (LR)
- Get 3D point (M)
- Get 3D line vector (NM)
- Get 3D Plane perpendicular to Camera (P)
- Find angle between line NM & plane P

## Speaking Detection
A Speaking Detection Model pre-trained using `HOG` based `dlib` face detector is utilized to predict whether a lip movement is observed or not. 

### Background

<img src="./assets/images/speaking.png?raw=true" alt="Speaking Detection" height=200/><br/>
1. Collect a sequence of 25 frames
2. For each video frame in this sequence :
	- Detect the face in the frame using a face detector ([MediaPipe Face Mesh Model](https://google.github.io/mediapipe/solutions/face_mesh.html) ). 
	- From the landmark predictor, fetch the points that mark the inner edges of the top and bottom lip. 
	- Calculate the average pixel separation between each part pairs and store this distance value into the lip separation sequence.
	- Once all 25 frames are processed this way, perform min-max scaling over the 25-length sequence.
	- Feed this normalized lip separation sequence into the RNN.
	- The RNN generates a 2-element tuple (speech, silence) that represents the likelihood that the speaker was speaking or silent during the 25 video frames before it.
	- Repeat the process for the next 25-frame window of the input video


## Resources
- [MediaPipe Face Detection Model](https://google.github.io/mediapipe/solutions/face_detection)  
- [MediaPipe Pose Estimation Model](https://google.github.io/mediapipe/solutions/pose.html)  
- [MediaPipe Face Mesh Model](https://google.github.io/mediapipe/solutions/face_mesh.html)  
- [Blaze Face](https://arxiv.org/abs/1907.05047)
- [MobileNetV1/V2](https://ai.googleblog.com/2018/04/mobilenetv2-next-generation-of-on.html)


