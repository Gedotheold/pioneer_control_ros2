import sys
import select
import termios
import tty
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

HELP_MSG = """
-----------------------------------------
Pioneer 3-DX Teleoperation Console
-----------------------------------------
Control Keys:
   w : Move Forward
   s : Move Backward
   a : Turn Left
   d : Turn Right

   spacebar : STOP
   q : Quit Node
-----------------------------------------
"""

class TeleopNode(Node):
    def __init__(self):
        super().__init__('teleop_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Velocity defaults
        self.declare_parameter('linear_speed', 0.4)   # m/s
        self.declare_parameter('angular_speed', 1.0)  # rad/s
        
        self.linear_speed = self.get_parameter('linear_speed').value
        self.angular_speed = self.get_parameter('angular_speed').value

    def publish_velocity(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = float(linear_x)
        msg.angular.z = float(angular_z)
        self.publisher_.publish(msg)

def get_key(settings, timeout=0.1):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main(args=None):
    rclpy.init(args=args)
    node = TeleopNode()
    
    # Save terminal settings for raw key input reading
    settings = termios.tcgetattr(sys.stdin)
    
    key_mapping = {
        'w': (node.linear_speed, 0.0),
        's': (-node.linear_speed, 0.0),
        'a': (0.0, node.angular_speed),
        'd': (0.0, -node.angular_speed),
        ' ': (0.0, 0.0),
    }

    print(HELP_MSG)
    try:
        while rclpy.ok():
            key = get_key(settings)
            
            if key == 'q' or key == '\x03':  # 'q' or Ctrl+C
                break
                
            if key in key_mapping:
                lin, ang = key_mapping[key]
                node.publish_velocity(lin, ang)
                
    except Exception as e:
        print(f"Error reading keyboard input: {e}")
        
    finally:
        # Publish zero velocity before exiting to stop the robot safely
        node.publish_velocity(0.0, 0.0)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
