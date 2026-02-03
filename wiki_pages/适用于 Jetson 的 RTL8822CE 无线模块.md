# 适用于 Jetson 的 RTL8822CE 无线模块

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/wifi/RTL8822CE_Wireless_NIC_for_Jetson.png)

[**立即购买 🖱️**](https://www.seeedstudio.com/RTL8822CE-WIFI-Module-p-6313.html)

RTL8822CE 是一款紧凑的双频 WLAN+蓝牙组合 M.2 卡，集成了带有 PCI Express 控制器的 2T2R 双频 WLAN 子系统和带有 USB 支持的蓝牙 v5.0 子系统。兼容 IEEE 802.11 a/b/g/n/ac 标准，提供高达 867 Mbps 的最大 PHY 速率，并支持蓝牙双模（v5.0/v4.2/v2.1）。非常适合与嵌入式设备（如 [reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-p-5586.html)）配合使用，提供高性能的无线和蓝牙连接。

## 功能特性

* 支持 2.4G/5GHz 双频
* 无线 PHY 速率可达 867Mbps
* IEEE 标准：IEEE 802.11a/b/g/n/ac
* 外形规格：M.2 2230 通用 A 键或 E 键
* 通过 MHF4 连接器连接外部天线
* 电源供应：DC3.3V±0.2V 电源供应
* 支持 Linux、Windows 10/11 等

## 规格参数

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 芯片组 **TRL8822CE-CG**| WLAN 标准 IEEE802.11a/b/g/n/ac|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 蓝牙规格 Bluetooth Core Specification v5.0/4.2/2.1|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 主机接口 PCI Express 2.1 for WLAN & USB2.0 FS for Bluetooth|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 天线 通过 MHF4 连接器连接外部天线|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | 尺寸 M.2 30*22*2.15mm (L*W*H)| 电源供应 DC 3.3V±0.2V@ 1000mA(Max)|  |  |  |  | | --- | --- | --- | --- | | 工作温度 -20℃ to +70℃|  |  | | --- | --- | | 工作湿度 10% to 95% RH (Non-Condensing) | | | | | | | | | | | | | | | | | |

## 支持设备

* [reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-w-o-power-adapter-p-5628.html)
* [reComputer J4011](https://www.seeedstudio.com/reComputer-J4011-w-o-power-adapter-p-5629.html)
* [reComputer J3011](https://www.seeedstudio.com/reComputer-J3011-w-o-power-adapter-p-5630.html)
* [reComputer J3010](https://www.seeedstudio.com/reComputer-J3010-w-o-power-adapter-p-5631.html)

## 硬件连接

danger

在本 wiki 中，我们将以 reComputer J4012 为例，演示如何在 Jetson 设备上安装和配置 RTL8822CE 无线模块。

步骤 1. 准备所有将要使用的材料。

* 配备 Jetpack 5.1.2 的 reComputer J4012
* Infineon Wi-Fi 模块

步骤 2. 将无线模块插入 M.2 Key E 端口。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/wifi/rtl8822ce.jpg)

## 配置无线模块

我们可以直接访问 Jetson 桌面，通过 `Settings` --> `WiFi` 连接到 wifi 网络。

![](https://files.seeedstudio.com/wiki/reComputer/Hard_ware/Infineon_wifi_module/connect_to_wifi.png)

我们也可以通过 `Settings` --> `Bluetooth` 配置蓝牙。

info

此外，我们可以通过命令行配置无线模块，例如使用 `bluetoothctl` 命令配置蓝牙设备。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-bluetooth-test.png)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您对我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。