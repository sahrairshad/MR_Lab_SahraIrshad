import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')

        # -------------------------
        # Task 1: Welcome message
        # -------------------------
        self.get_logger().info('Welcome to Mobile Robotics Lab')

        # -------------------------
        # Task 2: Counter
        # -------------------------
        self.file_path = os.path.join(os.path.dirname(__file__), 'counter.txt')
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.count = int(f.read())
        else:
            self.count = 0

        self.count += 1
        with open(self.file_path, 'w') as f:
            f.write(str(self.count))
        self.get_logger().info(f'Run count: {self.count}')

        # -------------------------
        # Task 3: Parameter student_name
        # -------------------------
        self.declare_parameter('student_name', '')
        name = self.get_parameter('student_name').value
        if name:
            self.get_logger().info(f'Student: {name}')
        else:
            self.get_logger().info('student_name not set')

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin(node)  # <--- keep node alive to show all messages
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
