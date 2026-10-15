# pioneer_control

ROS 2 teleoperation and ultrasonic sensor visualization for the Pioneer 3-DX in CoppeliaSim.

## Prerequisites
- Ubuntu + ROS 2 (Humble/Jazzy), CoppeliaSim >= 4.5 with the simROS2 plugin
- `sudo apt install python3-matplotlib python3-tk python3-colcon-common-extensions`

## Build
```bash
mkdir -p ~/ros2_ws/src && cp -r pioneer_control ~/ros2_ws/src/
cd ~/ros2_ws && source /opt/ros/$ROS_DISTRO/setup.bash
colcon build --packages-select pioneer_control
source install/setup.bash
```

## CoppeliaSim setup
1. In a terminal with ROS 2 sourced, start CoppeliaSim (`./coppeliaSim.sh`).
2. Drag `models/robots/mobile/PioneerP3DX.ttm` into the scene; add walls/cuboids around it.
3. Right-click the robot > Add > Associated child script > Non-threaded > Lua.
4. Paste `coppelia/p3dx_ros2_script.lua`, then press Play.

## Run (each in its own terminal, after sourcing ROS and the workspace)
```bash
ros2 run pioneer_control teleop_node        # w/a/s/d, space = stop, q = quit
ros2 run pioneer_control sensor_viz_node    # live bar graph
```

## Debug
```bash
ros2 topic list
ros2 topic echo /ultrasonic_sensors
ros2 topic info /cmd_vel
```
