# reComputer J1010 入门指南

## 介绍

reComputer J1010 是一款基于 NVIDIA Jetson Nano 4GB 生产模块构建的紧凑型边缘计算机，配备 128 个 NVIDIA CUDA® 核心，提供 0.5 TFLOPs（FP16）算力来运行 AI 框架和应用程序，如图像分类、目标检测和语音处理。生产模块提供 16GB eMMC、更长的保修期，以及在生产环境中 5-10 年的运行寿命（[Jetson FAQ](https://developer.nvidia.com/embedded/faq)）。我们还有基于 Jetson Xavier NX 模块构建的 reComputer [J20 系列](https://www.seeedstudio.com/reComputer-J2021-p-5438.html?queryID=14111cbf2ca4f2951fd8a4c1762eb435&objectID=5438&indexName=bazaar_retailer_products)，为更复杂的 AI 工作负载提供 21 TOPS AI 性能。

除了 Jetson 模块，reComputer J1010 还包括 [J101 载板](https://www.seeedstudio.com/reComputer-J101-v2-Carrier-Board-for-Jetson-Nano-p-5396.html)，板载 microSD 卡插槽、1×USB 3.0、2×USB2.0、HDMI、M.2 Key E 用于 WiFI、LTE 和蓝牙、RTC、Raspberry Pi GPIO 40 针接口等，以及散热器和铝制外壳。设备已预装 Jetpack 4.6.1，只需插入 USB C 5V/3A 电源、键盘、鼠标和网线，您就可以开始您的嵌入式 AI 之旅！如果您需要更多 USB 3.0 接口和板载 M.2 key M 来连接 SSD，您可以选择 reComputer J1020。

注意：我们收到客户询问，他们需要比 16GB eMMC 更大的存储空间。对于 2022 年 7 月 30 日之后的订单，我们在 reComputer J1010 的[载板](https://www.seeedstudio.com/reComputer-J101-v2-Carrier-Board-for-Jetson-Nano-p-5396.html)上增加了 microSD 卡插槽。请查看将启动镜像写入 microSD 卡和调整 I/O 速度的[指南](https://wiki.seeedstudio.com/cn/J1010_Boot_From_SD_Card/#flashing-system-from-j101-to-sd-card)。

## 特性

* **手掌大小的边缘 AI 完整系统：** 提供 0.5 TFLOPs（FP16）的现代 AI 算力和丰富的嵌入式开发接口。
* **开发和部署就绪：** 预装 NVIDIA JetPack 支持完整的 [Jetson 软件栈](https://developer.nvidia.com/embedded/develop/software)和业界领先的 [AI 开发者工具](https://wiki.seeedstudio.com/cn/Jetson-AI-developer-tools/)，用于构建强大的 AI 应用程序，如物流、零售、服务、农业、智慧城市、医疗保健和生命科学等
* **节能高效：** 由 Type C 5V/3A 供电，功耗低至 5 瓦。
* **可扩展：** 通过板载接口和 reComputer 外壳，可通过背面的安装孔壁挂安装。

## 规格参数

[TABLE COMPRESSED]
Columns: 规格参数 [reComputer J1010](https://www.seeedstudio.com/Jetson-10-1-A0-p-5336.html) [reComputer J1020](https://www.seeedstudio.com/Jetson-10-1-H0-p-5335.html) [NVIDIA Jetson Nano Developer Kit-B01](https://www.seeedstudio.com/NVIDIA-Jetson-Nano-Development-Kit-B01-p-4437.html) | 模块 Jetson Nano 4GB（生产版本） Nano（非生产版本） | 存储 16 GB eMMC MicroSD（不含卡） | SD卡插槽 包含（在载板上） - 包含（在模块上） | 视频编码器 4K30 | 2x1080p60 | 4x1080p30 | 4x720p60 | 9x720p30 (H.265 & H.264) 4Kp30 | 4x 1080p30 | 9x 720p30 (H.264/H.265) | 视频解码器 4K60 ...

## 将 JetPack 刷写到 reComputer J1010

请参考此 [wiki](/cn/reComputer_J1010_J101_Flash_Jetpack/) 页面获取更多信息，因为 J1010 使用 J101 载板。

## 资源

[reComputer J1010 数据手册](https://files.seeedstudio.com/wiki/reComputer/reComputer-J1010-datasheet.pdf)

[reComptuer J101 载板原理图](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer%20J101_V2.0_SCH_240822.pdf)

[reComputer J1010 3D 文件](https://files.seeedstudio.com/products/NVIDIA-Jetson/J1010-Jetson-Nano.stp)

[Seeed Jetson 系列目录](https://files.seeedstudio.com/wiki/Seeed_Jetson/Seeed-NVIDIA_Jetson_Catalog_V1.4.pdf)

[Seeed Jetson 设备单页介绍](https://files.seeedstudio.com/wiki/Seeed_Jetson/Seeed-Jetson-one-pager.pdf)
