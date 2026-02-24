# reComputer Super 入门指南

reComputer Super 系列为 reComputer Classic 提供了强大的性能提升，AI 性能提升高达 1.7 倍，达到 157 TOPS。它包含搭载 Jetson Orin Nano（11410311、11410312）和 Jetson Orin NX（11410313、11410314）的型号。
专为开发和生产而设计，配备丰富的接口，包括 M.2 Key E/M、双 RJ45 以太网、Mini-PCIe、4x USB 3.2、HDMI 2.1、4x CSI 和 CAN。预装 Jetpack 6.2 和 Linux OS BSP，可立即投入市场。
它还支持广泛的 LLM 和物理 AI 框架，如 NVIDIA、Hugging Face、ONNX、PyTorch 和 ROS2/1，可在边缘无缝运行，甚至将这些多模态能力与机器人应用相结合，丰富物理 AI 开发。

## 主要特性

### 🚀 ​**性能提升**

* ​**AI 性能比 reComputer Classic 提升 1.7 倍**，达到 ​**157 TOPS**
* 搭载 ​**Jetson Orin Nano**（型号：11410311、11410312）和 ​**Jetson Orin NX**（型号：11410313、11410314）

### 🔌 ​**丰富的连接性和接口**

* ​**M.2 Key E/M** + ​**Mini-PCIe** 提供扩展性
* ​**双 RJ45 以太网**端口，支持高速网络
* ​**4x USB 3.2**、​**HDMI 2.1**、​**4x CSI**（摄像头串行接口）
* ​**CAN 总线**支持工业/机器人应用

### 🛠️ ​**开发和生产就绪**

* 预装 ​**Jetpack 6.2** 和 ​**Linux OS BSP**，开箱即用
* 与以下框架无缝集成边缘 AI：
  + ​**NVIDIA**、​**Hugging Face**、​**ONNX**、​**PyTorch**
  + ​**ROS2/1** 用于机器人应用
* 支持 ​**多模态 AI** 和 ​**物理 AI** 开发

### 🤖 ​**边缘 AI 和机器人优化**

* 在边缘融合 ​**LLM（大语言模型）**能力与 ​**物理 AI**
* 适用于机器人、工业自动化和实时 AI 推理
* 通过预配置软件栈加速 ​**市场投入**

### ⚠️ 电源和配件指南

#### 1. ​**电源适配器**

* ​**Jetson Orin Nano**：12V 5A（5525 桶形插头）
* ​**Jetson Orin NX**：19V 4.74A（5525 桶形插头）
* 始终使用 ​**官方适配器**并满足电源要求。

#### 2. ​**交流电源线**

* 使用 ​**特定地区**的三叶草电源线。

#### 3. ​**配件**

* 仅使用 ​**官方推荐**的配件（如摄像头、无线模块）以获得最佳性能和兼容性。

## 规格参数

[TABLE COMPRESSED]
Columns: Jetson Orin Super 系统模块 | 规格 reComputer Super J3010 reComputer Super J3011 reComputer Super J4011 reComputer Super J4012 | 模块 NVIDIA Jetson Orin™ Nano 4GB NVIDIA Jetson Orin™ Nano 8GB NVIDIA Jetson Orin™ NX 8GB NVIDIA Jetson Orin™ NX 16GB | AI 性能 34 TOPS 67 TOPS 117 TOPS 157 TOPS | GPU 512 核 NVIDIA Ampere 架构 GPU，配备 16 个 Tensor 核心 1024 核 NVIDIA Ampere 架构 GPU，配备 32 个 Tensor 核心 | CPU 6 核 Arm® Cortex®-A78AE v8.2 64 位 CPU 1.5MB L2 + 4MB L3 6 核 Arm® Cortex®-A78AE v8.2 64 位 CPU 1.5MB L2 + 4MB L3 8 核 Arm® Cortex®-A78AE v8.2 64 位 CPU 2MB L2 + 4MB L3 | CPU 最大频率 1.7 GHz (MAXN\_SUPER) 2 GHz | 内存 4GB 64 位 LPDDR5 34 GB/s 8GB 128 位 LPDDR5 68 GB/s 8GB 128 位 LPDDR5 102.4GB/s 16GB 128 位 LPDDR5 102.4GB/s | 深度学习加速器 / 1x NVDLA v2 2x NVDLA v2 | 视频编码器 1080p30 由 1-2 个 CPU 核心支持 1x 4K60 (H.265) | 3x 4K30 (H.265) 6x 1080p60 (H.265) | 12x 1080p30 (H.265) ...

## 刷写 JetPack 操作系统

### 支持的模块

* [NVIDIA® Jetson Orin™ Nano Module 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5553.html)
* [NVIDIA® Jetson Orin™ Nano Module 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5551.html?___store=retailer)
* [NVIDIA® Jetson Orin™ NX Module 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5522.html)
* [NVIDIA® Jetson Orin™ NX Module 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5523.html)

### 前提条件

* Ubuntu 主机 PC
* reComputer Super
* USB Type-C 数据传输线

我们建议您使用物理 ubuntu 主机设备而不是虚拟机。
请参考下表准备主机。

[TABLE COMPRESSED]
Columns: JetPack 版本 Ubuntu 版本（主机） | 18.04 20.04 22.04 | JetPack 6.x ✅ ✅

### 准备 Jetpack 镜像

在这里，我们需要将对应我们使用的 Jetson 模块的系统镜像下载到 Ubuntu PC：

[TABLE COMPRESSED]
Columns: Jetpack 版本 Jetson 模块 GMSL 下载链接 1 SHA256 | 6.2 Orin Nano 4GB ✅ [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EQiC_is_O2tEkvFzu-3SrWYBFdcQr0zZRUf81lkjnXpnkQ?e=f3ISaO) 8FF204A65C006717ED45241186C14B4  FAA8ACE5BEBCDCE755F94C3CBF1311C38 | Orin Nano 8GB ✅ [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EbEYa6n_P6pCh1TQbVBSpcQBZlFVm_-il3sqXEBDGpdPJA?e=S1dgfv) 7EC06C0D17E33AE43D3C69EED791F64 CB9CFDC497E01D525E18EBAC1547A0236 | Orin NX 8GB ✅ [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EevZ9hO7BfhDuJvDPYIdHGkBGhrKcWgCyAuTQu1gpHsz4g?e=xbXfbL) 06B175484220DA7A63CC7CDAAE339F7E FF8997180AF1C4B836D1098CBD8A169D | Orin NX 16GB ✅ [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EeIg8k2osZFAuPzOlcO-FtIBdhbgULGQrsQOg4uUrXoK4w?e=uo29A8) CF37D028D6466DCC13201367E6358A6 9B7B5305CAE2A2B785E3ECFD3D8C66304

Jetpack6 镜像文件大小约为 **14.1GB**，下载时间约为 60 分钟。请耐心等待下载完成。

为了验证下载固件的完整性，您可以比较 SHA256 哈希值。

在 Ubuntu 主机上，打开终端并运行命令 `sha256sum <File>` 来获取下载文件的 SHA256 哈希值。如果得到的哈希值与 wiki 中提供的 SHA256 哈希值匹配，则确认您下载的固件是完整无损的。

### 进入强制恢复模式

在进行安装步骤之前，我们需要确保开发板处于强制恢复模式。

 分步指南 

**步骤 1.** 将开关切换到 RESET 模式。

**步骤 2.** 通过连接电源线为 reComputer Super 供电。

**步骤 3.** 使用 USB Type-C 数据传输线将 Super 连接到 Ubuntu 主机 PC。

**步骤 4.** 在 Linux 主机 PC 上，打开终端窗口并输入命令 `lsusb`。如果返回的内容根据您使用的 Jetson SoM 有以下输出之一，则开发板处于强制恢复模式。

* 对于 Orin NX 16GB：**0955:7323 NVidia Corp**
* 对于 Orin NX 8GB：**0955:7423 NVidia Corp**
* 对于 Orin Nano 8GB：**0955:7523 NVidia Corp**
* 对于 Orin Nano 4GB：**0955:7623 NVidia Corp**

下图是 Orin Nano 8GB 的示例

### 刷写到 Jetson

**步骤 1：** 解压下载的镜像文件：
```
cd <path-to-image>  
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-super-orin-nx-16g-j401-6.2-36.4.3-2025-05-22.tar.gz
```**步骤 2：** 执行以下命令将 jetpack 系统刷写到 NVMe SSD：
```
cd mfi_xxxx  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```如果刷写过程成功，您将看到以下输出

刷写命令可能需要运行 2-10 分钟。

**步骤 3：** 使用 HDMI 线缆连接显示器，并完成 reComputer Super 系统的初始化配置：

请根据您的需要完成 **System Configuration**。

## 资源

[reComputer Robotics J401 载板数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_super_user_manual.pdf)
[原理图](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer%20Super%20J401_v1.0_SCH_PDF_250401.pdf)
[3D 文件](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer%20Super%20J401.stp)
[机械图纸-reComputer Super](https://files.seeedstudio.com/products/NVIDIA-Jetson/Mechanical_reComputer_Super.dxf)
[机械图纸-reComputer Super PCBA](https://files.seeedstudio.com/products/NVIDIA-Jetson/Mechanical_reComputer_Super_PCBA.dxf)
[Seeed Jetson 单页介绍](https://files.seeedstudio.com/wiki/Seeed_Jetson/Seeed-Jetson-one-pager.pdf)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。
