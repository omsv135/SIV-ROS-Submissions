#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def node1():
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    pub = rospy.Publisher('Webcam_img', Image, queue_size=10)
    bridge = CvBridge()

    while not rospy.is_shutdown():
        # Capture image frames from webcam
        image_frame = capture_image_from_webcam()
        
        # Convert the image to a ROS message
        ros_image = bridge.cv2_to_imgmsg(image_frame, encoding='bgr8')

        # Publish the image frame
        pub.publish(ros_image)
        rate.sleep()

def capture_image_from_webcam():
    # Open the webcam (usually with device index 0)
    cap = cv2.VideoCapture(0)
    cv2.waitKey(0)

    # Check if the webcam is successfully opened
    if not cap.isOpened():
        print("Failed to open the webcam")
        return None

    # Capture frames from the webcam
    ret, frame = cap.read()

    # Release the webcam
    cap.release()

    # Check if the frame is captured successfully
    if not ret:
        print("Failed to capture frame from the webcam")
        return None

    return frame

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
