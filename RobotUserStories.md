# User stories
This document contains all the user stories connected to the Robotic arm. 
The user stories are based on what the user wants to input and wants to receive as an output from the software and hardware.
For every user story a desired software requirements such as RoboDK, LabVIEW, ROS, Arduino or unknown must be used to specify a direction of research.
The user stories will also be implemented on the github repository Fanuc Automated Manufacturing. These can be found in the Issues location.


1.
I want a standard GUI for robot programs with a view of the simulation
Software: RoboDK/Python

2. 
Tool Center Point calibration
A TCP calibration tool has to be milled to be able to perform TCP calibrations in RoboDK.
This must be an aluminium rod with a conical top.
Software: RoboDK

3.
I want to automatically take pictures of a radome based on the 3D CAD model
To inspect a radome a camera will be attached to the robot. The 3D CAD model data needs to be loaded, then a path need to be determined based on this CAD model. Then a picture is made in every position and these are stitched together on the 3D model or a new model is made using the pictures and photogrammetry.
Software: LabVIEW

4. 
Photogrammetry integration
Creating a python script that is able to make a 3D model with the help of a 2D camera (Photogrammetry)
software: RoboDK

5. 
I want to control mill rotation speed via serial
I want to control the spindle speed through a serial connection with an arduino board.
Software: Arduino/Python

6. 
5-axis robot milling
I want to be able to perform 5-axis milling operations with the Fanuc robot using SiemensNX CAM tools and RoboDK
Software: RoboDK/SiemensNX/Fusion360

