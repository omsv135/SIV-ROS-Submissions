#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def show_cropped_frames(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    cv2.imshow("Webcam Cropped", cv_image)
    cv2.waitKey(1)

def subscribe_and_show():
    rospy.init_node('image_viewer', anonymous=True)
    rospy.Subscriber('Webcam_cropped', Image, show_cropped_frames)
    cv2.namedWindow("Webcam Cropped Image", cv2.WINDOW_NORMAL)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_and_show()
    except rospy.ROSInterruptException:
        pass