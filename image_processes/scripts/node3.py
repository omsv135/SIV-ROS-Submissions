#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(img_msg):
    bridge = CvBridge()

    # Convert the ROS Image message to OpenCV image
    frame = bridge.imgmsg_to_cv2(img_msg, "bgr8")

    # Show the image
    cv2.imshow("Webcam Cropped", frame)
    cv2.waitKey(1)

def node3():
    rospy.init_node('node3', anonymous=True)
    sub = rospy.Subscriber('Webcam_cropped', Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        node3()
    except rospy.ROSInterruptException:
        pass
