FROM ubuntu:trusty

# setup environment
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

# Setup Keys
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 421C365BD9FF1F717815A3895523BAEEB01FA116

# Setup Sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init && rosdep update

# install ros packages
ENV ROS_DISTRO indigo
RUN apt-get update && apt-get install -y \
    ros-indigo-ros-core \
    ros-indigo-ros-base \
    ros-indigo-desktop \
    ros-indigo-desktop-full \
    ros-indigo-velodyne-* \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/share/didi
WORKDIR /usr/share/didi

# setup entrypoint
COPY ./ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
