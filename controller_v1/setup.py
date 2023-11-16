from setuptools import find_packages, setup

package_name = 'controller_v1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test','src']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nkcong206',
    maintainer_email='nkcong206@gmail.com',
    description='ROS2 controller_v1',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'led = controller_v1.led_v1:main',
            'socketio = controller_v1.socketio_v1:main',
            'gps = controller_v1.gps_v1:main',
            'controller = controller_v1.controller_v1:main',
        ],
    },
)