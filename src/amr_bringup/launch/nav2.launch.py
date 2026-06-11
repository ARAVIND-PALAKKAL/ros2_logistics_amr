import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    nav2_params_file = os.path.join(
        os.path.expanduser('~'),
        'ros2_logistics_amr', 'src', 'amr_navigation', 'config', 'nav2_params.yaml')
    map_file = os.path.join(
        os.path.expanduser('~'),
        'ros2_logistics_amr', 'maps', 'warehouse_map.yaml')

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
        ]),
        launch_arguments={
            'map': map_file,
            'use_sim_time': 'true',
            'params_file': nav2_params_file,
            'use_composition': 'True',
            'use_respawn': 'False',
        }.items()
    )

    initial_pose = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='amr_controller',
                executable='initial_pose_publisher',
                name='initial_pose_publisher',
                output='screen',
                parameters=[{'use_sim_time': True}]
            )
        ]
    )

    return LaunchDescription([
        nav2,
        initial_pose,
    ])