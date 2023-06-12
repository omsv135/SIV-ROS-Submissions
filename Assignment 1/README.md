What I have done for this Assignment:

#Learnt about openCv, classes, methods and about various dependencies to create/build a package.
#Create a package named image_processes in catkin_ws/src folder by running command line in terminal as catkin_create-pkg image_processes rospy roscpp cv_bridge stdg_msgs and more.
#Now run the catkin_make command in catkin_ws folder
#now created the node1.py node2.py node3.py files in catkin_ws/src/image_processes/src path
#now make the files executable by running command chmod +x node1.py and similarily for others two
#in node1.py imports the required libraries and then created a webcam-pub function which open the camera gather the image data and then publish it to the Webcam
-img topic
#in node2.py I subscribed to Webcam_img topic then publish a Webcam_cropped topic which has the image data 30% reduced by pixels. To crop, first we have to convert Ros image into cv image then crop it again convert into Ros image.
#in node3.py I subscribed the Webcam_cropped topic then show that cropped to image
#Finally created a launch file which launches all the three nodes at once.



#resources:-
wiki.ros.org
ChatGPT
askubuntu.com
stackoverflow.com