from setuptools import find_packages, setup

package_name = 'amr_controller'

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
    maintainer='aravind',
    maintainer_email='aravind.jpalakkal@gmail.com',
    description='AMR controller nodes',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odom_tf_broadcaster = amr_controller.odom_tf_broadcaster:main',
            'initial_pose_publisher = amr_controller.initial_pose_publisher:main',
        ],
    },
)