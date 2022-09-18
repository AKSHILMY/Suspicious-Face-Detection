# Suspicious Face Detection : A Monitoring System

## Application Scenario 

This project is based on the detection of suspicious behavior of a person analysing the facial aspects of the respective person. The project primarily focuses the implementation to be done as a lab monitoring system. The system would consist of the following features:

1. Desktop Application
      - Detection Algorithm
        - Detection of Face : _Identifying 'No Face' and 'Multiple Faces' detection scenarios_
        - Detection of Light Intensity : _possesses a threshold value_
        - Detection of Lip Movement : _recognition of speaking_
        - Detection of Head Orientation : _possesses a threshold angle of orientation_
        - Analysis of Facial Expressions 
        - Tracking of Eye
      - Warning System
2. Database
3. Remote Server
4. Web Application


A warning system is implemented in this project to notify the officials about the detections so that immediate necessary actions could be taken. The detection details are sent from a desktop application to a remote server from which the details are rendered to a WebApp GUI to be viewed by the official. Important detection details are stored in a database.

## Plan for the proposed Project
![See Plan](./assets/images/plan.jpg?raw=true "Plan")

## Basic Face Detection
The detection of the face is an essential feature for this monitoring system. Though this detection could serve as an attendance recording procedure at the intial stage of the monitoring process, the availability of the student through out the monitoring session is highly important. Also, the monitoring system ensures that the student solely does his work. Here is when the detection of multiple faces comes to play. <br>
<a href="https://github.com/AKSHILMY/Suspicious-Face-Detection/blob/main/Implementation/Face%20Detection%20Feature/README.md">See more ...</a>
