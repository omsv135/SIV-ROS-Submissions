#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

image_publisher = None

def img_callback(msg):
    global image_publisher

    try:
        #now convert the ros image into cv image
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")

        #cropping by 30% pixels [y1:y2, x1:x2] where (x1,y1) is the coordinate of bottom left corner and (x2,y2) is of top right corner
        cropped_image = cv_image[108:396, 192:1088]
        #again converting cv image to ros image message
        cropped_msg = bridge.cv2_to_imgmsg(cropped_image, "bgr8")

        #publishes the cropped image
        image_publisher.publish(cropped_msg)

    except Exception as e:
        rospy.logerr(e)

def img_cropper():
    global image_publisher

    #init_node command to initialize the node
    rospy.init_node('image_cropper', anonymous=True)

    #Creating a publisher for the cropped image topic
    image_publisher = rospy.Publisher('Webcam_cropped', Image, queue_size=10)

    # Creating a subscriber for the image topic
    rospy.Subscriber('Webcam_img', Image, img_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        img_cropper()
    except rospy.ROSInterruptException:
        pass
