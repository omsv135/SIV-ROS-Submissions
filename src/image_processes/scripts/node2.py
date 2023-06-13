#!/usr/bin/env python3

# Import the necessary libraries
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
import numpy as np
import sys 
 
def crop_image(frame, percentage):
    height, width = frame.shape[:2]
    crop_height = int(height * percentage)
    crop_width = int(width * percentage)
    cropped_frame = frame[crop_height:, crop_width:]
    return cropped_frame



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
    bridge = CvBridge()
    frame = imgmsg_to_cv2(img_msg)
    cropped_frame = crop_image(frame, 0.3)  # Crop by 30% in pixels
    cropped_img_msg = bridge.cv2_to_imgmsg(cropped_frame)
    pub = rospy.Publisher('Webcam_cropped', Image, queue_size=10)
    pub.publish(cropped_img_msg)

def webcam_cropped_node():
    rospy.init_node('webcam_cropped_node', anonymous=True)
    rospy.Subscriber('Webcam_img', Image, img_callback)
    
    rate = rospy.Rate(10)  # 10Hz

    rospy.spin()
    
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        webcam_cropped_node()
    except rospy.ROSInterruptException:
        pass