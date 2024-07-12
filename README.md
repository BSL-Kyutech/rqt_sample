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
   After that, the following GUI window will be launched.
   ![Screenshot from 2024-07-13 17-36-30](https://github.com/user-attachments/assets/498cc2b5-973e-4766-ad91-d0234aa314e2)

   In the sample RQt plugin, you can adjust and publish some values using sliders and a publish button.
