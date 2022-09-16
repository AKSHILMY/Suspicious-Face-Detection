## Basic Face Detection
The detection of the face is an essential feature for this monitoring system. Though this detection could serve as an attendance recording procedure at the intial stage of the monitoring process, the availability of the student through out the monitoring session is highly important.
Also, the monitoring system ensures that the student solely does his work. Here is when the detection of multiple faces comes to play.

#### 1. HAAR Classifier with AdaBoost algorithm
<span>
  <img src="../../assets/images/team_photo.png" align="right" width="400" >
</span>

- Less Detection Reliablity
  - Detection of Non-Faces as Faces at some instances
  - No detection of faces when the lighting is less  
Thus, a convolutional neural network was attempted to be employed.

#### 2. Multi-Task Convolution Neural Network (MTCNN)

- The MTCCN detection is capable of detecting the face under a considerably less lighting with higher reliability than the boosted HAAR classifier. 


#### 3. Face Detection Machine Learning Model from MediaPipe Python Package 

| Detection Strategy | Description | Approximate FPS | Limitations | Positives|
|:---| :---| :---| :---| :---|
| `HAAR Classifier _Boosted_` | | | | |
| `Multi-Task CNN`| | | | |




