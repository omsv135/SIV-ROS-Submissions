#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import sys

def imgmsg_to_cv2(img_msg):
    dtype = np.dtype("uint8") # Hardcode to 8 bits...
    dtype = dtype.newbyteorder('>' if img_msg.is_bigendian else '<')
    image_opencv = np.ndarray(shape=(img_msg.height, img_msg.width, 3), # and three channels of data. Since OpenCV works with bgr natively, we don't need to reorder the channels.
                    dtype=dtype, buffer=img_msg.data)
    # If the byt order is different between the message and the system.
    if img_msg.is_bigendian == (sys.byteorder == 'little'):
        image_opencv = image_opencv.byteswap().newbyteorder()
    return image_opencv

def img_callback(img_msg):
    frame = imgmsg_to_cv2(img_msg)
    cv2.imshow('Webcam Cropped', frame)
    cv2.waitKey(1)

def webcam_show_node():
    rospy.init_node('webcam_show_node', anonymous=True)
    img_sub = rospy.Subscriber('Webcam_cropped', Image, img_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        webcam_show_node()
    except rospy.ROSInterruptException:
        pass