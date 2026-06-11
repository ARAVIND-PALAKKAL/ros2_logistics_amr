# ROS2 Autonomous Logistics AMR

![ROS2](https://img.shields.io/badge/ROS2-Jazzy-blue)
![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![CI](https://github.com/ARAVIND-PALAKKAL/ros2_logistics_amr/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

An autonomous mobile robot (AMR) for warehouse logistics applications built with ROS2 Jazzy, Gazebo Harmonic, and Nav2. The robot autonomously navigates a warehouse environment using SLAM-generated maps and AMCL localization.

---

## Demo

[![Demo Video](https://img.shields.io/badge/Demo-YouTube-red)](https://youtu.be/4QUJeFePTSY)

> Robot navigating autonomously between 4 waypoints in a warehouse environment with shelf obstacles using Nav2 and AMCL localization.

---

## Features

- **Autonomous Navigation** — Nav2 stack with AMCL localization and NavFn global planner
- **SLAM Mapping** — Real-time warehouse map generation using SLAM Toolbox
- **Sim-to-Real Ready** — Full ROS2 Jazzy + Gazebo Harmonic pipeline with ros2_control hardware interfaces
- **Containerised** — Complete Docker stack for reproducible deployment
- **CI/CD** — GitHub Actions pipeline that builds and tests on every push
- **Warehouse World** — Custom Gazebo SDF environment with walls and shelf obstacles

---

## Architecture

---

## Stack

| Component | Technology |
|-----------|-----------|
| Robot OS | ROS2 Jazzy |
| Simulation | Gazebo Harmonic 8.x |
| Navigation | Nav2 (AMCL + NavFn + RegPP Controller) |
| SLAM | SLAM Toolbox |
| Hardware Interface | ros2_control + diff_drive |
| Containerisation | Docker + docker-compose |
| CI/CD | GitHub Actions |
| Language | Python, C++ |

---

## Project Structure
---

## Quick Start

### Prerequisites
- Ubuntu 24.04
- ROS2 Jazzy
- Gazebo Harmonic
- Docker (optional)

### Install dependencies

```bash
sudo apt install -y \
  ros-jazzy-navigation2 \
  ros-jazzy-nav2-bringup \
  ros-jazzy-slam-toolbox \
  ros-jazzy-ros-gz \
  ros-jazzy-rmw-cyclonedds-cpp \
  python3-colcon-common-extensions
```

### Build

```bash
git clone https://github.com/ARAVIND-PALAKKAL/ros2_logistics_amr.git
cd ros2_logistics_amr
colcon build --symlink-install
source install/setup.bash
```

### Run

**Terminal 1 — Gazebo simulation:**
```bash
ros2 launch amr_bringup amr_gazebo.launch.py
```

**Terminal 2 — Nav2 autonomous navigation:**
```bash
ros2 launch amr_bringup nav2.launch.py
```

**Terminal 3 — RViz visualisation:**
```bash
ros2 run rviz2 rviz2
```

Set Fixed Frame to `map`, add `/map` and `/scan` topics, then use **2D Goal Pose** to send navigation goals.

### Docker

```bash
cd docker
docker-compose up
```

---

## How It Works

1. **Robot spawns** in a Gazebo warehouse world with walls and shelves
2. **SLAM Toolbox** builds a 2D occupancy map as the robot explores
3. **AMCL** localises the robot on the saved map using lidar scan matching
4. **Nav2** plans a collision-free path and executes it using the Regulated Pure Pursuit controller
5. **ros2_control** sends velocity commands to the differential drive plugin

---

## Author

**Aravind Palakkal**
M.Sc. Elektromobilität-ACES — FAU Erlangen-Nürnberg
[LinkedIn](https://www.linkedin.com/in/aravind-palakkal-tech/)