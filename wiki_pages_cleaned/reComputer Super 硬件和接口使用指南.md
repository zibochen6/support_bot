# reComputer Super 硬件和接口使用指南

本 wiki 介绍了 reComputer Super 上的各种不同硬件和接口，以及如何使用它们来扩展您的项目想法。

## CSI 摄像头

reComputer Super 支持标准的 4 个 MIPI CSI 摄像头进行图像和视频捕获。请按照以下步骤连接和测试您的摄像头。

### 硬件连接

**步骤 1.** 打开 Recomputer Super 的后盖。

**步骤 2.** 将 MIPI CSI 摄像头连接到 reComputer Super 板上相应的 CSI 端口。

**步骤 3.** 固定摄像头并确保连接牢固。

### 使用说明

在使用 CSI 摄像头之前，请确保您已安装了包含必要摄像头驱动程序的 JetPack 版本。

**步骤 1.** 检查系统是否识别摄像头：
```
ls /dev/video*
```**步骤 2.** （可选）如果尚未安装视频工具，请安装：
```
sudo apt install v4l-utils
```**步骤 3.** 使用以下命令启动摄像头并显示视频流：
```
nvgstcapture-1.0 --sensor-id=0
```如果您有多个摄像头，请将 `--sensor-id` 更改为适当的值。

---

## USB

reComputer Super 总共有 4 个 USB 3.2 端口和 1 个用于调试的 USB 2.0 Type-C 端口。

### USB 3.2 端口

我们可以在 Jetson 终端中输入 `watch -n 1 lsusb -tv` 来探测 USB 端口。一旦连接了 USB 设备，该端口的详细信息将显示在这里。

此外，您可以使用 `dd` 命令测试 USB 存储设备的读写速度：

* **读取：**
```
  sudo dd if=/dev/sda of=/dev/null bs=1024M count=5 iflag=direct
  ```* **写入：**
```
  sudo dd if=/dev/zero of=/dev/sda bs=1024M count=5 conv=fdatasync
  ```### USB 2.0 Type-C 端口

使用此串行端口，通过 USB C 数据线，您可以在 PC 端监控输入和输出的调试信息。

**步骤 1.** 将开关切换到调试模式。

**步骤 2.** 通过 USB 数据线连接 PC，在您的 PC 上下载 [CP210X 驱动程序](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads)。

**步骤 3.** 通过 USB 数据线连接 PC，解压下载的文件并在您的 PC 上安装驱动程序。

**步骤 4.** 在您的 Windows PC 上打开设备管理器，检查分配给 reComputer Super 的 COM 端口号。它应该在"端口 (COM 和 LPT)"下显示为"Silicon Labs CP210x USB to UART Bridge (COMX)"，其中 X 是 COM 端口号。

**步骤 5.** 打开串行端口工具（这里我们以 MobaXterm 工具为例），创建一个新会话。

**步骤 6.** 选择串行工具。

**步骤 7.** 选择相应的串行端口，将波特率设置为 115200 并点击 "OK"。

**步骤 8.** 使用用户名和密码登录您的 reComputer Super。

## M.2 Key M

M.2 Key M 是为高速固态硬盘（SSD）设计的接口，提供超快的数据传输速度，非常适合高性能应用。

### 支持的 SSD 如下

* [128GB NVMe M.2 PCle Gen3x4 2280 内置 SSD](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html)
* [256GB NVMe M.2 PCle Gen3x4 2280 内置 SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-256GB-p-5333.html)
* [512GB NVMe M.2 PCle Gen3x4 2280 内置 SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-512GB-p-5334.html)
* [1TB NVMe M.2 PCle Gen3x4 2280 内置 SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-1TB-p-5767.html)
* [2TB NVMe M.2 PCle Gen3x4 2280 内置 SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-2TB-p-6265.html)

### 硬件连接

### 使用说明

在 Jetson 设备中打开终端并输入以下命令来测试 SSD 的读写速度。
```
#create a blank test file first  
sudo touch /ssd/test  
dd if=/dev/zero of=/home/seeed/ssd/test bs=1024M count=5 conv=fdatasync
```测试完成后，请运行 `sudo rm /home/seeed/ssd/test` 命令删除缓存文件。

## M.2 Key E

M.2 Key E 接口是一个紧凑的高速数据接口，专为 Wi-Fi 和蓝牙等无线通信模块设计，用于扩展无线功能。

### 硬件连接

### 使用说明

安装 Wi-Fi 模块并开机后，我们可以配置设备的 Wi-Fi 和蓝牙设置。

当然，我们也可以使用以下命令检查设备的运行状态。
```
ifconfig
```**蓝牙：**
```
bluetoothctl  
scan on
```## Mini PCIe

reComputer super 配备了一个用于 LTE 4G 模块的 mini-PCIe。

#### 硬件连接

如果您想取出 SIM 卡，请推入卡片以触发内部弹簧，这样 SIM 卡就会从插槽中弹出

### 使用说明

**步骤 1.** 安装 minicom：
```
sudo apt update  
sudo apt install minicom -y
```**步骤 2.** 进入连接的 4G 模块的串行控制台，这样我们就可以输入 AT 命令并与 4G 模块交互：
```
sudo minicom -D /dev/ttyUSB2 -b 115200
```**步骤 3.** 按 Ctrl+A 然后按 E 打开本地回显。

**步骤 4.** 输入命令 "AT" 并按回车。如果您看到响应为 "OK"，则 4G 模块工作正常。

**步骤 5.** 输入命令 "ATI" 检查模块信息。

使用 4G 网络进行互联网访问

## RTC

reComputer Super 具有 RTC 接口，即使在系统断电时也能提供准确的计时。

### 硬件连接

将 3V CR1225 纽扣电池连接到板上的 RTC 插座，如下所示。确保电池的\*\*正极（+）\*\*端朝上。

### 使用说明

**步骤 1.** 如上所述连接 RTC 电池。

**步骤 2.** 打开 reComputer Super。

**步骤 3.** 在 Ubuntu 桌面上，点击右上角的下拉菜单，导航到 `Settings > Date & Time`，通过以太网线连接到网络并选择 **Automatic Date & Time** 以自动获取日期/时间。

如果您没有通过以太网连接到互联网，您可以在这里手动设置日期/时间。

**步骤 4.** 打开终端窗口，执行以下命令检查硬件时钟时间：
```
cat /sys/devices/platform/bpmp/bpmp\:i2c/i2c-4/4-003c/nvvrs-pseq-rtc/rtc/rtc0/time
```.png)

**步骤 5.** 断开网络连接并重启设备。您会发现系统时间已断电但仍正常运行。

## 以太网

reComputer Super 上有 2 个 RJ45 千兆以太网端口，支持 10/100/1000M。ETH0 是原生以太网端口，另一个 ETH1 是从 PCIe 转换而来的。

每个以太网端口上有 2 个 LED 指示灯（绿色和黄色）：

* 绿色 LED：仅在连接到 1000M/10G 网络时点亮。
* 黄色 LED：显示网络活动状态。

测试以太网速度：
```
iperf3 -c 192.168.254.100 -R
```-c `<ip address>` 是服务器 IP 地址，-R 表示反向模式。
```
iperf3 -c 192.168.254.100
```## LED 指示灯

reComputer Super 配备了 2 个 LED 指示灯（PWR 和 ACT）来显示电源状态和系统活动，允许用户实时监控设备运行状态。

## 风扇

reComputer Super 配备了两种类型的风扇连接器，以满足不同的电压和散热需求：

* 1x 4 针风扇连接器（5V PWM）：专为低电压、低功耗静音风扇设计，此连接器支持 PWM 速度控制，允许根据系统温度智能调节风扇速度，以提高能效并降低噪音。
* 1x 4 针风扇连接器（12V PWM）：兼容标准 12V PWM 风扇，同样支持精确的速度控制，非常适合高性能散热需求。

### 硬件连接

更多信息，请查看[这里](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html?highlight=fan#fan-profile-control)。

**设置风扇速度：**
```
sudo -i  
echo 100 > /sys/bus/platform/devices/pwm-fan/hwmon/hwmon1/pwm1
```此外，我们可以使用 jtop 工具手动设置风扇速度。

## CAN

reComputer Super 系列提供了一个 CAN 接口，其中 CAN 信号直接从 SOM 以 TTL/CMOS 电平输出，这是一个非标准差分信号，需要外部 CAN 收发器才能连接到标准 CAN 总线；它支持 CAN FD 帧格式，允许扩展数据长度和更高的数据速率，适用于工业自动化、机器人、汽车原型设计和其他需要可靠实时通信的应用。

### 硬件连接

请注意连接线的顺序（R OUT ↔ RX，D IN ↔ TX），然后通过 CAN 总线收发器将它们转换为 CAN\_L 和 CAN\_H。

根据 [reComputer Super 数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_super_user_manual.pdf)，以相应的方式将 CAN 加热器连接到 CAN 总线收发器，然后将 CAN 总线收发器连接到 [USB to CAN Analyzer Adapter](https://www.seeedstudio.com/USB-CAN-Analyzer-p-2888.html)，最后连接到 Jetson 进行环回通信测试。

### 使用说明

**步骤 1.** 配置并打开 can0：
```
sudo ip link set can0 down  
sudo ip link set can0 type can bitrate 500000  
sudo ip link set can0 up
```**步骤 2.** 通信测试。
打开一个终端来接收信号。
```
candump can0
```**步骤 3.** 打开另一个终端来发送信号。
```
cansend can0 123#abcdabcd
```## 扩展端口

扩展端口包括一个 40 针扩展接头和一个 12 针控制和 UART 接头，为外设和通信接口提供多样化的连接选项。

### 40 针扩展接头

40 针扩展接头是一个多功能扩展接口，提供各种功能，如 GPIO、I2C、SPI 和 UART，便于连接传感器、外设或其他模块。

40 针接头的详细信息如下所示：

[TABLE COMPRESSED]
Columns: 接头引脚 信号 BGA 引脚 默认功能 | 1 3.3V - 主 3.3V 供电 | 2 5V - 主 5V 供电 | 3 I2C1\_SDA PDD.02 I2C #1 数据 | 4 5V - 主 5V 供电 | 5 I2C1\_SCL PDD.01 I2C #1 时钟 | 6 GND - 接地 | 7 GPIO09 PAC.06 通用输入/输出 | 8 UART1\_TXD PR.02 UART #1 发送 | 9 GND - 接地 | 10 UART1\_RXD PR.03 UART #1 接收 | 11 UART1\_RTS PR.04 UART #1 请求发送 ...

### 使用说明

简单的 GPIO 控制示例
```
#install  
sudo apt-get install gpiod  
  
# Search for the corresponding number for the pin  
sudo gpiofind PH.00  
gpiochip0 43  
  
#Set the pin to H, then press Enter to release.  
sudo gpioset --mode=wait 0 43=1  
  
#Set the Pin to L, then press Enter to release.  
sudo gpioset --mode=wait 0 43=0  
  
#gpio 0_119 Low level maintained for 2 seconds  
sudo gpioset --mode=time -s 2 0 119=0  
  
#input  
sudo gpioget 0 43
```**如果您想配置默认未启用的 GPIO，请参考以下步骤：**

启用 40 针接头：
```
  sudo /opt/nvidia/jetson-io/jetson-io.py
```保存并重启。

**通过 Overlay 配置来配置未受控制的 GPIO：**

**步骤 1.** 下载并解压 [overlay 包](https://files.seeedstudio.com/wiki/overlay.zip) 到您的 jetson 设备。
```
wget https://files.seeedstudio.com/wiki/overlay.zip
```**步骤 2.** 将 build.sh 和 gpio-overlay.dts 复制到 Jetson。

**步骤 3.** 编辑 `pio-overlay.dts` 文件并修改它以包含您需要的引脚的 pinmux 定义。

更多详细信息请参见 [jetson-orin-nx-and-orin-nano-series-pinmux-config](https://developer.nvidia.com/downloads/jetson-orin-nx-and-orin-nano-series-pinmux-config-template)

**步骤 3.** 启用覆盖配置。
```
sudo bash ./build.sh  
#The following command needs to be executed only once.  
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "seeed gpio config Overlay"
```**步骤 4.** 重启设备以使配置生效。
```
sudo reboot
```**步骤 5.** 现在您可以通过 `gpioset` 控制刚刚修改的引脚。
```
#For example px7  
sudo gpioset --mode=wait 0 121=1
```### 12 引脚控制和 UART 接头

12 引脚控制和 UART 接头提供了用于连接和管理外部设备的基本控制信号和 UART 通信接口。

reComputer Super 的引脚功能与 reComputer Classic 类似。更多详细信息，请参考[这里](https://wiki.seeedstudio.com/cn/J401_carrierboard_Hardware_Interfaces_Usage/#gpio)。

## HDMI

reComputer Super 配备了 HDMI 2.1 Type A 端口，支持 7680x4320 分辨率。这允许超高清视频输出。

## 资源

* [用户手册和数据表](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_super_user_manual.pdf)
* [温度测试报告](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_Super_Temperature_Test_Report.pdf)
* [原理图](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer%20Super%20J401_v1.0_SCH_PDF_250401.pdf)
* [3D 文件](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer%20Super%20J401.stp)
* [机械文档-reComputer Super](https://files.seeedstudio.com/products/NVIDIA-Jetson/Mechanical_reComputer_Super.dxf)
* [机械文档-reComputer Super PCBA](https://files.seeedstudio.com/products/NVIDIA-Jetson/Mechanical_reComputer_Super_PCBA.dxf)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。
