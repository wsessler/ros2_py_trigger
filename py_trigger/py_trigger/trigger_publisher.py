import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Bool

import time
import board
import digitalio

class TriggerPublisher(Node):

    def __init__(self):
        super().__init__('trigger_publisher')

        self.parameter_name__trigger_pin = 'trigger_pin'
        self.declare_parameter(self.parameter_name__trigger_pin, 'D4')       

        self.parameter_name__trigger_topic = 'trigger_topic'
        self.declare_parameter(self.parameter_name__trigger_topic, 'trigger')       

        self.parameter_name__polling_time = 'polling_time'
        self.declare_parameter(self.parameter_name__polling_time, 0.5)       

        self.publisher_ = self.create_publisher(Bool, 
                self.get_parameter(self.parameter_name__trigger_topic).get_parameter_value().string_value, 
                10)

        self.get_logger().info("trigger pin: " + self.get_parameter(self.parameter_name__trigger_pin).get_parameter_value().string_value)
        self.get_logger().info("trigger topic: " + self.get_parameter(self.parameter_name__trigger_topic).get_parameter_value().string_value)
        self.get_logger().info("polling time (double!): " + str(self.get_parameter(self.parameter_name__polling_time).get_parameter_value().double_value))
        self.get_logger().info("available pins: " + str(dir(board)))

        self.timer_period = self.get_parameter(self.parameter_name__polling_time).get_parameter_value().double_value # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.button = digitalio.DigitalInOut(getattr(board, 
            self.get_parameter(self.parameter_name__trigger_pin).get_parameter_value().string_value))
        self.button.direction = digitalio.Direction.INPUT

    def timer_callback(self):
        msg = Bool() #String()
        msg.data = bool(self.button.value)
        self.publisher_.publish(msg)
        self.get_logger().debug('Publishing: "%d"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    trigger_publisher = TriggerPublisher()

    rclpy.spin(trigger_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    trigger_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
