#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def webcam_pub():
    #To initialize the node
    rospy.init_node('webcam_publisher', anonymous=True)
    #Creating a publisher for the Webcam_image topic
    image_publisher = rospy.Publisher('Webcam_img', Image, queue_size=10)
    #publishing rate in Hz
    rate = rospy.Rate(10)

    #variable/objct to store CvBridge() class
    bridge = CvBridge()
    #it will open camera
    camera = cv2.VideoCapture(0)

    while not rospy.is_shutdown():
        #it will capture frames
        ret, frame = camera.read()

        if ret:
            try:
                #converts image to ros msg
                image_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
                #publish the image message
                image_publisher.publish(image_msg)
            except Exception as e:
                rospy.logerr(e)

        #It will maintain the publishing rate by sleeping
        rate.sleep()

    camera.release()

if __name__ == '__main__':
    try:
        webcam_pub()
    except rospy.ROSInterruptException:
        pass
