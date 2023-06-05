#!/usr/bin/env python3


import rospy 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2
 
def callback(data):
  br = CvBridge()
  rospy.loginfo("receiving video frame")
  current_frame = br.imgmsg_to_cv2(data)
  cv2.imshow("output", current_frame)
  cv2.waitKey(0)
      
def receive_message():
  rospy.init_node('sub1_node', anonymous=True)
  rospy.Subscriber('webcam_cropped', Image, callback)
  rospy.spin()
  cv2.destroyAllWindows()
  
if __name__ == '__main__':
  receive_message()