# coding: UTF-8

from qt_gui.plugin import Plugin
from python_qt_binding.QtCore import QTimer

from rqt_sample.sample_widget import SampleWidget


# ros2 msg
from std_msgs.msg import Float32MultiArray


class SamplePlugin(Plugin):

    def __init__(self, context):
        super(Sample, self).__init__(context)
        self.setObjectName('Sample')

        self._context = context
        self.freq = 20
        self.qos = 10

        # set sample widget
        self._widget = SampleWidget()
        if context.serial_number() > 1:
            self._widget.setWindowTitle(
                self._widget.windowTitle('') + (' (%d)' % context.serial_number())) 
        context.add_widget(self._widget)

        # 
        self._timer = QTimer()
        self._timer.timeout.connect(self._widget.update)
        self._timer.start(16)

        # create publisher
        topicname = '/sample_plugin/talker1'
        self.sample_pub = self._context.node.create_publisher(Float32MultiArray, topicname, self.qos)

        # create timer_callback 
        self.timer_period = 1/self.freq
        self._context.node.create_timer(self.timer_period, self.timer_callback)

        # get current time from node
        self.current_time = self._context.node.get_clock().now().to_msg()

    def timer_callback(self):
        # get current time from node
        self.current_time = self._context.node.get_clock().now().to_msg()

        # publish message when a button is pushed
        if self._widget.sample_pub_flag:
            # restore the publish flug
            self._widget.sample_pub_flag = False
            # publish
            self.publish_array(self._widget.send_value)
            

        return 0

    def sample_publish(self, value):
        msg = Float32MultiArray()
        value = value.tolist()
        #msg = Float32MultiArray(value)
        #msg.header.stamp = self.current_time
        #msg.layout.dim = len(value)
        #msg.layout.
        msg.data = value
        
        self.sample_pub.publish(msg)


    def shutdown_plugin(self):
        
        self._timer.stop()
        pass


    def save_settings(self, plugin_settings, instance_settings):
        
        pass


    def restore_settings(self, plugin_settings, instance_settings):
        
        pass
