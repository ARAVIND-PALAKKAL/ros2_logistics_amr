#!/bin/bash
set -e

# Source ROS2
source /opt/ros/jazzy/setup.bash

# Source workspace
source /ros2_ws/install/setup.bash

# Set middleware
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

exec "$@"