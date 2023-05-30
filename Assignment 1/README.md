What I have done for this Assignment:

#Learnt about openCv, classes, methods and about various dependencies to create/build a package.
#Create a package named image_processes in catkin_ws/src folder by running command line in terminal as catkin_create-pkg image_processes rospy roscpp cv_bridge stdg_msgs and more.
#Now run the catkin_make command in catkin_ws folder
#now created the node1.py node2.py node3.py files in catkin_ws/src/image_processes/src path
#now make the files executable by running command chmod +x node1.py and similarily for others two
#in node1.py imports the required libraries and then created a webcam-pub function which gopen the camera gather the image data and then publish it to the Webcam
-img topic
#in node2.py I sunscribed to Webcam_img topic then publish a Webcam_cropped topic which has the iamge data 30% reduced by pixels
#in node3.py I subscribed the Webcam_cropped topic then show that cropped image
