# 在 NVIDIA® Jetson 设备上使用 Scailable 入门指南

![](https://files.seeedstudio.com/wiki/Scailable/wiki-thumb-4.gif)

## 什么是 Scailable？

[Scailable](https://scailable.net) 提供了一个用于大规模创建和管理边缘 AI 解决方案的平台。使用 Scailable，您可以简单地配置任何支持的边缘设备（如路由器、网关或 IPC）将其转变为"智能"设备。智能设备可以在输入数据（如视频流）上运行先进的人工智能（AI）和机器学习（ML）模型，将输入转换为有意义的内容，例如统计视频中汽车的数量。

## 为什么在 NVIDIA Jetson 上使用 Scailable？

NVIDIA Jetson 平台是运行 Scailable 的绝佳选择，因为作为包含 NVIDIA SoM 的边缘 AI 设备，它能够在大规模地向这些设备空中部署各种 AI 管道后提供更好的推理性能。

本教程将介绍如何在 NVIDIA Jetson 平台上轻松安装 Scailable AI Manager，并使用 Scailable 平台远程配置和管理您的大规模 AI 解决方案。

## 先决条件

* 运行 NVIDIA JetPack 5.0+ 并连接到互联网的 NVIDIA Jetson 设备

  + 我们已经在运行 [JetPack 5.1.1](https://developer.nvidia.com/embedded/jetpack-sdk-511) 的 [reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-p-5586.html) 上测试了本教程。如果您想了解更多 Seeed 提供的 NVIDIA Jetson 设备，请访问[此页面](https://files.seeedstudio.com/products/NVIDIA/NVIDIA-Jetson-Devices-and-carrier-boards-comparision.pdf)。
* 运行 Windows、Linux 或 Mac 并连接到互联网的主机 PC

## 安装 Scailable AI Manager

**步骤 1：** 执行以下命令在 Jetson Orin 设备上安装 Scailable AI Manager

```
sudo bash -ic "$(wget -q -O - https://get.sclbl.net)"
```

note

在安装过程中，当提示询问是否启用 JetPack 5 支持时，您需要输入"y"。

![](https://files.seeedstudio.com/wiki/Scailable/2.jpg
)

**步骤 2：** 您可以在网页浏览器中输入 Jetson 设备的 IP 地址，后跟 **:8081**，或者直接输入命令行中显示的 URL，如下所示

![](https://files.seeedstudio.com/wiki/Scailable/4.jpg
)

## 注册 Scailable 账户

**步骤 1：** 当 Scailable AI Manager 显示后，通过给设备命名来注册设备，然后点击 **Register** 按钮

![](https://files.seeedstudio.com/wiki/Scailable/1.jpg
)

**步骤 3：** 确认您之前创建的设备名称，点击 **Register**，然后点击 **Return to device**

![](https://files.seeedstudio.com/wiki/Scailable/7.jpg
)

如果一切顺利，您将在 **Status** 选项卡下看到所有状态检查都成功，如下所示

![](https://files.seeedstudio.com/wiki/Scailable/8.jpg
)

## 运行 AI 应用程序

Scailable 预装了许多不同的 AI 模型供您试用。但是，如果您想使用自己的 AI 模型，也可以导入。

**步骤 1：** 在 **Model** 选项卡下，在 **First Model** 部分中，点击 **Assign Model**

![](https://files.seeedstudio.com/wiki/Scailable/9.jpg
)

**步骤 2：** 在这里您可以通过点击 **add a model** 添加自己的模型，或使用预构建的模型。这里我们将选择 **Scailable Models**

![](https://files.seeedstudio.com/wiki/Scailable/10.jpg
)

**步骤 3：** 作为示例，我们将选择 **People counter within a region** 模型。点击 **Use this model**

![](https://files.seeedstudio.com/wiki/Scailable/12.png
)

现在您将看到模型已被选中

![](https://files.seeedstudio.com/wiki/Scailable/13.png
)

**步骤 4：** 在 **Input** 选项卡下，为输入驱动程序选择 **Video driver**

![](https://files.seeedstudio.com/wiki/Scailable/14.png
)

在这里您可以选择视频流、图像或 Scailable 预装的示例图像/视频

![](https://files.seeedstudio.com/wiki/Scailable/16.png
)

**步骤 5：** 例如，我们将选择 Scailable 自带的预装视频源，即 **faces**

![](https://files.seeedstudio.com/wiki/Scailable/15.jpg
)

**步骤 6：** 在 **output** 选项卡下，保持默认设置

![](https://files.seeedstudio.com/wiki/Scailable/17.png
)

**步骤 7：** 在 **Options** 选项卡下，保持默认设置

![](https://files.seeedstudio.com/wiki/Scailable/18.png
)

**步骤 7：** 在 **Test** 选项卡下，点击 **Test configuration**

![](https://files.seeedstudio.com/wiki/Scailable/19.png
)

如果成功，您将看到以下输出

![](https://files.seeedstudio.com/wiki/Scailable/20.png
)

**步骤 8：** 在 **Run** 选项卡下，点击 **Run Model**

![](https://files.seeedstudio.com/wiki/Scailable/21.png
)

如果运行成功，您将看到以下输出

![](https://files.seeedstudio.com/wiki/Scailable/22.png
)

**步骤 9：** 点击 **View live visualization** 在本地预览推理结果

![](https://files.seeedstudio.com/wiki/Scailable/23.png
)

![](https://files.seeedstudio.com/wiki/Scailable/25.png
)

**步骤 10：** 点击 **View output in cloud** 以 CSV 或 JSON 格式下载结果

![](https://files.seeedstudio.com/wiki/Scailable/26.png
)

![](https://files.seeedstudio.com/wiki/Scailable/27.png
)

## 大规模部署AI模型

使用Scailable，您可以轻松地将单个模型大规模部署到多个设备上

**步骤1：** 访问[此网页](https://admin.sclbl.net/login)，登录到您的Scailable账户，您将看到如下仪表板

![](https://files.seeedstudio.com/wiki/Scailable/32.png
)

**步骤2：** 点击**DEVICES**后，您将看到所有连接到您Scailable账户的设备

![](https://files.seeedstudio.com/wiki/Scailable/28.png
)

**步骤3：** 通过点击复选框选择所有设备，为设备组输入名称并点击**Save new groups**

![](https://files.seeedstudio.com/wiki/Scailable/29.png
)

**步骤4：** 点击**Assign a model to all devices in group**

![](https://files.seeedstudio.com/wiki/Scailable/30.png
)

**步骤5：** 像之前一样选择一个模型，该模型将远程部署到组中的所有设备

成功远程部署模型后，您将看到以下输出

![](https://files.seeedstudio.com/wiki/Scailable/31.jpg
)

## 了解更多

Scailable提供非常详细和全面的文档。因此强烈建议您在[这里](https://docs.scailable.net)查看它们。

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。