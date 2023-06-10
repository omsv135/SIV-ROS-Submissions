#!/usr/bin/env python3
'''import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class node2(Node):
    def __init__(self):
        super().__init__('webcam_subscriber')
        self.subscription_ = self.create_subscription(
            Image,
            'Webcam_img',
            self.process_image,
            10
        )
        self.publisher_ = self.create_publisher(Image, 'webcam_cropped', 10)
        self.bridge = CvBridge()

    def process_image(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        height, width, _ = frame.shape
        crop_width = int(width * 0.3)
        crop_height = int(height * 0.3)
        cropped_frame = frame[crop_height:-crop_height, crop_width:-crop_width]

        cropped_msg = self.bridge.cv2_to_imgmsg(cropped_frame, encoding='bgr8')
        self.publisher_.publish(cropped_msg)

def main(args=None):
    rclpy.init(args=args)
    webcam_subscriber = node2()
    rclpy.spin(webcam_subscriber)
    webcam_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    '''

'''import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
pub = rospy.Publisher('Webcam_cropped',Image ,queue_size=10)
def node2():
    rospy.init_node('node2',anonymous=True)
    rate = rospy.Rate(10)

    rospy.Subscriber('Webcam_img',Image,process_image_callback)

    while not rospy.is_shoutdown():
        rate.sleep()

def process_image_callback(image_frame):
    cv_bridge = CvBridge()
    cv_image = cv_bridge.imgmsg_to_cv2(image_frame,desired_encoding='bgr8')

    height,width = cv_image.shape[:2]
    new_width = int(width*0.7)
    new_height = int(height*0.7)
    start_x = int((width-new_width)/2)
    start_y = int((height-new_height)/2)
    cropped_image - cv_bridge[start_y:start_y + new_height , start_x = start_x + new_width]
    image_frame  = cv_bridge.cv2_to_imgmsg(cropped_image,encoding = 'bgr8')

    pub.publish(image_frame)
    if __name__ = '__main__':
        try:
           node2()
        

        except rospy.ROSInterruptException:
            pass'''

'''import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def node2():
    rclpy.init()
    node = rclpy.create_node('node2')
    rate = node.create_rate(10)

    publisher = node.create_publisher(Image, 'Webcam_cropped', 10)
    cv_bridge = CvBridge()

    def process_image_callback(image_frame):
        cv_image = cv_bridge.imgmsg_to_cv2(image_frame, desired_encoding='bgr8')

        height, width = cv_image.shape[:2]
        new_width = int(width * 0.7)
        new_height = int(height * 0.7)
        start_x = int((width - new_width) / 2)
        start_y = int((height - new_height) / 2)
        cropped_image = cv_image[start_y:start_y + new_height, start_x:start_x + new_width]
        cropped_image_frame = cv_bridge.cv2_to_imgmsg(cropped_image, encoding='bgr8')

        publisher.publish(cropped_image_frame)

    subscription = node.create_subscription(Image, 'Webcam_img', process_image_callback, 10)

    while rclpy.ok():
        rclpy.spin_once(node)
        rate.sleep()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    try:
        node2()
    except KeyboardInterrupt:
        pass
'''
#!/usr/bin/env python3

'''import os
import sys
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'webcam_img',
            self.image_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(Image, 'webcam_cropped', 10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            # Convert the ROS Image message to an OpenCV image
            image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error('Failed to convert image: {}'.format(e))
            return

        # Crop the image by 30%
        height, width, _ = image.shape
        crop_width = int(width * 0.3)
        crop_height = int(height * 0.3)
        cropped_image = image[crop_height:height-crop_height, crop_width:width-crop_width]

        try:
            # Convert the cropped image back to a ROS Image message
            cropped_msg = self.bridge.cv2_to_imgmsg(cropped_image, encoding='bgr8')
        except Exception as e:
            self.get_logger().error('Failed to convert cropped image: {}'.format(e))
            return

        # Publish the cropped image on the "webcam_cropped" topic
        self.publisher_.publish(cropped_msg)
        self.get_logger().info('Cropped image published to webcam_cropped topic')

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
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
import os

class ImageCropper(Node):
    def __init__(self):
        super().__init__('image_cropper')
        self.subscription = self.create_subscription(
            Image,
            'webcam_img',
            self.image_callback,
            10
        )
        self.publisher_ = self.create_publisher(Image, 'cropped_img', 10)
        self.bridge = CvBridge()
        self.screen_width = 800  # Specify the desired screen width
        self.screen_height = 600  # Specify the desired screen height
        self.crop_width = 100  # Specify the desired crop width in pixels
        self.crop_height = 100  # Specify the desired crop height in pixels

    def image_callback(self, msg):
        # Convert the ROS Image message to a CV image
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Get the original image dimensions
        height, width, _ = cv_image.shape

        # Calculate the crop coordinates
        x = int((width - self.crop_width) / 2)
        y = int((height - self.crop_height) / 2)

        # Crop the image
        cropped_image = cv_image[y:y+self.crop_height, x:x+self.crop_width]

        # Resize the cropped image to fit within the screen dimensions while preserving aspect ratio
        aspect_ratio = float(self.screen_width) / self.screen_height
        cropped_image = self.resize_image(cropped_image, self.screen_width, int(self.screen_width / aspect_ratio))

        # Convert the resized image back to a ROS Image message
        cropped_msg = self.bridge.cv2_to_imgmsg(cropped_image, encoding='bgr8')

        # Publish the cropped image
        self.publisher_.publish(cropped_msg)
        self.get_logger().info('Published cropped image')

    def resize_image(self, image, width, height):
        # Resize the image while preserving aspect ratio
        image_height, image_width, _ = image.shape
        if image_width / image_height > width / height:
            new_height = height
            new_width = int(image_width * height / image_height)
        else:
            new_width = width
            new_height = int(image_height * width / image_width)
        resized_image = cv2.resize(image, (new_width, new_height))
        return resized_image

def main(args=None):
    rclpy.init(args=args)
    os.environ['QT_QPA_PLATFORM'] = 'wayland'  # Set the QT_QPA_PLATFORM to 'wayland'
    image_cropper = ImageCropper()
    rclpy.spin(image_cropper)
    image_cropper.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
