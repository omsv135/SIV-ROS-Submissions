from setuptools import find_packages, setup

package_name = 'image_processes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='garima',
    maintainer_email='garima@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "webcam_publisher = image_processes.webcam_publisher:main",
            "webcam_subscriber = image_processes.webcam_subscriber:main",
            "webcam_display = image_processes.webcam_display:main",
        ],
    },
)
