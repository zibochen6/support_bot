# 在 Jetson AGX Orin 上部署 NVBlox 与 Orbbec 相机

![](https://media.githubusercontent.com/media/NVIDIA-ISAAC-ROS/.github/release-4.0/resources/isaac_ros_docs/repositories_and_packages/isaac_ros_nvblox/isaac_sim_nvblox_humans.gif)

## 简介

[Isaac ROS NVBlox](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox) 是 NVIDIA 开发的高性能 GPU 加速 3D 建图框架，用于实时机器人感知。与单目深度估计模型不同，NVBlox 使用来自 RGB-D 相机或立体相机的真实深度输入来构建精确的 3D 场景表示。

它实时构建密集的 TSDF（截断符号距离场）和 ESDF（欧几里得符号距离场）地图，实现高质量的 3D 重建、障碍物感知导航和碰撞检测。NVBlox 还可以生成网格、基于体素的代价地图以及适用于自主移动机器人（AMR）的 3D 占用表示。

这使其在边缘 AI 应用中特别有价值，在这些应用中硬件约束和计算效率是关键考虑因素。本 wiki 演示了如何在 **Jetson AGX Orin** 上部署 Isaac ROS NVBlox，集成 **ROS 2**，使用 **Orbbec RGB-D 相机** 和移动机器人平台来实现完全的设备端感知和导航管道。🚀

![](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/5/-/5-100020039-recomputer-mini-j501---carrier-board-for-jetson-agx-orin.jpg)

[**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Mini-J501-Carrier-Board-for-Jetson-AGX-Orin-p-6606.html)

## 先决条件

* **[reComputer J50](https://www.seeedstudio.com/reComputer-Robotics-J4012-p-6505.html)**（Jetson AGX Orin）配备 JetPack 6.2
* Orbbec RGB-D 相机 📷
* 移动机器人底盘（可选）🤖
* 已安装 [ROS2 Humble](https://wiki.seeedstudio.com/cn/install_ros2_humble/) 环境
* 需要安装 Orbbec ROS2 SDK
* 需要安装 Isaac ROS

![](https://files.seeedstudio.com/wiki/other/page-nvblox.jpg)

## 技术亮点

* **实时 3D 建图**：NVBlox 使用 GPU 加速实时生成密集的 TSDF 和 ESDF 地图，为机器人应用提供高质量的 3D 场景重建。
* **RGB-D 相机集成**：利用 Orbbec RGB-D 相机的真实深度信息创建精确的 3D 表示，无需依赖单目深度估计。
* **边缘部署优化**：专为 Jetson AGX Orin 等边缘设备的高效推理而设计，具有 CUDA 优化以获得最大性能。
* **导航就绪输出**：生成适用于自主导航和碰撞避免的网格、基于体素的代价地图和 3D 占用网格。
* **ROS2 原生支持**：提供与标准机器人消息类型的无缝 ROS2 Humble 集成，便于集成到现有机器人系统中。

## 环境设置

### 安装基本依赖

在终端中安装以下依赖：

```
sudo apt update  
sudo apt-get install python3-pip # Install Python3  
sudo apt-get install nvidia-jetpack # Install developer tools  
sudo pip3 install jetson-stats # Install Jtop to check JetPack version  
sudo apt-get install git-lfs # Install Git LFS
```

### 安装 Docker CE

更新软件源：

```
sudo apt-get update
```

安装基本依赖：

```
sudo apt-get install \  
    apt-transport-https \  
    ca-certificates \  
    curl \  
    software-properties-common # Install essential packages to allow apt over HTTPS
```

添加 Docker 的官方 GPG 密钥：

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

添加 Docker 的稳定仓库：

```
sudo add-apt-repository \  
   "deb [arch=arm64] https://download.docker.com/linux/ubuntu \  
   $(lsb_release -cs) \  
   stable"
```

再次更新包列表（添加了新仓库）：

```
sudo apt-get update
```

安装 Docker CE（社区版）：

```
sudo apt-get install docker-ce
```

确保 Docker 启动：

```
sudo systemctl enable docker  
sudo systemctl start docker
```

添加权限（将用户添加到 Docker 组）：

```
sudo usermod -aG docker $USER
```

重启系统或注销：

```
sudo reboot
```

### 安装 Isaac ROS 3.2

创建工作空间并添加到环境：

```
mkdir -p ~/workspaces/isaac_ros-dev/src  
echo "export ISAAC_ROS_WS=${HOME}/workspaces/isaac_ros-dev/" >> ~/.bashrc  
source ~/.bashrc
```

进入工作空间并克隆包：

```
cd ${ISAAC_ROS_WS}/src  
git clone -b release-3.2 https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common.git
```

拉取官方 Isaac Common Docker 镜像并进入 Docker：

```
cd ${ISAAC_ROS_WS}/src/isaac_ros_common && \  
  ./scripts/run_dev.sh
```

运行 `./scripts/run_dev.sh` 将自动安装 Isaac ROS 并启动容器。

tip

安装 Isaac ROS 需要在终端中登录 NVIDIA NGC 并输入您的 NGC 账户生成的 API Key 🔑

### 安装 Orbbec SDK ROS2

使用 Orbbec RGB-D 相机需要安装 SDK 驱动。本指南使用从源码构建的方法。

安装依赖：

```
sudo apt install libgflags-dev nlohmann-json3-dev \  
ros-$ROS_DISTRO-image-transport ros-${ROS_DISTRO}-image-transport-plugins ros-${ROS_DISTRO}-compressed-image-transport \  
ros-$ROS_DISTRO-image-publisher ros-$ROS_DISTRO-camera-info-manager \  
ros-$ROS_DISTRO-diagnostic-updater ros-$ROS_DISTRO-diagnostic-msgs ros-$ROS_DISTRO-statistics-msgs ros-$ROS_DISTRO-xacro \  
ros-$ROS_DISTRO-backward-ros libdw-dev libssl-dev mesa-utils libgl1 libgoogle-glog-dev
```

创建 colcon 工作空间：

```
mkdir -p ~/ros2_ws/src  
  
cd ~/ros2_ws/src  
git clone https://github.com/orbbec/OrbbecSDK_ROS2.git  
cd OrbbecSDK_ROS2  
git checkout v2-main
```

进入工作目录并编译：

```
cd ~/ros2_ws  
colcon build --event-handlers console_direct+ --cmake-args -DCMAKE_BUILD_TYPE=Release
```

为了让 Orbbec 相机在 Linux 上被正确识别，需要安装 udev 规则。

进入源码工作目录并运行脚本：

```
cd ~/ros2_ws/src/OrbbecSDK_ROS2/orbbec_camera/scripts  
sudo bash install_udev_rules.sh  
sudo udevadm control --reload-rules && sudo udevadm trigger
```

note

如果不执行此脚本，由于权限问题，打开设备将失败。您需要使用 sudo（管理员权限）运行示例。⚠️

## 部署 NVBlox

### 构建 NVBlox

获取适配 Orbbec 相机的 NVBlox 源码并复制到工作目录：

```
git clone https://github.com/jjjadand/isaac-NVblox-Orbbec.git  
cp -r isaac-NVblox-Orbbec/src/isaac_ros_nvblox/ ${ISAAC_ROS_WS}/src/  
cp -r isaac-NVblox-Orbbec/src/isaac_ros_nitros/ ${ISAAC_ROS_WS}/src/  
cp -r isaac-NVblox-Orbbec/build/ ${ISAAC_ROS_WS}/
```

进入工作空间并启动 Isaac ROS Docker 容器：

```
cd ${ISAAC_ROS_WS}/src/isaac_ros_common && \  
  ./scripts/run_dev.sh
```

（可选）如果遇到类似以下的错误：

```
Finished pulling pre-built base image: nvcr.io/nvidia/isaac/ros:aarch64-ros2_humble_4c0c55dddd2bbcc3e8d5f9753bee634c  
Nothing to build, retagged nvcr.io/nvidia/isaac/ros:aarch64-ros2_humble_4c0c55dddd2bbcc3e8d5f9753bee634c as isaac_ros_dev-aarch64  
Running isaac_ros_dev-aarch64-container  
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: could not apply required modification to OCI specification: error modifying OCI spec: failed to inject CDI devices: unresolvable CDI devices nvidia.com/gpu=all
```

您可以尝试在终端中运行以下命令来修复：

```
sudo nvidia-ctk cdi generate --mode=csv --output=/etc/cdi/nvidia.yaml
```

成功启动容器后，您应该看到类似这样的内容：

![](https://files.seeedstudio.com/wiki/other/isaac-ros.jpg)

安装额外依赖：

```
sudo apt update  
sudo apt-get install -y ros-humble-magic-enum  
sudo apt-get install -y ros-humble-foxglove-msgs
```

将 CUDA 环境变量添加到 `.bashrc`：

```
echo '  
CUDA_HOME=/usr/local/cuda  
export PATH=$CUDA_HOME/bin:$PATH  
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH  
export CUDACXX=$CUDA_HOME/bin/nvcc  
' >> ~/.bashrc
```

创建符号链接：

```
sudo ln -sf /opt/ros/humble/include/magic_enum.hpp /usr/include/magic_enum.hpp  
  
sudo mkdir -p /opt/ros/humble/include/foxglove_msgs  
sudo ln -sfn /opt/ros/humble/include/foxglove_msgs/foxglove_msgs/msg /opt/ros/humble/include/foxglove_msgs/msg
```

在 `/workspaces/isaac_ros-dev` 中构建并初始化工作空间：

```
colcon build --symlink-install --cmake-args -DBUILD_TESTING=OFF  
source install/setup.bash
```

编译完成后，您应该看到类似这样的结果：

![](https://files.seeedstudio.com/wiki/other/NVblox-complied.jpg)

### 启动 NVBlox

通过数据线将 Orbbec 相机连接到 Jetson 后，首先在本地环境中启动 Orbbec ROS2 脚本：

```
cd ~/ros2_ws/src  
source install/setup.bash  
  
ros2 launch orbbec_camera <camera_name>.launch.py  
  
# Example: ros2 launch orbbec_camera gemini2.launch.py
```

以下是一些支持的 `<camera_name>` 参数：

* gemini210
* gemini2
* gemini2L
* gemini\_330\_gmsl
* gemini\_330\_series

warning

注意，您不应该在 Docker 容器内启动 Orbbec 脚本。请确保您已按照之前的教程安装了 Orbbec 驱动程序。⚠️

Isaac ROS 容器默认与本地发布的 ROS2 桥接。在 Docker 容器中，输入：

```
ros2 topic list
```

通常，您应该在 Docker 容器中看到 Orbbec 相机发布的以下数据主题：

```
/camera/accel/imu_info  
/camera/color/camera_info  
/camera/color/image_raw  
/camera/depth/camera_info  
/camera/depth/image_raw  
/camera/depth/points  
/camera/depth_filter_status  
/camera/device_status  
/camera/gyro/imu_info  
/camera/gyro_accel/sample  
/camera/ir/camera_info  
/camera/ir/image_raw
```

确保您可以读取 Orbbec 相机数据主题。然后在 Isaac ROS 容器中启动 NVBlox 示例脚本：

```
cd ~/workspaces/isaac_ros-dev  
source install/setup.bash  
  
ros2 launch nvblox_examples_bringup orbbec_example.launch.py
```

您可以在 RViz 中看到 NVBlox 输出的 3D 占用网格和网格：

![](https://files.seeedstudio.com/wiki/other/rviz.jpg)

RViz 可以按如下所示进行配置。启用您想要的可视化结果并选择可用的主题名称：

![](https://files.seeedstudio.com/wiki/other/rviz-lan.jpg)

最后，通过将 AGX Orin 和 Orbbec 相机安装在移动 AGV 上，您可以实现视频中显示的效果：🎥

这可以用于移动机器人的障碍物检测和构建场景的 3D 网格地图。🤖

## 参考资料

* [Isaac ROS Common GitHub 仓库](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common)
* [Isaac ROS NVBlox GitHub 仓库](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox.git)
* [Isaac NVBlox Orbbec GitHub 仓库](https://github.com/jjjadand/isaac-NVblox-Orbbec#)
* [ROS2 Humble 文档](https://docs.ros.org/en/humble/)
* [Orbbec SDK ROS2 文档](https://github.com/orbbec/OrbbecSDK_ROS2)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。