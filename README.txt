=====================================================
TURTLEBOT 3 - OBSTACLE AVOIDANCE PROJECT 
=====================================================

1. Dependencies Installation:
sudo apt update
sudo apt install ros-humble-turtlebot3-gazebo ros-humble-turtlebot3-msgs

2. Setup Environment:
export TURTLEBOT3_MODEL=burger

3. Build and Run:
cd ~/ros2_ws
colcon build --packages-select turtlebot3_avoidance
source install/setup.bash

4. Execution:
- Terminal 1: ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
- Terminal 2: ros2 run turtlebot3_avoidance avoid_obstacles
