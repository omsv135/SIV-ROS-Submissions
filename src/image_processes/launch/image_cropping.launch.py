#!/usr/bin/env python3

from launch import LaunchDescription, LaunchService
import launch
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    webcam_publisher = Node(
        package='image_processes',
        executable='webcam_publisher',
        output='screen'
    )

    image_cropper = Node(
        package='image_processes',
        executable='webcam_subscriber',
        output='screen'
    )

    image_display = Node(
        package='image_processes',
        executable='webcam_display',
        output='screen'
    )

    return LaunchDescription([
        webcam_publisher,
        image_cropper,
        image_display
    ])


if __name__ == '__main__':
    ld = generate_launch_description()
    ls = LaunchService()
    ls.include_launch_description(ld)
    ls.run()
