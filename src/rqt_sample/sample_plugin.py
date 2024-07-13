# coding: UTF-8

from qt_gui.plugin import Plugin
from python_qt_binding.QtCore import QTimer

from rqt_sample.sample_widget import SampleWidget


# ros2 msg
from std_msgs.msg import Float32MultiArray


# RQtプラグインのオブジェクト
class SamplePlugin(Plugin):

    def __init__(self, context):
        super(SamplePlugin, self).__init__(context)
        # Pluginの名前
        self.setObjectName('Sample')

        # ノードなどが入ったPluginの中身
        self._context = context

        # publisher関連のパラメータ
        self.freq = 20
        self.qos = 10

        # Qt（GUI）オブジェクトの作成
        self._widget = SampleWidget()
        
        if context.serial_number() > 1:
            self._widget.setWindowTitle(
                'Sample'
            )
                #self._widget.windowTitle('') + (' (%d)' % context.serial_number())) 
        
        # RQtプラグインにGUIを埋め込み
        context.add_widget(self._widget)

        # 
        self._timer = QTimer()
        self._timer.timeout.connect(self._widget.update)
        self._timer.start(16)

        # ノードのpublisherを作成
        topicname = '/sample_plugin/talker1'
        self.sample_pub = self._context.node.create_publisher(Float32MultiArray, topicname, self.qos)

        # ノードの callback　関数を作成
        self.timer_period = 1/self.freq
        self._context.node.create_timer(self.timer_period, self.timer_callback)

        # get current time from node
        self.current_time = self._context.node.get_clock().now().to_msg()

    def timer_callback(self):
        # get current time from node
        self.current_time = self._context.node.get_clock().now().to_msg()

        # publish message when a button is pushed
        # ボタンが押されたときにpublish
        if self._widget.sample_pub_flag:
            # restore the publish flug
            self._widget.sample_pub_flag = False
            # publish
            # Qt(GUI)オブジェクトで設定された値を取り出してpublish
            self.sample_publish(self._widget.send_value)
            

        return 0


    # publish用の関数
    def sample_publish(self, value):
        msg = Float32MultiArray()
        value = value.tolist()
        msg.data = value
        
        self.sample_pub.publish(msg)


    def shutdown_plugin(self):
        
        self._timer.stop()
        pass


    def save_settings(self, plugin_settings, instance_settings):
        
        pass


    def restore_settings(self, plugin_settings, instance_settings):
        
        pass