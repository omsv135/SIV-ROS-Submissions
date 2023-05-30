# SIV-ROS Submissions
**Sensor Integration and Visualisation in ROS**

ASSIGNMENT-1
#create a catkin workspace
mkdir catkin_ws
cd catkin_ws
mkdir src
catkin_make
cd
source ~/catkin_ws/devel/setup.bash

#create a new package "image_processes"
cd ~/catkin_ws/src
catkin_create_pkg image_processes rospy cv2 cv_bridge sensor_msgs

#create three nodes
cd ~/catkin_ws/src/image_processes
mkdir scripts
cd scripts
touch node1.py
chmod node1.py
touch node2.py
chmod node2.py
touch node3.py
cd ../..
code .
writing three nodes' code

run roscore in one terminal and then run three nodes in three terminal windows
