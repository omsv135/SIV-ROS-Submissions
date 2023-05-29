import rospy
from std_msgs.msg import String
import cv2,numpy as np 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from matplotlib import pyplot as plt
bridge=CvBridge()

def pos_callback(cropped_img_msg):
    final_image=bridge.imgmsg_to_cv2(cropped_img_msg,desired_encoding="bgr8")
    plt.imshow(final_image)
    plt.show()

def final():
    rospy.init_node('node3')
    rospy.loginfo("Node has started")
    rospy.Subscriber('Webcam_cropped',Image,callback=pos_callback)
    rospy.spin()

if __name__=='__main__':
    try:
        final()
    except rospy.ROSInterruptException:
        pass    