# ITS_Project
It's an university project for the subject Intelligent Transport Systems.

## The scope of the project

The main purpose of the project is an implementation of a robot controll system, based on traffic sign recognition. For traffic sign recognition we used the deep learning technology. The controlling of the robot use Robot Operation System (ROS) framework. 

Important files is this github repository:
* mydata folder: it's the dataset, we meged it from 2 different datasets.
* ITs.py: Code to train our model.
* labels.csv: Contains the 6 different labels of the traffic signs, what we's like to recognize.
* prediction_listener.py: It reads out  predictions from a rostopic, and implement the controlling commands. 
* streamTX.sh: Start stream from robot side.
* webcam-send-to-rostopic.py: It's do the recognition with the use of computer's webcam. 
