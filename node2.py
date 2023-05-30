#!/usr/bin/env python3
import cv2
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image
pub = rospy.Publisher('Webcam_cropped', Image, queue_size=10)
def node2():
    rospy.init_node('node2', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    
    rospy.Subscriber('Webcam_img', Image, process_image_callback)

    while not rospy.is_shutdown():
        rate.sleep()

def process_image_callback(image_frame):
    # Crop the image frame by 30% in pixels
    cv_bridge = CvBridge()
    cv_image = cv_bridge.imgmsg_to_cv2(image_frame, desired_encoding='bgr8')
    
    height, width = cv_image.shape[:2]
    new_width = int(width*0.7)
    new_height = int(height*0.7)
    start_x = int((width - new_width) / 2)
    start_y = int((height - new_height) / 2)
    cropped_image = cv_image[start_y:start_y + new_height, start_x:start_x + new_width]
    image_frame= cv_bridge.cv2_to_imgmsg(cropped_image, encoding='bgr8')

    # Publish the cropped image
    pub.publish(image_frame)

#def crop_image(image):
    
    # Crop the image by 30% in pixels using appropriate image processing libraries
    # Return the cropped image

if __name__ == '__main__':
    try:
        node2()
  
  
    except rospy.ROSInterruptException:
        pass