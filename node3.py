#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def node3():
    rospy.init_node('node3', anonymous=True)
    rospy.Subscriber('Webcam_cropped', Image, show_image_callback)

    rospy.spin()

def show_image_callback(image_frame):
    # Convert the ROS image message to OpenCV format
    cv_bridge = CvBridge()
    cv_image = cv_bridge.imgmsg_to_cv2(image_frame, desired_encoding='bgr8')

    # Display the image using OpenCV (you may need to adjust the window name)
    cv2.imshow('Webcam_cropped', cv_image)
    cv2.waitKey(1)  # Refresh the display

if __name__ == '__main__':
    try:
        node3()
    except rospy.ROSInterruptException:
        pass