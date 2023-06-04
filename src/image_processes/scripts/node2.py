import rospy 
from std_msgs.msg import String
import cv2,numpy as np 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
#from matplotlib import pyplot as plt
bridge=CvBridge()
global cropped_img_msg

def callback(image_msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image_msg, desired_encoding="bgr8")
    height, width, _ = cv_image.shape
    cropped_image = cv_image[int(height * 0.3):, :]
    cropped_img_msg = bridge.cv2_to_imgmsg(cropped_image, encoding="bgr8")
    cropped=rospy.Publisher('Webcam_cropped',Image,queue_size=10)
    cropped.publish(cropped_img_msg)
    rospy.loginfo("hey")
def imgcropper():
    rospy.init_node('node2')
    rospy.loginfo("Node has started")
    rospy.Subscriber('Webcam_img',Image,callback=callback)
    # cropped=rospy.Publisher('Webcam_cropped',Image,queue_size=10)
    # cropped.publish(cropped_img_msg)
    rospy.spin()

if __name__=='__main__':
    try:
        imgcropper()
    except rospy.ROSInterruptException:
        pass       