import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class Turtlebot3Avoidance(Node):
    def __init__(self):
        super().__init__('turtlebot3_avoidance_node')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, 'scan', self.scan_callback, 10)
        self.twist = Twist()

    def scan_callback(self, msg):
       
        scan_range = msg.ranges[0:30] + msg.ranges[330:360]
        min_distance = min(scan_range)

        if min_distance < 0.5: 
            self.get_logger().info('Object Detected! Turning...')
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.5
        else:
            self.twist.linear.x = 0.15
            self.twist.angular.z = 0.0
            
        self.publisher.publish(self.twist)

def main():
    rclpy.init()
    node = Turtlebot3Avoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
