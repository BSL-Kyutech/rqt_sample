import sys
from rqt_gui.main import Main

def main():
    main_obj = Main()
    sys.exit(main_obj.main(sys.argv, standalone='rqt_sample.sample_plugin.SamplePlugin', plugin_argument_provider=None))