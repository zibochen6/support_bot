# Deploy Facial Recognition on reComputer

## Introduction

This wiki will guide you through using a reComputer equipped with a `Hailo` NPU to implement real-time facial recognition. In this project, we use `SCRFD-10G` for efficient face detection, capable of quickly and accurately detecting faces of various scales, including small faces, ensuring real-time performance. At the same time, we employ the `ArcFace-MobileFaceNet` model for lightweight face recognition, which leverages the ArcFace loss function to enhance recognition accuracy and enable efficient identity verification.

## Prepare Hardware

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html) | | | | | | | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

Note: You need a USB camera as the input.

## Install Hailo Software & Verify Installation

### update the system

```
sudo apt update  
sudo apt full-upgrade
```

note

Sometimes you may encounter the following issues during updates.

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
```

This is because the time on the Raspberry Pi is set incorrectly, and you need to manually set the time on the Raspberry Pi with command below:

```
# This command only you can connect google.com  
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
```

After set your raspberry time, you can update your raspberry.

### Set pcie to gen2/gen3(gen3 is faster than gen2)")

Add following text to `/boot/firmware/config.txt`

```
#Enable the PCIe external connector  
  
dtparam=pciex1  
  
#Force Gen 3.0 speeds  
  
dtparam=pciex1_gen=3
```

note

If you want to use gen2, please comment dtparam=pciex1\_gen=3

### Install hailo-all and reboot

Open terminal on the Raspberry Pi5, and input command as follows to install Hailo software.

```
sudo apt install hailo-all  
sudo apt-get -y install libblas-dev nlohmann-json3-dev  
sudo reboot
```

### Check Software and Hardware

Open terminal on the Raspberry Pi5, and input command as follows to check if hailo-all have been installed.

```
hailortcli fw-control identify
```

The right result show as bellow:

![pir](https://files.seeedstudio.com/wiki/reComputer-R1000/YOLOV8/check_software.png)

Open terminal on the Raspberry Pi5, and input command as follows to check if hailo-8L have been connected.

```
lspci | grep Hailo
```

The right result show as bellow:

![pir](https://files.seeedstudio.com/wiki/reComputer-R1000/YOLOV8/check_hardware.png)

## Run Project

### Install Project

```
cd ~ && git clone https://github.com/Seeed-Projects/hailo-apps-infra  
cd hailo-apps-infra  
./install.sh  
source venv_hailo_apps/bin/activate
```

### Add your photo

```
cd /resources/face_recon/train  
# change name to the name of the person to be recognized  
mkdir name
```

Note: Place the photo of the person to be recognized into the folder that was just created.

### Add information to the database

```
cd ~/hailo-apps-infra/hailo_apps/hailo_app_python/apps/face_recognition  
python face_recognition.py --mode train
```

The right result show as bellow:

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/face/face_1.png)

### Run the project

Input the command below you will see a face recognition demo:

```
 python face_recognition.py --input usb
```

## Result

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.