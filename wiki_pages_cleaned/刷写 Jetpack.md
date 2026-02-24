# 将 JetPack 刷写到 J401-Mini 载板

reComputer Mini 是一款由 NVIDIA Jetson Orin Nano/Orin NX 模块驱动的微型 AI 计算机，可提供高达 100 TOPS 的 AI 性能。它在底部配备了 PCIe 端口，提供丰富的扩展能力，也可以灵活定制。整个系统设计用于嵌入到自主机器中，如无人机、巡逻机器人、配送机器人等。它可以直接使用 54V 直流输入，能够广泛应用于电池供电系统。

## 特性

* **出色的生产级 AI 性能：** 实现高达 **100 TOPS** 的 AI 性能，具有低功耗和低延迟特性，由 NVIDIA Orin SoC 构建，结合了 NVIDIA Ampere™ GPU 架构和 64 位操作能力，集成了先进的多功能视频和图像处理以及 NVIDIA 深度学习加速器。
* **手掌大小的边缘 AI 设备：** 紧凑尺寸为 **63mmx95mmx42mm**，配备 NVIDIA Jetson Orin NX 16GB 模块、Mini J401 载板、风扇和外壳。支持桌面和壁挂安装。
* **丰富 I/O 接口可扩展：** 包括多达 7x USB、1x DP 2.1、2x CSI、1x RJ45 千兆以太网、M.2 Key E、M.2 Key M、双通道 CAN 以及带扩展板的 GPIO。
* **加速解决方案上市：** 在 128GB NVMe SSD 上预装 **JetPack 6.0**、Linux OS BSP，支持 Jetson 软件和领先的 AI 框架。
* **规模化部署：** 支持 OTA、由 Allxon 和 Balena 提供的远程管理服务。
* **灵活定制：** 包括更换配件模块、标识以及基于 reComputer Mini J4012 原始设计的硬件接口修改。

## 规格参数

[TABLE COMPRESSED]
Columns: Jetson Orin 系统模块 | 规格 reComputer Mini J3010 reComputer Mini J3011 reComputer Mini J4011 reComputer Mini J4012 | 模块 Jetson Orin Nano 4GB Jetson Orin Nano 8GB Jetson Orin NX 8GB Jetson Orin NX 16GB | AI 性能 20 TOPS 40 TOPS 70 TOPS 100 TOPS | GPU 512核 NVIDIA Ampere 架构 GPU，配备 16 个 Tensor 核心 1024核 NVIDIA Ampere 架构 GPU，配备 32 个 Tensor 核心 | CPU 6核 Arm® Cortex®-A78AE v8.2 64位 CPU 1.5MB L2 + 4MB L3 6核 Arm® Cortex®-A78AE v8.2 64位 CPU 1.5MB L2 + 4MB L3 8核 Arm® Cortex®-A78AE v8.2 64位 CPU 2MB L2 + 4MB L3 | CPU 最大频率 1.5 GHz 2 GHz | 内存 4GB 64位 LPDDR5 34 GB/s 8GB 128位 LPDDR5 68 GB/s 8GB 128位 LPDDR5 102.4GB/s 16GB 128位 LPDDR5 102.4GB/s | 深度学习加速器 / 1x NVDLA v2 2x NVDLA v2 | 视频编码器 1080p30 由 1-2 个 CPU 核心支持 1x 4K60 (H.265) | 3x 4K30 (H.265) 6x 1080p60 (H.265) | 12x 1080p30 (H.265) ...

## 硬件概览

## 刷写 JetPack 操作系统

在这里，我们将向您展示如何将 [Jetpack 6.0](https://developer.nvidia.com/embedded/jetson-linux-archive) 刷写到连接到 reComputer Mini 的 NVMe SSD 上。

### 支持的 Nvidia Jetson 模块

* [NVIDIA® Jetson Orin™ Nano Module 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5554.html)
* [NVIDIA® Jetson Orin™ Nano Module 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5552.html)
* [NVIDIA® Jetson Orin™ NX Module 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5523.html)
* [NVIDIA® Jetson Orin™ NX Module 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5524.html)

### 前提条件

* Ubuntu 主机电脑
* 带有 Jetson Orin 模块的 reComputer J401-Mini 载板
* USB Micro-B 数据传输线

我们建议您使用物理 ubuntu 主机设备而不是虚拟机。
请参考下表准备主机。

[TABLE COMPRESSED]
Columns: JetPack 版本 Ubuntu 版本（主机电脑） | 18.04 20.04 22.04 | JetPack 5.x ✅ ✅ | JetPack 6.x ✅ ✅

### 准备 Jetpack 镜像

在这里，我们需要下载与我们使用的 Jetson 模块对应的系统镜像到我们的 Ubuntu PC：

[TABLE COMPRESSED]
Columns: Jetpack 版本 Jetson 模块 下载链接 SHA256 | 5.1.3 Orin Nx 16GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EfA7P_6gLnJAnxptIAURoCgBDF-emSfyD9uGWYY2vuFhmg?e=DF6a8l) 099bf8e706468dc36600ffdb3444168 3cde7454646621017fc39db49c16a2c53 | Orin Nx 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/Eew7pWvWB3RLtT5vMkVTFHABADBzxS8id4xNtrQHGcO3eg?e=drxTwI) 6ce30b9e212310498eee2c0a363cb35 14b1c607ae6a1ab403d5029115bc3a71b | Orin Nano 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcEvOGxB9DpOuFubj-xJ1oYBixiZy4vd0t_chXQcezPy9A?e=RnX7NN) b8f7a0b6d5974add33c3102824c671b 61ca8e278b0c5e3c38a7c5a45e251251e | Orin Nano 4GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EYi8K66PG6xOjwiU-_x3Ey4BpZhEiLFS8c_JoEDzeTVaxg?e=TkAgJV) cc6efd6e4a42f099dde47e9ed71a34e 0981e77c50e3dc74f38338210c1f3bda0 | 6.0 Orin Nx 16GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcQFCfXEWVREuzwvvBX7vRsBlr9H6HQpTBzmDw0rigIt1Q?e=IzLuYu) 7B4ABE1D1A8711D5D4E9B676DBB1E76 CDA35C614608CE7ECE112BC4A50E71C7C | Orin Nx 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EUpeLu1P7RJOv7-nqR7QbmABfmWR45xVUt95bMplpp25mQ?e=oiWB6b) 3956B968F2BFB9FDF37D952E83DDB70 3980C813156919BC367CA5E23BBDEC89F | Orin Nano 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EWbSLkBX0XpIrFjkT0vndGsBysfm51HvFkBFsRnfRaWBxA?e=t7vRcH) BF6921DF313B467254154BDA835C379 AD86D817E03D0301543B62F7CA0C9222F | Orin Nano 4GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EUB7YoQeCrVHnDjsrfFaL8EBxkjRrclpDxFwDB3dJpM3xQ?e=oYHLp7) 8941C13204A8069CE70B109B6A13EA2 40CBB02F69B8D4028D465134B3744BC28 | 6.2 Orin Nano 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EVjuq6G9y_5OjIxMIHFiBj0BVckYdcRQBunaXMHFBLZ3tw?e=tY89se) A1C5F44B19B6C06E11AC38ABDA79AD6 CBFF2AAFBEEA7BF3A14B2FE08EA37267F | Orin Nano 4GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcdaeIBdGRpCp0Dev5R3o1sB2Tr4HIwjgtp3d_XX7lE9Gg?e=bxteCW) 23855098982DD1E05C025D3F078BCA0 2F396C1FB68DC58E539D83569A894571D

Jetpack6 镜像文件大约为 **16.7GB**，下载时间约为 60 分钟。请耐心等待下载完成。

为了验证下载固件的完整性，您可以比较 SHA256 哈希值。

在 Ubuntu 主机上，打开终端并运行命令 `sha256sum <File>` 来获取下载文件的 SHA256 哈希值。如果得到的哈希值与 wiki 中提供的 SHA256 哈希值匹配，则确认您下载的固件是完整无损的。

### 进入强制恢复模式

在进行安装步骤之前，我们需要确保开发板处于强制恢复模式。

 分步说明 

* **步骤 1.** 在 USB2.0 DEVICE 端口和 ubuntu 主机 PC 之间连接一根 USB Micro-B 线缆。
* **步骤 2.** 使用针插入 RECOVERY 孔按下恢复按钮并保持按住。
* **步骤 3.** 连接电源。
* **步骤 4.** 释放恢复按钮。

在 Linux 主机 PC 上，打开终端窗口并输入命令 `lsusb`。如果返回的内容根据您使用的 Jetson SoM 包含以下输出之一，则表示开发板处于强制恢复模式。

* 对于 Orin NX 16GB：0955:7323 NVidia Corp
* 对于 Orin NX 8GB：0955:7423 NVidia Corp
* 对于 Orin Nano 8GB：0955:7523 NVidia Corp
* 对于 Orin Nano 4GB：0955:7623 NVidia Corp

下图是 Orin Nx 16GB 的示例：

### 逐步刷写到 Jetson

**步骤 1：** 在 ubuntu 主机 PC 上解压下载的镜像文件：
```
cd <path-to-image>  
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-orin-nano-8g-j401-6.0-36.3.0-2024-06-07.tar.gz
```**步骤 2:** 执行以下命令将 jetpack 系统刷写到 NVMe SSD：
```
cd mfi_xxxx  
# For example: cd mfi_recomputer-orin-j401  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```如果刷写过程成功，您将看到以下输出

刷写命令可能需要运行 2-10 分钟。

**步骤 3：** 使用板载 HDMI 连接器将 J501 连接到显示器，并完成初始配置设置：

请根据您的需要完成**系统配置**。

**步骤 4（可选）：** 安装 Nvidia Jetpack SDK

请在 Jetson 设备上打开终端并执行以下命令：
```
sudo apt update  
sudo apt install nvidia-jetpack
```## 硬件接口使用

如果您想了解更多关于硬件接口的详细规格和使用方法，请参考[此wiki](https://wiki.seeedstudio.com/cn/recomputer_jetson_mini_hardware_interfaces_usage/)。

## 资源

* [reComptuer Mini 数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_mini_datasheet_V1.0.pdf)
* [reComptuer Mini 原理图](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/reComputer_Mini_SCH.7z)
* [reComputer Mini 3D文件](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/reComputer_Mini_3D.7z)
* [Seeed Jetson系列产品目录](https://files.seeedstudio.com/wiki/Seeed_Jetson/Seeed-NVIDIA_Jetson_Catalog_V1.4.pdf)
* [Seeed Studio边缘AI成功案例](https://www.seeedstudio.com/blog/wp-content/uploads/2023/07/Seeed_NVIDIA_Jetson_Success_Cases_and_Examples.pdf)
* [Seeed Jetson系列产品对比](https://www.seeedstudio.com/blog/nvidia-jetson-comparison-nano-tx2-nx-xavier-nx-agx-orin/)
* [Seeed Jetson设备单页介绍](https://files.seeedstudio.com/wiki/Seeed_Jetson/Seeed-Jetson-one-pager.pdf)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。
