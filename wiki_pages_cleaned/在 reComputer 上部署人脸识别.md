# 在 reComputer 上部署人脸识别

## 简介

本 wiki 将指导您使用配备 `Hailo` NPU 的 reComputer 实现实时人脸识别。在这个项目中，我们使用 `SCRFD-10G` 进行高效的人脸检测，能够快速准确地检测各种尺度的人脸，包括小人脸，确保实时性能。同时，我们采用 `ArcFace-MobileFaceNet` 模型进行轻量级人脸识别，该模型利用 ArcFace 损失函数来提高识别精度并实现高效的身份验证。

## 准备硬件

[TABLE COMPRESSED]
Columns: reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145 | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

注意：您需要一个 USB 摄像头作为输入。

## 安装 Hailo 软件并验证安装

### 更新系统
```
sudo apt update  
sudo apt full-upgrade
```有时您在更新过程中可能会遇到以下问题。
```
Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]  
Get:2 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]  
Get:3 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]  
Get:4 http://archive.raspberrypi.com/debian bookworm InRelease [39.0 kB]  
Reading package lists... Done                                     
E: Release file for http://deb.debian.org/debian/dists/bookworm/InRelease is not valid yet (invalid for another 58d 8h 26min 35s). Updates for this repository will not be applied.  
E: Release file for http://deb.debian.org/debian-security/dists/bookworm-security/InRelease is not valid yet (invalid for another 84d 18h 23min 59s). Updates for this repository will not be applied.  
E: Release file for http://archive.raspberrypi.com/debian/dists/bookworm/InRelease is not valid yet (invalid for another 84d 13h 13min 5s). Updates for this repository will not be applied.  
E: Release file for http://deb.debian.org/debian/dists/bookworm-updates/InRelease is not valid yet (invalid for another 85d 0h 52min 29s). Updates for this repository will not be applied.
```这是因为 Raspberry Pi 上的时间设置不正确，您需要使用以下命令手动设置 Raspberry Pi 上的时间：
```
# This command only you can connect google.com  
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
```设置好 raspberry 时间后，您可以更新您的 raspberry。

### 设置 pcie 为 gen2/gen3（gen3 比 gen2 更快）

将以下文本添加到 `/boot/firmware/config.txt`
```
#Enable the PCIe external connector  
  
dtparam=pciex1  
  
#Force Gen 3.0 speeds  
  
dtparam=pciex1_gen=3
```如果您想使用 gen2，请注释掉 dtparam=pciex1\_gen=3

### 安装 hailo-all 并重启

在 Raspberry Pi5 上打开终端，输入以下命令来安装 Hailo 软件。
```
sudo apt install hailo-all  
sudo apt-get -y install libblas-dev nlohmann-json3-dev  
sudo reboot
```### 检查软件和硬件

在 Raspberry Pi5 上打开终端，输入以下命令来检查 hailo-all 是否已安装。
```
hailortcli fw-control identify
```正确的结果如下所示：

在 Raspberry Pi5 上打开终端，输入以下命令来检查 hailo-8L 是否已连接。
```
lspci | grep Hailo
```正确的结果如下所示：

## 运行项目

### 安装项目
```
cd ~ && git clone https://github.com/Seeed-Projects/hailo-apps-infra  
cd hailo-apps-infra  
./install.sh  
source venv_hailo_apps/bin/activate
```### 添加您的照片
```
cd /resources/face_recon/train  
# change name to the name of the person to be recognized  
mkdir name
```注意：将要识别的人的照片放入刚刚创建的文件夹中。

### 将信息添加到数据库
```
cd ~/hailo-apps-infra/hailo_apps/hailo_app_python/apps/face_recognition  
python face_recognition.py --mode train
```正确的结果如下所示：

### 运行项目

输入以下命令，您将看到人脸识别演示：
```
 python face_recognition.py --input usb
```## 结果

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。
