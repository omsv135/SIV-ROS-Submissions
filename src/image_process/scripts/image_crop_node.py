#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
   
def callback(img_input):
  br = CvBridge()
  image2 = br.imgmsg_to_cv2(img_input)
  width = image2.shape[0]
  height = image2.shape[1]
  x = int(((width *7)/10))
  y = int(((height *7)/10))
  img_cropped = cv2.resize(image2,(x,y))
  publish_cropped(img_cropped)
  
def receive_message(): 
  rospy.loginfo('cropping image')
  rospy.init_node('crop_node')
  rospy.Subscriber('webcam_img', Image, callback)
  rospy.spin()
  cv2.destroyAllWindows()
  
def publish_cropped(img_cropped):
  pub = rospy.Publisher('webcam_cropped', Image , queue_size=10)
  br = CvBridge()
  pub.publish(br.cv2_to_imgmsg(img_cropped))
             
if __name__ == '__main__':
  
  try:
    data = receive_message()
    
  except rospy.ROSInterruptException:
    pass