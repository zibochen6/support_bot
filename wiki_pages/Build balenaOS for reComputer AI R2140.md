# Build balenaOS for reComputer AI R2140

[balena](https://www.balena.io/) is an Internet of Things (IoT) platform designed to help developers build, deploy, and manage IoT applications across a fleet of devices. It supports a wide range of device architectures and includes features for containerized application deployment, making it possible to easily update your IoT software and HostOS, fix bugs and introduce new features on your IoT applications. balena provides a unified way to push code updates, manage device configurations and ensure devices run reliably and securely in the field, regardless of their location or network conditions.

![pir](https://files.seeedstudio.com/wiki/Edge_Box/balena/balena.png)

## Getting Start

Before you start this project, you may need to prepare your hardware and software in advance as described here.

### Hardware Preparation

|  |  |  |
| --- | --- | --- |
| reComputer AI R2140|  |  | | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2140-12-p-6431.html) | | |

> Note: Prepare an SD card and a card reader to burn the image.

### Software

* A [balenaCloud](https://balena.io) account (sign up here) and get the first 10 devices free.

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/balena.png)

* [balenaEtcher](https://etcher.balena.io/) to flash the reComputer R2140 memory.

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/balenaEtcher.png)

### Creat fleet on balena cloud

Please refer to the process in the image below to create the fleet：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/creat_fleet.png)

### Add device

Please refer to the process in the image below to add new reComputer AI R2140：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/add_device.png)

### Install balena OS

Please refer to the process in the image below to install balena OS：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/install_image.png)

### Flash balena OS

Please refer to the process in the image below to flash balena OS to SD card：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/flash_image.png)

The image below shows what it looks like after the flashing is complete：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/finish_image.png)

### Test device

Insert the flashed SD card into the recomputer AI box, then power it on and connect the Ethernet cable. After 2 minutes, you should be able to see the new device in Balena Cloud.

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/test_device.png)

When you click on the device, you'll enter the screen shown in the image below, which means you can remotely control the device.

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/resul.png)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.