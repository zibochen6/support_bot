# 为 reComputer AI R2140 构建 balenaOS

[balena](https://www.balena.io/) 是一个物联网（IoT）平台，旨在帮助开发者在设备群中构建、部署和管理 IoT 应用程序。它支持广泛的设备架构，包括容器化应用程序部署功能，使您能够轻松更新 IoT 软件和主机操作系统，修复错误并为 IoT 应用程序引入新功能。balena 提供了一种统一的方式来推送代码更新、管理设备配置，并确保设备在现场可靠安全地运行，无论其位置或网络条件如何。

![pir](https://files.seeedstudio.com/wiki/Edge_Box/balena/balena.png)

## 入门指南

在开始此项目之前，您可能需要按照此处描述的内容提前准备硬件和软件。

### 硬件准备

|  |  |  |
| --- | --- | --- |
| reComputer AI R2140|  |  | | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2140-12-p-6431.html) | | |

> 注意：准备一张 SD 卡和读卡器来烧录镜像。

### 软件

* 一个 [balenaCloud](https://balena.io) 账户（在此注册）并免费获得前 10 台设备。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/balena.png)

* [balenaEtcher](https://etcher.balena.io/) 用于刷写 reComputer R2140 存储器。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/balenaEtcher.png)

### 在 balena cloud 上创建舰队

请参考下图中的流程来创建舰队：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/creat_fleet.png)

### 添加设备

请参考下图中的流程来添加新的 reComputer AI R2140：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/add_device.png)

### 安装 balena OS

请参考下图中的流程来安装 balena OS：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/install_image.png)

### 刷写 balena OS

请参考下图中的流程将 balena OS 刷写到 SD 卡：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/flash_image.png)

下图显示了刷写完成后的样子：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/finish_image.png)

### 测试设备

将刷写好的 SD 卡插入 recomputer AI box，然后开机并连接网线。2 分钟后，您应该能够在 Balena Cloud 中看到新设备。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/test_device.png)

当您点击设备时，您将进入下图所示的界面，这意味着您可以远程控制设备。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/balena/recomputer_ai_box/resul.png)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。