# pioneer_control_ros2

A ROS 2 package for teleoperating a Pioneer 3-DX mobile robot in CoppeliaSim, featuring real-time ultrasonic sensor data visualization using Matplotlib[cite: 1, 3].

## System Overview

The system consists of three primary components communicating via ROS 2 topics:
*   **Keyboard Teleoperation Node (`teleop_node.py`):** A Python node that captures terminal keystrokes and publishes `geometry_msgs/msg/Twist` messages to control the robot's movement[cite: 1, 2].
*   **CoppeliaSim Simulator:** Hosts the Pioneer 3-DX robot model, subscribes to the Twist messages to drive the wheels, and publishes range data from 16 ultrasonic sensors[cite: 1].
*   **Sensor Visualization Node (`sensor_viz_node.py`):** A Python node that subscribes to the ultrasonic sensor data and utilizes Matplotlib to display a continuously updating real-time bar graph of the readings[cite: 1, 3].

## Prerequisites

Ensure the following software and libraries are installed before running the package:
*   **ROS 2:** Installed and sourced.
*   **CoppeliaSim:** Simulator installed with the `simROS2` plugin enabled[cite: 3].
*   **Python Dependencies:**
    *   `rclpy`[cite: 2]
    *   `geometry_msgs`[cite: 2]
    *   `std_msgs` or `sensor_msgs`[cite: 2]
    *   `matplotlib` (for real-time plotting)[cite: 3]
    *   `pynput` or `curses` (recommended for non-blocking keyboard input)[cite: 3]

## Setup and Installation

1. Create a ROS 2 workspace (if you don't already have one) and clone this package into the `src` directory:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   # Clone repository here
   ```
2. Build the `pioneer_control` package[cite: 2, 4]:
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select pioneer_control
   ```
3. Source the workspace:
   ```bash
   source install/setup.bash
   ```

## Usage Instructions

### 1. Launch CoppeliaSim
1. Open the CoppeliaSim application[cite: 2].
2. From the Model Browser, import the Pioneer 3-DX model located at `Models/mobile/Pioneer p3dx.ttm`[cite: 2].
3. Add walls or objects to the environment to test the ultrasonic sensors[cite: 2].
4. Start the simulation.

### 2. Run the Teleoperation Node
In a new sourced terminal, run the teleoperation node to drive the robot:
```bash
ros2 run pioneer_control teleop_node
```
*   Use standard directional keys (e.g., 'w', 'a', 's', 'd') to publish linear and angular velocities[cite: 2].
*   Press the designated stop key (e.g., spacebar) to publish a zero-velocity Twist message and halt the robot[cite: 2].

### 3. Run the Sensor Visualization Node
In another sourced terminal, launch the visualization node:
```bash
ros2 run pioneer_control sensor_viz_node
```
A Matplotlib window will open, displaying a 16-bar graph that dynamically updates as the robot approaches obstacles in the simulator[cite: 1, 3].

