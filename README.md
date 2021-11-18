# ITS_Project
It's an university project for the subject Intelligent Transport Systems.

## The scope of the project

The main purpose of the project is an implementation of a robot control system, based on traffic sign recognition. For traffic sign recognition we used deep learning technology. The controlling of the robot uses Robot Operation System (ROS) framework. 

Important files are this GitHub repository:
* mydata folder: it's the dataset, we merged it from 2 different datasets.
* ITs.py: Code to train our model.
* labels.csv: Contains the 6 different labels of the traffic signs, what we're like to recognize.
* prediction_listener.py: It reads out  predictions from a rostopic, and implements the controlling commands. 
* streamTX.sh: Start stream from the robot side.
* webcam-send-to-rostopic.py: It's doing the recognition with the use of a computer's webcam. 
