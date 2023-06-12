#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

#def subscribe_and_crop():


def crop_webcam_frames(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

    height, width, _ = cv_image.shape
    crop_width = int(width * 0.3)
    crop_height = int(height * 0.3)
    cropped_image = cv_image[crop_height:-crop_height, crop_width:-crop_width]

    # Publish the cropped image
    cropped_pub.publish(bridge.cv2_to_imgmsg(cropped_image, encoding="bgr8"))



if __name__ == '__main__':
    try:
        rospy.init_node('image_cropper', anonymous=True)
        rospy.Subscriber('Webcam_img', Image, crop_webcam_frames)
        cropped_pub = rospy.Publisher('Webcam_cropped', Image, queue_size=10)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass