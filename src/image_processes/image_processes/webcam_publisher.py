#!/usr/bin/env python3
'''from cv2 import IMWRITE_JPEG_OPTIMIZE, destroyWindow, imshow, imwrite, waitKey
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class WebcamPublisher(Node):
    def __init__(self):
        super().__init__('webcam_publisher')
        self.publisher_ = self.create_publisher(Image, 'webcam_img', 10)
        self.timer_ = self.create_timer(0.1, self.publish_frame)
        self.cv_bridge = CvBridge()
        self.capture = cv2.VideoCapture(0)

    def publish_frame(self):
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to a ROS2 Image message
            msg = self.cv_bridge.cv2_to_imgmsg(frame)

            # Publish the image frame
            self.publisher_.publish(msg)

   
        
      
   
def main(args=None):
    rclpy.init(args=args)
    webcam_publisher = WebcamPublisher()
    rclpy.spin(webcam_publisher)
    webcam_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

  '''
'''import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def node1():
    rospy.init('node1',anonymous=True)
    Srate = rospy.Rate(10)
    pub = rospy.Publisher('Webcam_img',Image,queue_size=10)
    bridge = CvBridge()

    while not rospy.is_shoutdown():
        image_frame = capture_image_from_webcam()

        ros_image = bridge.cv2_to_imgmsg(image_frame,encoding='bgr8')

        pub.publish(ros_image)
        rate.sleep()

def capture_image_from_webcam():
    cap=cv2.VideoCapture(0)
    cv2.waitKey(0)

    if not cap.isOpened():
        print("failed to open the webcam")
        return None
    ret, frame = cap.read()

    cap.release()

    if not ret:
        print("Failed to capture frame from the webcam")
        return None
    return frame

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
           




import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def node1():
    rclpy.init()
    node = rclpy.create_node('node1')
    rate = node.create_rate(10)

    publisher = node.create_publisher(Image, 'Webcam_img', 10)
    bridge = CvBridge()

    while rclpy.ok():
        image_frame = capture_image_from_webcam()

        ros_image = bridge.cv2_to_imgmsg(image_frame, encoding='bgr8')

        publisher.publish(ros_image)
        rate.sleep()

    node.destroy_node()
    rclpy.shutdown()

def capture_image_from_webcam():
    cap = cv2.VideoCapture(0)
    cv2.waitKey(0)

    if not cap.isOpened():
        print("Failed to open the webcam")
        return None
    ret, frame = cap.read()

    cap.release()

    if not ret:
        print("Failed to capture frame from the webcam")
        return None
    return frame

if __name__ == '__main__':
    try:
        node1()
    except KeyboardInterrupt:
        pass
'''

'''import os
import sys
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Video
from cv_bridge import CvBridge

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Video, 'webcam_img', 10)
        self.bridge = CvBridge()

    def publish_image(self):
        # Path to the image file
        image_file = '/home/garima/first_ws/src/image_processes/image_processes/sample.jpg'

        # Load the image using OpenCV
        image = cv2.imread(image_file)
        if image is None:
            self.get_logger().error('Failed to load image from file: {}'.format(image_file))
            sys.exit(1)

        # Convert the image to a ROS Image message
        img_msg = self.bridge.cv2_to_imgmsg(image, encoding="bgr8")

        while True:
            # Publish the image message
            self.publisher_.publish(img_msg)
            self.get_logger().info('Image published to webcam_img topic')

            # Sleep for a while before publishing the next image
           #we rclpy.sleep(1.0)  # 1 second

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    image_publisher.publish_image()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
'''

#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image, 'webcam_img', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.bridge = CvBridge()
        self.video = cv2.VideoCapture('/home/garima/Downloads/sample.mp4')

    def timer_callback(self):
        ret, frame = self.video.read()
        if not ret:
            # If the video is over, loop back to the beginning
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.video.read()
            if not ret:
                # If the video still cannot be read, stop publishing
                self.get_logger().info('Video cannot be read')
                self.timer.cancel()
                return

        # Convert the frame to a ROS Image message
        image_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')

        # Publish the image message
        self.publisher_.publish(image_msg)
        self.get_logger().info('Published image')

def main(args=None):
    rclpy.init(args=args)
    video_publisher = VideoPublisher()
    rclpy.spin(video_publisher)
    video_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
