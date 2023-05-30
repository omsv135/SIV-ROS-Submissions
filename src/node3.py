#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    try:
        #converting the ros image message to opencv format
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")

        #displays the cropped image
        cv2.imshow("Webcam-Cropped-Image", cv_image)
        cv2.waitKey(1)  #Refresh display every 1 ms

    except Exception as e:
        rospy.logerr(e)

def image_viewer():
    #initializing the node
    rospy.init_node('image_viewer', anonymous=True)

    #Creating a subscriber for the image topic
    rospy.Subscriber('Webcam_cropped', Image, image_callback)

    rospy.spin()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        image_viewer()
    except rospy.ROSInterruptException:
        pass
