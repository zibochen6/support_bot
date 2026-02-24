# reComputer J401B 入门指南

## 介绍

reComputer J401B 系列是 reComputer Classic 系列的迭代产品。搭载 NVIDIA Jetson Orin NX 8GB 模块的 reComputer J4011B 是一款功能强大且紧凑的边缘 AI 设备，具有丰富的接口：2x USB 3.2、HDMI、以太网、用于 Wi-Fi 模块的 M.2 Key E、用于 SSD 的 M.2 Key M、用于 LTE 模块的 mini-PCIe、CAN、40 针等更多接口。

## 特性

* **构建最强大的嵌入式 AI 平台：** 兼容 Jetson Orin NX 模块，提供高达 100 TOPS 的算力。
* **专为开发和生产而设计：** 配备丰富的 I/O 接口：2x USB3.2、HDMI、以太网、M.2 Key M、M.2 Key E、mini-PCIe、40 针 GPIO 等。支持多种有线和无线通信，包括 Wi-Fi 和 LTE
* **即刻投入市场：** 预装 JetPack5.1.3，Linux OS BSP 就绪
* **认证包括** ROHS、CE、FCC、KC、UKCA、REACH
* **长期供货保证：** 生产周期：至少到 2032 年

## 规格

[TABLE COMPRESSED]
Columns: 规格 [reComputer J3010B](https://www.seeedstudio.com/reComputer-J3010B-p-6404.html) [reComputer J3011B](https://www.seeedstudio.com/reComputer-J3011B-p-6405.html) [reComputer J4011B](https://www.seeedstudio.com/reComputer-J4011B-p-6407.html) [reComputer J4012B](https://www.seeedstudio.com/reComputer-J4012B-p-6406.html) | 模块 Jetson Orin Nano 4GB Jetson Orin Nano 8GB Jetson Orin NX 8GB Jetson Orin NX 16GB | AI 性能 20 TOPS 40 TOPS 70 TOPS 100 TOPS | GPU 512核 NVIDIA Ampere 架构 GPU，配备 16 个 Tensor 核心 1024核 NVIDIA Ampere 架构 GPU，配备 32 个 Tensor 核心 1024核 NVIDIA Ampere 架构 GPU，配备 32 个 Tensor 核心 | GPU 最大频率 625 MHz 765 MHz 918 MHz | CPU 6核 Arm® Cortex®-A78AE v8.2 64位 CPU 1.5MB L2 + 4MB L3 6核 Arm® Cortex®-A78AE v8.2 64位 CPU 1.5MB L2 + 4MB L3 8核 Arm® Cortex®-A78AE v8.2 64位 CPU 2MB L2 + 4MB L3 | CPU 最大频率 1.5 GHz 2 GHz | 内存 4GB 64位 LPDDR5 34 GB/s 8GB 128位 LPDDR5 68 GB/s 8GB 128位 LPDDR5 102.4GB/s 16GB 128位 LPDDR5 102.4GB/s | 深度学习加速器 / 1x NVDLA v2 2x NVDLA v2 | DLA 最大频率 / 614 MHz | 视觉加速器 / 1x PVA v2 | 存储 128GB NVMe SSD ...

## 刷写 JetPack

在这里，我们将向您展示如何将 [Jetpack](https://developer.nvidia.com/embedded/jetpack) 刷写到连接到 reComputer J4012B/ J4011B/ J3010B 和 J3011B 的 NVMe SSD 上。所有这些设备内部都配备了 J401B 载板，刷写过程对所有设备都是相同的。

reComputer J401B 系列在随附的 NVMe SSD 上预装了 JetPack 5.1.3，因此您无需刷写。但是，如果您想再次使用 JetPack 刷写，可以按照本指南操作。

### 支持的模块

* [NVIDIA® Jetson Orin™ Nano 模块 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5553.html)
* [NVIDIA® Jetson Orin™ Nano 模块 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5551.html?___store=retailer)
* [NVIDIA® Jetson Orin™ NX 模块 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5522.html)
* [NVIDIA® Jetson Orin™ NX 模块 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5523.html)

### 前提条件

* Ubuntu 主机电脑
* reComputer J4012B/ J4011B/ J3010B 或 J3011B
* USB Type-C 数据传输线

我们建议您使用物理 ubuntu 主机设备而不是虚拟机。
请参考下表准备主机。

[TABLE COMPRESSED]
Columns: JetPack 版本 Ubuntu 版本（主机电脑） | 18.04 20.04 22.04 | JetPack 5.x ✅ ✅ | JetPack 6.x ✅ ✅

* 我们不建议使用虚拟机和ARM架构的Ubuntu进行刷写。

### 进入强制恢复模式

在我们进行安装步骤之前，我们需要确保jetson设备处于强制恢复模式。

请参考以下步骤将jetson设备设置为强制恢复模式。

动画GIF中的载板是J401，但不用担心——J401和J401B载板进入强制恢复模式的步骤是相同的。

 分步说明 

**步骤 1.** 使用跳线连接 **FC REC** 引脚和 **GND** 引脚。

[TABLE COMPRESSED]
Columns: 按钮接头 描述 按钮接头 描述 | 1 PWR BTN 7 AUTO ON | 2 GND 8 DIS | 3 FC REC 9 UART TXD | 4 GND 10 UART RXD | 5 SYS RET 11 LED + | 6 GND 12 LED -

**步骤 2.** 通过连接随附的电源适配器线缆为 reComputer 供电，并使用 USB Type-C 数据传输线缆将开发板与 Ubuntu 主机 PC 连接

**步骤 3.** 在 Linux 主机 PC 上，打开终端窗口并输入命令 `lsusb`。如果返回的内容中包含以下输出之一（根据您使用的 Jetson SoM），则表示开发板处于强制恢复模式。

* 对于 Orin NX 16GB：**0955:7323 NVidia Corp**
* 对于 Orin NX 8GB：**0955:7423 NVidia Corp**
* 对于 Orin Nano 8GB：**0955:7523 NVidia Corp**
* 对于 Orin Nano 4GB：**0955:7623 NVidia Corp**

下图是 Orin NX 16GB 的示例

**步骤 4.** 移除跳线

### 刷写 Jetpack OS

在开始刷写之前，需要注意的是 Jetson Orin NX 模块仅支持 JetPack 5.1 及以上版本，而 Jetson Orin Nano 模块仅支持 JetPack 5.1.1 及以上版本。

首先，在开始刷写 JetPack 之前，请在 Ubuntu 主机 PC 上安装以下必需的依赖项。
```
sudo apt install qemu-user-static sshpass abootimg nfs-kernel-server libxml2-utils binutils -y
```* JP5.1.1* JP5.1.2* JP5.1.3* JP6.0* JP6.1* JP6.2

这里我们将使用 NVIDIA L4T 35.3.1 在 reComputer 上安装 Jetpack 5.1.1

**步骤 1：** 在主机 PC 上[下载](https://developer.nvidia.com/embedded/jetson-linux-r3531) NVIDIA 驱动程序。所需的驱动程序如下所示：

**步骤 2：** 通过导航到包含这些文件的文件夹来解压 **Jetson\_Linux\_R35.3.1\_aarch64** 和 **Tegra\_Linux\_Sample-Root-Filesystem\_R35.3.1\_aarch64**，应用更改并安装必要的先决条件
```
tar xf Jetson_Linux_R35.3.1_aarch64  
sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_R35.3.1_aarch64 -C Linux_for_Tegra/rootfs/  
cd Linux_for_Tegra/  
sudo ./apply_binaries.sh  
sudo ./tools/l4t_flash_prerequisites.sh
```**步骤 3（可选）：** 配置您的用户名、密码和主机名，这样您就不需要在设备完成启动后进入 Ubuntu 安装向导
```
sudo tools/l4t_create_default_user.sh -u {USERNAME} -p {PASSWORD} -a -n {HOSTNAME} --accept-license
```例如（用户名："nvidia"，密码："nvidia"，设备名称："nvidia-desktop"）：
```
sudo tools/l4t_create_default_user.sh -u nvidia -p nvidia -a -n nvidia-desktop --accept-license
```**步骤 4：** 将系统刷写到 NVMe SSD
```
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 \  
  -c tools/kernel_flash/flash_l4t_external.xml -p "-c bootloader/t186ref/cfg/flash_t234_qspi.xml" \  
  --showlogs --network usb0 p3509-a02+p3767-0000 internal
```如果刷写过程成功，您将看到以下输出

现在，您可以将鼠标、键盘和显示器连接到 Jetson 设备。它就可以使用了！

如果您的 Jetson 设备打开桌面需要很长时间，请重新连接电源。

**步骤 5（可选）：** 安装 Nvidia Jetpack SDK

请在 **Jetson 设备** 上打开终端并执行以下命令：
```
sudo apt update  
sudo apt install nvidia-jetpack
```这里我们将使用 NVIDIA L4T 35.4.1 在 reComputer 上安装 Jetpack 5.1.2

**步骤 1：** 在主机 PC 上[下载](https://developer.nvidia.com/embedded/jetson-linux-r3541) NVIDIA 驱动程序。所需的驱动程序如下所示：

**步骤 2：** 通过导航到包含这些文件的文件夹来解压 **Jetson\_Linux\_R35.4.1\_aarch64** 和 **Tegra\_Linux\_Sample-Root-Filesystem\_R35.4.1\_aarch64**，应用更改并安装必要的先决条件
```
tar xf Jetson_Linux_R35.4.1_aarch64.tbz2  
sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_R35.4.1_aarch64.tbz2 -C Linux_for_Tegra/rootfs/  
cd Linux_for_Tegra/  
sudo ./apply_binaries.sh  
sudo ./tools/l4t_flash_prerequisites.sh
```现在我们需要应用来自 NVIDIA 的补丁，这对于 JP5.1.2 是必需的，在官方 NVIDIA JetPack 发布说明的第 4.2.3 节中有[详细说明](https://docs.nvidia.com/jetson/archives/r35.4.1/ReleaseNotes/Jetson_Linux_Release_Notes_r35.4.1.pdf)。

**步骤 3：** 导航到以下目录
```
cd Linux_for_Tegra/bootloader/t186ref/BCT
```**步骤 4:** 打开文件 **"tegra234-mb2-bct-scr-p3767-0000.dts"** 并在 **tfc** 部分下添加以下行
```
tfc {  
    reg@322 { /* GPIO_M_SCR_00_0 */  
    exclusion-info = <2>;  
    value = <0x38008080>;  
    };
```**步骤 5（可选）：** 导航到 **"Linux\_for\_Tegra"** 目录，并输入以下命令来配置您的用户名、密码和主机名，这样设备启动完成后您就无需进入 Ubuntu 安装向导
```
cd Linux_for_Tegra  
sudo tools/l4t_create_default_user.sh -u {USERNAME} -p {PASSWORD} -a -n {HOSTNAME} --accept-license
```例如（用户名："nvidia"，密码："nvidia"，设备名称："nvidia-desktop"）：
```
sudo tools/l4t_create_default_user.sh -u nvidia -p nvidia -a -n nvidia-desktop --accept-license
```**步骤 6:** 将系统刷写到 NVMe 固态硬盘
```
cp p3509-a02+p3767-0000.conf p3509-a02-p3767-0000.conf  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1   -c tools/kernel_flash/flash_l4t_nvme.xml -p "-c bootloader/t186ref/cfg/flash_t234_qspi.xml --no-systemimg"   --showlogs --network usb0 p3509-a02-p3767-0000 external
```如果刷写过程成功，您将看到以下输出

现在，您可以将鼠标、键盘和显示器连接到 Jetson 设备。它就可以使用了！

如果您的 Jetson 设备打开桌面需要很长时间，请重新连接电源。

**步骤 7（可选）：** 安装 Nvidia Jetpack SDK

请在 **Jetson 设备** 上打开终端并执行以下命令：
```
sudo apt update  
sudo apt install nvidia-jetpack
```在这里我们将在 reComputer 上安装 Jetpack 5.1.3。

**步骤 1：** 根据您使用的 Jetson 模块，将相应的系统镜像下载到您的 Ubuntu PC：

[TABLE COMPRESSED]
Columns: Jetson 模块 下载链接 SHA256 | Orin NX 16GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EXpnEetKYeNEkVs_mrG161IBNt4Rn84D2l1mvX-RS6hBog?e=OUpkC2) 28877E13DE9E029C4E4328F836C7D534E182849714CCA2930C3712757DDD6CD1 | Orin NX 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EdchzEJ2fYJClYD680qFaosBNkYRXjHBLpYykpxYBi2_0Q?e=LEHd41) E4C5611164475D86E2F128826F993F251491368168218A2D660E6D23DEE63D53 | Orin Nano 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EUPTqRpD_fVGmw-qKTrRl4gBUB9YvlytoRGwxe7aCqhF9w?e=Bsr1GU) A3F0C30EFDFB612F1EAB5B01E01B7E6FDFACA6A27A596C3B0AABD82C0EFE94D4 | Orin Nano 4GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/ER4pJqYIOGVGiu1ticFeYMoBFaSpmI_JISciXqqvI-lzAA?e=nBRhmh) EDCDA822B59BB6FAC8E7AD301757C6801FC29481DE274DEE370CFDA4874AC0B0

为了验证下载固件的完整性，您可以比较 SHA256 哈希值。

在 Ubuntu 主机上，打开终端并运行命令 `sha256sum <文件>` 来获取下载文件的 SHA256 哈希值。如果得到的哈希值与 wiki 中提供的 SHA256 哈希值匹配，则确认您下载的固件是完整无损的。

**步骤 2：** 解压下载的镜像文件：
```
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-orin-nano-8g-j401-6.0-36.3.0-2024-06-07.tar.gz
```**步骤 3：** 导航到解压后的目录并执行以下命令将 jetpack 系统刷写到 NVMe SSD：
```
cd mfi_xxxx  
# For example: cd mfi_recomputer-orin-j401  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```如果刷写过程成功，您将看到以下输出

刷写命令可能需要运行 2-10 分钟。

**步骤 4：** 使用板上的 HDMI 连接器将 J401 连接到显示器，并完成初始配置设置。

请根据您的需要完成**系统配置**。

这里我们将使用 NVIDIA L4T 36.3 在 reComputer 上安装 Jetpack 6.0

**步骤 1：** 将对应您使用的 Jetson 模块的系统镜像下载到您的 Ubuntu PC：

[TABLE COMPRESSED]
Columns: Jetson 模块 下载链接1 下载链接2 SHA256 | Orin NX 16GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EavQHXoSEg9PuLs4vuujXLcB0-GW6Ti1zHGL2UHzgS6TWg?e=J7oRrf) [下载](https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/EbEZRxHDtgBDjBrHK_7ltfEB6JBa3VGXLx3meNc0OJUL_g?e=8MNsTg) 20b38d9524327fd714c37cb293036006e070b5335d6b4f6978a862be51c3db52 | Orin NX 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcfUdbmSiOBFo_Po-Cui3jkBDORKexZ4S43Jde5XApqdeQ?e=zqealW) [下载](https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/EQawJy3jmKBAmJgHght-vVUBHbsC3vtlvMsYfW7vsie3LQ?e=vor3t3) da966e7616ed86b45e184b6db9c3eb81e779a5f4524f6c3c5610e56c53532fe1 | Orin Nano 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EauK-aXvruxHsC1-bAmTwZkBNB0PsvPX6S6oV4Q1UrAUFw?e=rytWvU) [下载](https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/EeJP8SNF76BKiJg2e-FKNd4BhJwlWiMbLcT6Y286tRO7JQ?e=ct6qLf) e0fa101c5df6f507d123c2332e9fedea0ac54f8a5253cb28e71fdff01147fa68 | Orin Nano 4GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcHfrgY9GxVNiwGh6YTB50cBCc5QcKgnGpTZQfv94x4VNw?e=Rl73Zh) [下载](https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/ERQJluPq9X1LmpLXTSGZVMwBVg9ikWw8veG2aOdHv504Gw?e=hujab4) 80ebeac0a843baa2c3104ee6341d44f39a2cfab1c9c725e176c7b2a219b79dfc

为了验证下载固件的完整性，您可以比较 SHA256 哈希值。

在 Ubuntu 主机上，打开终端并运行命令 `sha256sum <文件>` 来获取下载文件的 SHA256 哈希值。如果得到的哈希值与 wiki 中提供的 SHA256 哈希值匹配，则确认您下载的固件是完整无损的。

**步骤 2：** 解压下载的镜像文件：
```
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-orin-nano-8g-j401-6.0-36.3.0-2024-06-07.tar.gz
```**步骤 3：** 导航到解压后的目录并执行以下命令将 jetpack 系统刷写到 NVMe SSD：
```
cd mfi_xxxx  
# For example: cd mfi_recomputer-orin-j401  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```如果刷写过程成功，您将看到以下输出

刷写命令可能需要运行 2-10 分钟。

**步骤 4：** 使用板上的 HDMI 连接器将 J401 连接到显示器，并完成初始配置设置：

请根据您的需要完成**系统配置**。

**步骤 5：** 启动系统后，您需要执行以下命令来重新激活无线网卡驱动程序：
```
sudo rm /lib/modules/5.15.136-tegra/build  
sudo ln -s /usr/src/linux-headers-5.15.136-tegra-ubuntu22.04_aarch64/3rdparty/canonical/linux-jammy/kernel-source/ /lib/modules/5.15.136-tegra/build  
sudo apt install -y iwlwifi-modules
```这里我们将使用 NVIDIA L4T 36.4 在 reComputer 上安装 Jetpack 6.1

**步骤 1：** 将对应您使用的 Jetson 模块的系统镜像下载到您的 Ubuntu PC：

[TABLE COMPRESSED]
Columns: Jetson 模块 下载链接 SHA256 | Orin NX 16GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EWCZOBNb9C9AoZe-mt23jLABZk942Lf0yopVGFJFTeL5DA?e=o7epES) 3e53f484eb41a2d81f01ba2a0512a3c13d86d90f646207a488eaf77ae0cd5d69 | Orin NX 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcvDRK7qgWhGty_H-P7yHZ8Bob3v9AEs_vFVd-zOC3WX5w?e=FmlfjD) fc22a3d1669eb311cf237b8f4252896bfb71ff860c14f7a502c60fda5439d99d | Orin Nano 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EeO8T8kNkpZGl9W2QfmnKYQBeXB8-M88aZWLMvPP7uARcA?e=fBuClA) c2e48b41d284e4c98a2bc3409f1a1d09c61e4b60d6a5bdec3a33d084560a3bba | Orin Nano 4GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EY01pL5oq0FAmavoRY_p9DMBj4t-LHzRtEAh1UBQen3S3g?e=jUfauO) b9e4f5889a66d055d967884980aee6357316acb562c4d713ef2fdb21f4644788

为了验证下载固件的完整性，您可以比较 SHA256 哈希值。

在 Ubuntu 主机上，打开终端并运行命令 `sha256sum <文件>` 来获取下载文件的 SHA256 哈希值。如果得到的哈希值与 wiki 中提供的 SHA256 哈希值匹配，则确认您下载的固件是完整无损的。

**步骤 2：** 解压下载的镜像文件：
```
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-orin-nx-16g-j401-6.1-36.4.0-2024-12-04.tar
```**步骤 3：** 导航到解压后的目录并执行以下命令将 jetpack 系统刷写到 NVMe SSD：
```
cd mfi_xxxx  
# For example: cd mfi_recomputer-orin-j401  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```如果刷写过程成功，您将看到以下输出

刷写命令可能需要运行 2-10 分钟。

**步骤 4：** 使用板上的 HDMI 连接器将 J401 连接到显示器，并完成初始配置设置：

请根据您的需要完成**系统配置**。

这里我们将使用 NVIDIA L4T 36.4.3 在 reComputer 上安装 Jetpack 6.2

**步骤 1：** 将对应您所使用的 Jetson 模块的系统镜像下载到您的 Ubuntu PC：

[TABLE COMPRESSED]
Columns: Jetson 模块 下载链接 SHA256 | Orin Nano 8GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/Ea8wqK7OE0VGtclEw1J0FIYB8I6qJEH_n1facfwl9AlhkQ?e=UoHjcf) D9ECF85D0BD52E6E90E9C567A52688C7FAEE7DD1BDC87ED557184086FD605249 | Orin Nano 4GB [下载](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EYuzr4pFfZ5Lp2WIqG_tZ7ABIYU9A0KuFl1nAs9FiGmZBQ?e=WALXR5) 00B881683FD2D61A22BD2D0326E7B5E39CB5C4F249BF2CD18A272766CB6612E7

要验证下载固件的完整性，您可以比较 SHA256 哈希值。

在 Ubuntu 主机上，打开终端并运行命令 `sha256sum <File>` 来获取下载文件的 SHA256 哈希值。如果得到的哈希值与 wiki 中提供的 SHA256 哈希值匹配，则确认您下载的固件是完整且完好的。

请注意，由于启用 `super mode` 后功耗和发热量增加，[reComputer J4011B](https://www.seeedstudio.com/reComputer-J4011B-p-6407.html) 和 [reComputer J4012B](https://www.seeedstudio.com/reComputer-J4012B-p-6406.html) 无法在最高模式下稳定运行。因此，此次更新不包括这两款产品。
我们目前正在设计新版本的 reComputer。敬请期待！

**步骤 2：** 解压下载的镜像文件：
```
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-orin-nano-8g-j401-6.2-36.4.3-2025-02-08.tar.gz
```**步骤 3：** 导航到解压后的目录并执行以下命令将 jetpack 系统刷写到 NVMe SSD：
```
cd mfi_xxxx  
# For example: cd mfi_recomputer-orin-j401  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```如果刷写过程成功，您将看到以下输出

刷写命令可能需要运行 2-10 分钟。

**步骤 4：** 使用板上的 HDMI 连接器将 J401 连接到显示器，并完成初始配置设置：

请根据您的需要完成**系统配置**。

## 接口使用

有关接口使用的更多信息，请参考此[wiki页面](/cn/recomputer_j401b_interfaces_usage/)。

## 资源

* [reComputer J401B 数据手册](https://files.seeedstudio.com/wiki/reComputer/reComputer_J401B_datasheet_v1.pdf)
* [reComputer J401B 原理图](https://files.seeedstudio.com/products/NVIDIA/reComputer_J401B_CarrierBoard_SCH_V1.0.pdf)
* [LTE 板原理图](https://files.seeedstudio.com/products/NVIDIA/reComputer_J401B_LTE_SCH_V1.0.pdf)
* [Seeed Jetson 系列目录](https://files.seeedstudio.com/wiki/Seeed_Jetson/Seeed-NVIDIA_Jetson_Catalog_V1.4.pdf)
* [Seeed Studio 边缘AI成功案例](https://www.seeedstudio.com/blog/wp-content/uploads/2023/07/Seeed_NVIDIA_Jetson_Success_Cases_and_Examples.pdf)
* [Seeed Jetson 系列对比](https://www.seeedstudio.com/blog/nvidia-jetson-comparison-nano-tx2-nx-xavier-nx-agx-orin/)
* [Seeed Jetson 设备单页介绍](https://files.seeedstudio.com/wiki/Seeed_Jetson/Seeed-Jetson-one-pager.pdf)
* [Jetson 示例](https://github.com/Seeed-Projects/jetson-examples)
* [reComputer-Jetson-for-Beginners](https://github.com/Seeed-Projects/reComputer-Jetson-for-Beginners)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。
