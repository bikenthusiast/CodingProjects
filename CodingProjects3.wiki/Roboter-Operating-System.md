# ROS wiki

### Starting the usb_cam node
`roslaunch usb_cam usb_cam-test.launch`

The launch-file looks like:

```bash
<launch>
  <node name="usb_cam" pkg="usb_cam" type="usb_cam_node" output="screen" >
    <param name="video_device" value="/dev/video0" />
    <param name="image_width" value="640" />
    <param name="image_height" value="480" />
    <param name="pixel_format" value="yuyv" />
    <param name="camera_frame_id" value="usb_cam" />
    <param name="io_method" value="mmap"/>
  </node>
  <node name="image_view" pkg="image_view" type="image_view" respawn="false" output="screen">
    <remap from="image" to="/usb_cam/image_raw"/>
    <param name="autosize" value="true" />
  </node>
</launch>
```

# Sourcing your workspace

Loosely adhering to the following [tutorial](https://answers.ros.org/question/206876/how-often-do-i-need-to-source-setupbash/)

Autonomous sourcing of terminal-sessions:

1. Open your terminal
2. Enter ` gedit ~/.bashrc`
3. File will open on gedit
4. Go to the bottom (my last line was "source /opt/ros/indigo/setup.bash" , for others it may differ)
5. Add your PATH --> `source [YOUR PATH]/catkin_ws/devel/setup.bash`
6. Save and exit

Now with every new shell you open, it will source automatically
