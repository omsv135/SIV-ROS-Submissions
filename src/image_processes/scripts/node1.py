import rospy 
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2,numpy as np 
from cv_bridge import CvBridge

bridge=CvBridge()
im=cv2.imread('/home/aniket/catkin_ws/src/image_processes/scripts/2023-05-26-105727.jpg')

def img():
    rospy.init_node('node1')
    rospy.loginfo("Node1 has started")
    #print(str(im.shape))
    
    img_msg = bridge.cv2_to_imgmsg(im, encoding="bgr8")
    pub=rospy.Publisher('Webcam_img',Image,queue_size=10)
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("hey there")
        pub.publish(img_msg)
        rate.sleep()

if __name__=='__main__':
    try:
        img()
    except rospy.ROSInterruptException:
        pass    

