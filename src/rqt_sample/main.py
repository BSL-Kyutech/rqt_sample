import sys
from rqt_gui.main import Main

def main():
    main_obj = Main()
    # スタンドアローン起動（単独のwindowでGUIを起動）用の設定
    sys.exit(main_obj.main(sys.argv, standalone='rqt_sample.sample_plugin.SamplePlugin', plugin_argument_provider=None))


if __name__=='__main__':
    main()