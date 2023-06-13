#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def node1():
    rospy.init_node('node1', anonymous=True)
    pub = rospy.Publisher('Webcam_img', Image, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    cap = cv2.VideoCapture(0)  # Open the webcam

    bridge = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()

        if ret:
            # Convert the OpenCV image to ROS Image message
            img_msg = bridge.cv2_to_imgmsg(frame, "bgr8")

            # Publish the image message to 'Webcam_img' topic
            pub.publish(img_msg)

        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
