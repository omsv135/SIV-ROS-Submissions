#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def crop_image(frame):
    height, width = frame.shape[:2]
    cropped_width = int(width * 0.7)  # Crop width by 30%
    cropped_frame = frame[:, :cropped_width, :]
    return cropped_frame

def node2():
    rospy.init_node('node2', anonymous=True)
    sub = rospy.Subscriber('Webcam_img', Image, image_callback)
    pub = rospy.Publisher('Webcam_cropped', Image, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    bridge = CvBridge()

    def image_callback(img_msg):
        # Convert the ROS Image message to OpenCV image
        frame = bridge.imgmsg_to_cv2(img_msg, "bgr8")

        # Crop the image
        cropped_frame = crop_image(frame)

        # Convert the cropped OpenCV image to ROS Image message
        cropped_img_msg = bridge.cv2_to_imgmsg(cropped_frame, "bgr8")

        # Publish the cropped image message to 'Webcam_cropped' topic
        pub.publish(cropped_img_msg)

    rospy.spin()

if __name__ == '__main__':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass
