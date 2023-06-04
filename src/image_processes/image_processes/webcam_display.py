#!/usr/bin/env python3
'''import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class node3(Node):
    def __init__(self):
        super().__init__('webcam_display')
        self.subscription_ = self.create_subscription(
            Image,
            'webcam_cropped',
            self.display_image,
            10
        )
        self.bridge = CvBridge()

    def display_image(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        cv2.imshow('Webcam Cropped', frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    webcam_display = node3()
    rclpy.spin(webcam_display)
    webcam_display.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()'''

'''import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def node3():
    rospy,init_node('node3',anonymous = True)
    rospy.Subscriber('Webcam_cropped',Image,show_image_callback)

    rospy.spin()

def show_image_callback(image_frame):
    cv_bridge = CvBridge()
    cv_image = cv_bridge.imgmsg_to_cv2(image_frame,desired_encoding='bgr8')
    cv2.imshow('Webcam_cropped',cv_image)
    cv2.waitkey(1)

if __name__ = '__main__':
    try:
           node3()
    except rospy.ROSInterruptException:
         pass
'''

'''import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def node3():
    rclpy.init()
    node = rclpy.create_node('node3')

    cv_bridge = CvBridge()

    def show_image_callback(image_frame):
        cv_image = cv_bridge.imgmsg_to_cv2(image_frame, desired_encoding='bgr8')
        cv2.imshow('Webcam_cropped', cv_image)
        cv2.waitKey(1)

    subscription = node.create_subscription(Image, 'Webcam_cropped', show_image_callback, 10)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    try:
        node3()
    except KeyboardInterrupt:
        pass
        '''

#!/usr/bin/env python3
#!/usr/bin/env python3

'''import os
import sys
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        self.subscription = self.create_subscription(
            Image,
            'webcam_cropped',
            self.image_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            # Convert the ROS Image message to an OpenCV image
            image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error('Failed to convert image: {}'.format(e))
            return

        # Display the image in a window
        cv2.imshow('Webcam Cropped', image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    image_viewer = ImageViewer()
    rclpy.spin(image_viewer)
    cv2.destroyAllWindows()
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

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        self.subscription = self.create_subscription(
            Image,
            'cropped_img',
            self.image_callback,
            10
        )
        self.bridge = CvBridge()

    def image_callback(self, msg):
        # Convert the ROS Image message to a CV image
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Display the image
        cv2.imshow('Cropped Image', cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    image_viewer = ImageViewer()
    try:
        rclpy.spin(image_viewer)
    except KeyboardInterrupt:
        pass

    # Destroy the OpenCV windows and clean up
    cv2.destroyAllWindows()
    image_viewer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
