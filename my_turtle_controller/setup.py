from setuptools import setup

package_name = 'my_turtle_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your-email@example.com',
    description='Simple ROS2 node to control turtlesim',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'turtle_move = my_turtle_controller.turtle_move:main',
        ],
    },
)

