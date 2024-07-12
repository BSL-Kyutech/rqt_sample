# rqt_sample
A ros2 package of sample RQt plugin.
This package provides a simple GUI to ROS2 GUI developers.

# How to use
1. Create a workspace and clone rqt_sample pacakge
1. Load setups
   ```
   # in a workspace
   colcon build --packages-select rqt_sample
   . install/setup.bash
   ```
1. Apply the sample RQt plugin to RQt
   ```
   rqt --force-discover
   ```
1. Launch the sample GUI node by stand-alone mode.
   ```
   ros2 run rqt_sample sample
   ```
   After this command, a GUI windows will be open.
   In the RQt sample plugin, you can adjust and publish some values using sliders and a publish button.
