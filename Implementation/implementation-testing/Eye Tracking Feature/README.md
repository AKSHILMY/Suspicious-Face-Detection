# Approach

<img src="../../assets/images/eye_track_approach.jpg" alt="drawing" width="700"/>

# Calculation of depth of eye from camera

## 01. Using the focal length of camera to estimate the depth
<img src="../../assets/images/focal_length_approach.png" alt="image" width="700"/>
<br>
In this approach for depth estimation, the focal length of the camera need to be calculated prior to working of the mathematical operation.
<br>
The average distance between eyes of an adult human eye : _6.3 cm_
Calculate the distance between eyes in the captured image using facial landmarks detector.
<br><br>

```
img, faces = detector.findFaceMesh(img,draw = False)
face = faces[0]
```
From <a href="https://raw.githubusercontent.com/google/mediapipe/a908d668c730da128dfa8d9f6bd25d519d006692/mediapipe/modules/face_geometry/data/canonical_face_model_uv_visualization.png">here</a> , the landmarks of the face could be obtained.<br>
The pixel coordinates of the eyes are obtained from the facial landmarks array.
<br>
```
pointLeft = face[145]
pointRight =  face[374]
```
The distance is calculated 
```
w,_ = detector.findDistance(pointLeft,pointRight) 
```
<br>
<img src="../../assets/my_images/w_1.png" alt="image" width="200"/>
<img src="../../assets/my_images/w_2.png" alt="image" width="200"/>
<br>
The above images show the distance between the eyes in the frames captured at two instances.

#### Calculation of the focal length of camera
The intention is to calculate the focal length using the formula.
$$ f = {w \over W}{d} $$
Steps<br>
```
1. d is set to 50 cm 
   Place your eyes at an accurate distance of 50 cm from the camera
```
```
2. W is considered to be at an average of 6.3 cm
```
```
3. w is obtained using the detector discussed above
```
```
4. Calculate f
```

| Estimation Strategy| Limitations | Possible Improvements|
|:---|:---|:---|
|Mathematical| - Less accuracy of focal length <br> - Needs Camera Calibration <br>| Get the actual focal length from the camera system|

