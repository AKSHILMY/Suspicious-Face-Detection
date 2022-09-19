# Suspicious Face Detection : A Monitoring System

## Application Scenario 

This project is based on the detection of suspicious behavior of a person analysing the facial aspects of the respective person. The project primarily focuses the implementation to be done as a lab monitoring system. 
<br/>
The overview of the system is shown below.

![See Plan](./assets/images/application_scenario.jpg?raw=true "Application Scenario")

As observed in the above image, a computer installed with a desktop application that runs in the background is provided to the user (student) and a web application is provided to the officials. The desktop application consists of real-time detection and warning algorithms that detect the suspicious behavior of the user and provide instant warnings to user and the officials. The detection algorithms focus on the certain important aspects of the face as well as some external aspects to make the detection possible. 
The detection details and warnings are sent from the computer to the remote server from which the details are updated to a database and also rendered to a web application. The warnings are notified to the officials by means of this web application. The warnings for the students are displayed in the computer desktop itself so that the student could adhere to the monitoring process.

## Plan for the proposed Project
Note that there can be unexpected delays and changes to the this plan. 

![See Plan](./assets/images/plan.jpg?raw=true "Plan")

## Basic Face Detection
The detection of the face is an essential feature for this monitoring system. Though this detection could serve as an attendance recording procedure at the intial stage of the monitoring process, the availability of the student through out the monitoring session is highly important. Also, the monitoring system ensures that the student solely does his work. Here is when the detection of multiple faces comes to play. <br>
<a href="https://github.com/AKSHILMY/Suspicious-Face-Detection/blob/main/Implementation/Face%20Detection%20Feature/README.md">See more ...</a>
