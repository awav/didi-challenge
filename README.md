DIDI Challenge
===

## Naive visualization

It is completely based on ROS rviz and applicable only for DIDI challenge dataset version 1.

1. Install ROS-kinetic (I used Ubuntu 16.04.02), official instruction is [here](http://wiki.ros.org/kinetic/Installation/Ubuntu)
Install everything:
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-get update
sudo apt-get install ros-kinetic-*
sudo apt-get install python-rosinstall
```
  Install only needed packages
```bash
sudo apt-get install ros-kinetic-desktop
sudo apt-get install ros-kinetic-velodyne-*
sudo apt-get install python-rosinstall
```

2. I do not like to include extraneous bash scripts into `~/.bash`, so you need either to add this line to `.bashrc` or type into terminal:
```
source /opt/ros/kinetic/setup.bash
```

3. Run `roscore` and `rviz` application:
```bash
roscore &
rosrun rviz rviz -f velodyne -d didi.rviz
```

4. Play `rosbag` files:
```bash
rosbag play --loop BAG_FILE
```

## Rosbag content

Content example of the dataset #2:

```yaml
$ rosbag info --yaml data-2/Data/2/3_f.bag
path: data-2/Data/2/3_f.bag
version: 2.0
duration: 21.515603
start: 1490992759.483720
end: 1490992780.999323
size: 822761554
messages: 37446
indexed: True
compression: none
types:
    - type: bond/Status
      md5: eacc84bf5d65b6777d4c50f463dfb9c8
    - type: dataspeed_can_msgs/CanMessageStamped
      md5: 33747cb98e223cafb806d7e94cb4071f
    - type: dbw_mkz_msgs/BrakeInfoReport
      md5: fc88af128b5b3213ea25ab325a9b3bbb
    - type: dbw_mkz_msgs/BrakeReport
      md5: a306c167d365176ae6159e3c4e3f3197
    - type: dbw_mkz_msgs/FuelLevelReport
      md5: f5ec1964dbda02fda82785b8035744e4
    - type: dbw_mkz_msgs/GearReport
      md5: f33342dfeb80c29d8fe4b31e22519594
    - type: dbw_mkz_msgs/Misc1Report
      md5: 9ecd16fb81815b3e46e0550feea1da2f
    - type: dbw_mkz_msgs/SteeringReport
      md5: 25bf2c220d904531d8bc16ab5271325d
    - type: dbw_mkz_msgs/SurroundReport
      md5: 17a8c9ed72da4f55d44d6d71483cf0e3
    - type: dbw_mkz_msgs/SuspensionReport
      md5: a2c91f746e5d8bec139c834f92ac7468
    - type: dbw_mkz_msgs/ThrottleInfoReport
      md5: 8255d20d2bbc661ad39074024259c71a
    - type: dbw_mkz_msgs/ThrottleReport
      md5: a7fd7b93c8549e83c319e38a18f6dbdc
    - type: diagnostic_msgs/DiagnosticArray
      md5: 60810da900de1dd6ddd437c3503511da
    - type: diagnostic_msgs/DiagnosticStatus
      md5: d0ce08bc6e5ba34c7754f563a9cabaf1
    - type: dynamic_reconfigure/Config
      md5: 958f16a05573709014982821e6822580
    - type: dynamic_reconfigure/ConfigDescription
      md5: 757ce9d44ba8ddd801bb30bc456f946f
    - type: geometry_msgs/TwistStamped
      md5: 98d34b0043a2093cf9d9345ab6eef12e
    - type: nav_msgs/Odometry
      md5: cd5e73d190d741a2f92e81eda573aca7
    - type: radar_driver/RadarTracks
      md5: 6a2de2f790cb8bb0e149d45d297462f8
    - type: rosgraph_msgs/Log
      md5: acffd30cd6b6de30f120938c17c593fb
    - type: sensor_msgs/Image
      md5: 060021388200f6f0f447d0fcd9c64743
    - type: sensor_msgs/Imu
      md5: 6a62c6daae103f4ff57a132d6f95cec2
    - type: sensor_msgs/JointState
      md5: 3066dcd76a6cfaef579bd0f34173e9fd
    - type: sensor_msgs/NavSatFix
      md5: 2d3a8cd499b9b4a0249fb98fd05cfa48
    - type: sensor_msgs/PointCloud2
      md5: 1158d486dd51d683ce2f1be655c3c181
    - type: sensor_msgs/Range
      md5: c005c34273dc426c67a020a87bc24148
    - type: sensor_msgs/TimeReference
      md5: fded64a0265108ba86c3d38fb11c0c16
    - type: std_msgs/Bool
      md5: 8b94c1b53db61fb6aed406028ad6332a
    - type: std_msgs/Float64
      md5: fdb28210bfa9d7c91146260178d9a584
    - type: velodyne_msgs/VelodyneScan
      md5: 50804fc9533a0e579e6322c04ae70566
topics:
    - topic: /can_bus_dbw/can_rx
      type: dataspeed_can_msgs/CanMessageStamped
      messages: 15136
    - topic: /cloud_nodelet/parameter_descriptions
      type: dynamic_reconfigure/ConfigDescription
      messages: 1
    - topic: /cloud_nodelet/parameter_updates
      type: dynamic_reconfigure/Config
      messages: 1
    - topic: /diagnostics
      type: diagnostic_msgs/DiagnosticArray
      messages: 216
    - topic: /diagnostics_agg
      type: diagnostic_msgs/DiagnosticArray
      messages: 64
    - topic: /diagnostics_toplevel_state
      type: diagnostic_msgs/DiagnosticStatus
      messages: 64
    - topic: /image_raw
      type: sensor_msgs/Image
      messages: 513
    - topic: /objects/capture_vehicle/front/gps/fix
      type: sensor_msgs/NavSatFix
      messages: 169
    - topic: /objects/capture_vehicle/front/gps/rtkfix
      type: nav_msgs/Odometry
      messages: 213
    - topic: /objects/capture_vehicle/front/gps/time
      type: sensor_msgs/TimeReference
      messages: 203
    - topic: /objects/capture_vehicle/rear/gps/fix
      type: sensor_msgs/NavSatFix
      messages: 43
    - topic: /objects/capture_vehicle/rear/gps/rtkfix
      type: nav_msgs/Odometry
      messages: 214
    - topic: /objects/capture_vehicle/rear/gps/time
      type: sensor_msgs/TimeReference
      messages: 151
    - topic: /objects/obs1/rear/gps/fix
      type: sensor_msgs/NavSatFix
      messages: 22
    - topic: /objects/obs1/rear/gps/rtkfix
      type: nav_msgs/Odometry
      messages: 203
    - topic: /objects/obs1/rear/gps/time
      type: sensor_msgs/TimeReference
      messages: 149
    - topic: /radar/points
      type: sensor_msgs/PointCloud2
      messages: 427
    - topic: /radar/range
      type: sensor_msgs/Range
      messages: 428
    - topic: /radar/tracks
      type: radar_driver/RadarTracks
      messages: 428
    - topic: /rosout
      type: rosgraph_msgs/Log
      messages: 29
    - topic: /vehicle/brake_info_report
      type: dbw_mkz_msgs/BrakeInfoReport
      messages: 1069
    - topic: /vehicle/brake_report
      type: dbw_mkz_msgs/BrakeReport
      messages: 1068
    - topic: /vehicle/dbw_enabled
      type: std_msgs/Bool
      messages: 1
    - topic: /vehicle/filtered_accel
      type: std_msgs/Float64
      messages: 1066
    - topic: /vehicle/fuel_level_report
      type: dbw_mkz_msgs/FuelLevelReport
      messages: 214
    - topic: /vehicle/gear_report
      type: dbw_mkz_msgs/GearReport
      messages: 427
    - topic: /vehicle/gps/fix
      type: sensor_msgs/NavSatFix
      messages: 21
    - topic: /vehicle/gps/time
      type: sensor_msgs/TimeReference
      messages: 21
    - topic: /vehicle/gps/vel
      type: geometry_msgs/TwistStamped
      messages: 21
    - topic: /vehicle/imu/data_raw
      type: sensor_msgs/Imu
      messages: 2133
    - topic: /vehicle/joint_states
      type: sensor_msgs/JointState
      messages: 3208
    - topic: /vehicle/misc_1_report
      type: dbw_mkz_msgs/Misc1Report
      messages: 426
    - topic: /vehicle/sonar_cloud
      type: sensor_msgs/PointCloud2
      messages: 106
    - topic: /vehicle/steering_report
      type: dbw_mkz_msgs/SteeringReport
      messages: 1066
    - topic: /vehicle/surround_report
      type: dbw_mkz_msgs/SurroundReport
      messages: 106
    - topic: /vehicle/suspension_report
      type: dbw_mkz_msgs/SuspensionReport
      messages: 1069
    - topic: /vehicle/throttle_info_report
      type: dbw_mkz_msgs/ThrottleInfoReport
      messages: 2134
    - topic: /vehicle/throttle_report
      type: dbw_mkz_msgs/ThrottleReport
      messages: 1067
    - topic: /vehicle/tire_pressure_report
      type: dbw_mkz_msgs/SuspensionReport
      messages: 43
    - topic: /vehicle/twist
      type: geometry_msgs/TwistStamped
      messages: 1068
    - topic: /vehicle/twist_controller/parameter_descriptions
      type: dynamic_reconfigure/ConfigDescription
      messages: 1
    - topic: /vehicle/twist_controller/parameter_updates
      type: dynamic_reconfigure/Config
      messages: 1
    - topic: /vehicle/wheel_speed_report
      type: dbw_mkz_msgs/SuspensionReport
      messages: 2136
    - topic: /velodyne_nodelet_manager/bond
      type: bond/Status
      messages: 86
    - topic: /velodyne_packets
      type: velodyne_msgs/VelodyneScan
      messages: 214
```

Unfortunately, this dataset doesn't have Velodyne PointClouds and you have to transform them manually from `/velodyne_packets` topic.
If you have installed `ros indigo`, then it should not be a problem. Full instruction is [here](http://wiki.ros.org/velodyne_pointcloud).

```bash
rosrun velodyne_pointcloud transform_node
```

https://github.com/udacity/didi-competition
