# reComputer Mini 硬件和接口使用

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/reComputer_mini.jpg)

本 wiki 介绍了 reComputer mini J40 系列上的各种不同硬件和接口，以及如何使用它们来扩展您的项目想法。

[**立即获取 🖱**](https://www.seeedstudio.com/reComputer-Mini-optional-accessories.html)

## 硬件接口概览

![](https://files.seeedstudio.com/wiki/recomputer_mini/hardware_overview.png)

## 电源

reComputer Mini 配备了 **12-54V (XT30)** 电源接口，兼容宽电压输入范围（12V 至 54V），使其适用于各种电源供应环境。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/power.png)

## 显示器

该产品配备了具有 Host + DP（DisplayPort）功能的 Type-C 端口，这意味着它不仅支持数据传输，还允许您通过此端口连接显示器，实现高质量的视频输出。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/display.png)

## 用于 WIFI 和蓝牙的 M.2 Key E

reComputer Mini 具有 M.2 Key E 接口，通过该接口您可以扩展设备的蓝牙和 Wi-Fi 功能。

我们推荐使用 Intel 双频 RTL8822CE 无线网卡。

### 硬件连接

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/wifi.png)

### 使用说明

安装 Wi-Fi 模块并为设备通电后，我们可以配置设备的 Wi-Fi 和蓝牙设置。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-wifi-bluetooth-test.gif)

当然，我们也可以使用以下命令检查设备的运行状态。

```
ifconfig
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/wifi_ifconfig.png)

```
bluetoothctl
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/bluetoothctl.png)

## M.2 Key M 用于 SSD

M.2 Key M 是一个专为高速固态硬盘（SSD）设计的接口，提供超快的数据传输速度，非常适合高性能应用。

开箱即用，reComputer Industrial 包含一个 128GB 工业级 SSD，连接到 M.2 Key M 插槽，支持 x4 PCIe Gen3，预装了 JetPack 系统。

### 硬件连接

如果您想要移除附带的 SSD 并安装新的 SSD，您需要确保您的 SSD 满足以下两个条件：

* 支持 **M.2 Key M 插槽，x4 PCIe Gen3** 接口。
* 符合 **2242** 尺寸规格。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/ssd.png)

### 使用说明

在 Jetson 设备中打开终端，输入以下命令来测试 SSD 的读写速度。

```
sudo dd if=/dev/zero of=tempfile bs=1M count=1024 conv=fdatasync
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/test_nvme.png)

danger

测试完成后，请运行 `sudo rm tempfile` 命令删除缓存文件。

## 以太网

### 硬件连接

reComputer Mini 在扩展板上配备了一个 **RJ45 千兆以太网端口（10/100/1000M）**。

![](https://files.seeedstudio.com/wiki/recomputer_mini/network_photo.png)

### 使用说明

在终端中输入 `ifconfig`，您可以看到以太网接口映射的设备名称是 `eth0`：

![](https://files.seeedstudio.com/wiki/recomputer_mini/network_ifconfig.png)

使用千兆以太网 RJ45 线缆将 **reComputer Mini** 连接到 **PC**。通过 `iperf` 工具，我们可以简单测试以太网接口的传输速率。
打开终端，在 **PC** 和 **reComputer Mini** 上都安装 `iperf3`。

```
sudo apt update  
sudo apt install iperf3
```

在PC上打开终端并输入 `iperf3 -s`。

![](https://files.seeedstudio.com/wiki/recomputer_mini/iperf3PC.jpg)

然后，在 **reComputer Mini** 上打开终端并输入 `iperf3 -c <你的PC的IP地址>`。
在这种情况下，我的PC网络接口的IP地址是 `192.168.12.211`。示例命令如下：

```
iperf3 -c 192.168.12.211
```

然后，根据下图所示的结果，您可以看到 reComputer Mini 的以太网传输速度可以达到千兆级别。

![](https://files.seeedstudio.com/wiki/recomputer_mini/networkspeed.jpg)

## USB

### 硬件连接

reComputer Mini 载板总共有 4 个 USB 端口：2 个 USB 3.2 Type-A 端口，1 个用于刷机的 USB 2.0 Micro-B 端口，以及 1 个 USB 2.0 GH1.25 端口。扩展板有 4 个 USB 3.0 Type-A 端口。

![](https://files.seeedstudio.com/wiki/recomputer_mini/USBshow.jpg)

在[数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_mini_datasheet_V1.0.pdf)中，您可以找到 **USB 2.0** 5 针 GH-1.25 接口的接线图，如下所示：

![](https://files.seeedstudio.com/wiki/recomputer_mini/usb2.0-datasheet.png)

我们可以参考以下步骤，通过 USB 3.2/USB 2.0/USB 3.0 将存储设备连接到 reComputer mini，以测试 USB 读写速度。**使用说明**将显示后续步骤。

![](https://files.seeedstudio.com/wiki/recomputer_mini/USBLINK.jpg)

### 使用说明

我们可以在 Jetson 终端中输入 `watch -n 1 lsusb -tv` 来探测 USB 端口。一旦连接了 USB 设备，该端口的详细信息将在此处显示。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/usb_lsusb.png)

通过 USB 3.2/USB 2.0/USB 3.0 连接存储设备后，在终端中输入以下命令查看存储设备映射的分区：

```
ls /dev/sd*
```

![](https://files.seeedstudio.com/wiki/recomputer_mini/sda1.png)

**/dev/sda1** 是通过 USB 连接的存储设备映射的分区。如果插入多个设备，它们可能具有不同的映射分区名称。例如：**/dev/sdb1**。

从 **GitHub** 拉取并运行测试程序来测量 USB 的写入和读取速度。该程序将写入然后读取 **1GB** 的临时数据，测试完成后将删除这些数据。
`sudo ./USBIO` 后面的参数取决于通过 USB 连接的存储设备的映射分区。

```
git clone https://github.com/jjjadand/Mini_USBIO_test.git  
cd Mini_USBIO_test/  
gcc -o USBIO USB_test.c  
sudo ./USBIO /dev/sda1
```

通过USB 3.2连接的外部SSD进行1GB数据传输的读写速度如下：

![](https://files.seeedstudio.com/wiki/recomputer_mini/usb-write-read.jpg)

该程序也适用于测试其他USB接口。

info

关于USB Micro-B接口的使用，请参考[此wiki](https://wiki.seeedstudio.com/cn/recomputer_jetson_mini_getting_started/)获取详细教程。

## UART

reComputer Mini载板有两个4针GH-1.25 UART接口：**UART1**和**UART-DEBUG**。

![](https://files.seeedstudio.com/wiki/recomputer_mini/uart_photo.png)

### UART1

#### 硬件连接

在[数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_mini_datasheet_V1.0.pdf)中，您可以找到**UART1** 4针GH-1.25接口的接线图，如下所示：

![](https://files.seeedstudio.com/wiki/recomputer_mini/uart1_datasheet.png)

要测试和监控**UART1**的发送和接收功能，请选择合适的[UART转USB](https://www.seeedstudio.com/USB-To-Uart-5V-3V3-p-1832.html?qid=eyJjX3NlYXJjaF9xdWVyeSI6InVhcnQgdXNiIiwiY19zZWFyY2hfcmVzdWx0X3BvcyI6MSwiY190b3RhbF9yZXN1bHRzIjoxMywiY19zZWFyY2hfcmVzdWx0X3R5cGUiOiJQcm9kdWN0IiwiY19zZWFyY2hfZmlsdGVycyI6InN0b3JlQ29kZTpbcmV0YWlsZXJdICYmIHF1YW50aXR5X2FuZF9zdG9ja19zdGF0dXM6WzFdIn0%3D)模块（根据您的需求），按照数据手册中的接线图进行连接，然后安装cutecom。

将一端连接到**UART1**的4针GH-1.25接口，另一端插入USB端口，确保Tx连接到Rx，Rx连接到Tx。
使用说明将显示后续步骤。

![](https://files.seeedstudio.com/wiki/recomputer_mini/UARTLINK.jpg)

![](https://files.seeedstudio.com/wiki/recomputer_mini/uart2usb.png)

#### 使用说明

系统识别的UART1串口号为：**/dev/ttyTHS1**。您可以通过在终端中输入以下命令来检查：

![](https://files.seeedstudio.com/wiki/recomputer_mini/ttyTHS.png)

安装**Cutecom**来测试**UART1**数据传输和接收：

```
sudo apt update  
sudo apt install cutecom
```

在两个不同的终端中打开 **Cutecom**。

```
sudo cutecom
```

根据下图设置参数：在一个终端中，为"device"选项选择 **/dev/ttyTHS1**。在另一个终端中，"device"应该**根据您使用的UART转USB模块来选择**。您可以在"Input"字段中输入消息来测试数据的传输和接收。

![](https://files.seeedstudio.com/wiki/recomputer_mini/cutecom_uart1.png)

![](https://files.seeedstudio.com/wiki/recomputer_mini/cutecom_uart.png)

### UART-DEBUG

#### 硬件连接

在[数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_mini_datasheet_V1.0.pdf)中，您可以找到UART-DEBUG 4针GH-1.25接口的接线图，如下所示：

![](https://files.seeedstudio.com/wiki/recomputer_mini/UART-DEBUG.png)

要测试**UART-DEBUG**，您还需要一个**UART转USB**模块，该模块应连接到您的**PC**，如下图所示。

![](https://files.seeedstudio.com/wiki/recomputer_mini/UARTDBdraw.png)

![](https://files.seeedstudio.com/wiki/recomputer_mini/UART-DEBUG_photo.jpg)

#### 使用说明

完成硬件连接后。

首先在您的PC上安装串口登录工具[**MobaXterm**](https://mobaxterm.mobatek.net/)。
然后在您的PC上打开\*\*"设备管理器"**来检查**UART转USB**模块映射的COM端口。
要测试**UART-DEBUG\*\*，您还需要一个**UART转USB**模块，该模块应连接到您的**PC**，如下图所示。

![](https://files.seeedstudio.com/wiki/recomputer_mini/mobax1.png)

在**PC**上打开[**MobaXterm**](https://mobaxterm.mobatek.net/)，点击"Session"，然后点击"Serial"。根据\*\*"设备管理器"\*\*中映射的COM端口选择相应端口，并将波特率设置为115200。

![](https://files.seeedstudio.com/wiki/recomputer_mini/mobax2.png)

输入用户名和密码后，您将通过**UART-DEBUG**登录到reComputer Mini的终端。

![](https://files.seeedstudio.com/wiki/recomputer_mini/mobax3.png)

## RTC

reComputer Mini具有RTC接口，即使在系统断电时也能提供准确的计时功能。

将带有JST连接器的3V CR2032纽扣电池连接到板上的2针1.25mm JST插座。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/rtc.png)

## FAN

reComputer Mini的板载风扇接口由nvfancontrol守护进程管理，该进程根据Jetson模块的运行状态自适应调节风扇转速。我们可以通过其配置文件`/etc/nvfancontrol.conf`来配置守护进程的工作模式。

note

更多信息，请查看[这里](https://docs.nvidia.com/jetson/archives/r36.3/DeveloperGuide/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html?highlight=fan#fan-profile-control)。

此外，我们可以使用**jtop**工具手动设置风扇转速。

您可以在终端中输入以下命令来安装**jtop**。

```
sudo apt update  
sudo apt install python3-pip -y  
sudo pip3 install jetson-stats
```

然后重启您的 reComputer Mini：

```
sudo reboot
```

安装 **jtop** 后，你可以在终端中启动它：

```
jtop
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/jtop.png)

## CAN

reComputer mini 具有两个 CAN 接口，扩展板上有四个外部 CAN 接口。**CAN0** 由两个 **XT30 连接器 (2+2)** 组成，而 **CAN1** 由两个 **4 针 GH-1.25** 连接器组成。

![](https://files.seeedstudio.com/wiki/recomputer_mini/can-photo.png)

### CAN0/CAN1 通信

#### 硬件连接

在[数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_mini_datasheet_V1.0.pdf)中，您可以找到 CAN0/CAN1 接口的接线图，如下所示：

![](https://files.seeedstudio.com/wiki/recomputer_mini/can1-datasheet.png)

![](https://files.seeedstudio.com/wiki/recomputer_mini/can0-datasheet.png)

在使用 CAN0 和 CAN1 之前，请拆下底盖并将两个 120Ω 终端电阻都设置为 ON 位置。

![](https://files.seeedstudio.com/wiki/robotics/Actuator/myactuator/7.png)

在这里，我们将演示以 125 kbps 的波特率从 CAN0 向 CAN1 连续发送数据 30 秒。
首先，如下图所示，将 CAN0 的信号线连接到 CAN1 的信号线。具体来说，将 **CAN0\_H 连接到 CAN1\_H**，将 **CAN0\_L 连接到 CAN1\_L**。

![](https://files.seeedstudio.com/wiki/recomputer_mini/CANdraw.jpg)

![](https://files.seeedstudio.com/wiki/recomputer_mini/CAN0toCAN1.jpg)

#### 使用说明

完成硬件连接后。

在终端中输入以下命令查看映射到 CAN0 和 CAN1 的设备名称：

```
ifconfig -a
```

这里，`can0` 对应 **CAN0** 接口，`can1` 对应 **CAN1** 接口。

![](https://files.seeedstudio.com/wiki/recomputer_mini/can_express.jpg)

在终端中安装 `can-utils`：

```
sudo apt-get update  
sudo apt-get install can-utils
```

打开一个**终端 1**并输入以下命令来监控从`can0`发送的数据字节数：

```
watch -n 1 'ifconfig can0 | grep "TX packets"'
```

打开一个**终端 2**。从 GitHub 拉取用于测试 CAN 通信的脚本并运行它：

```
git clone https://github.com/jjjadand/Mini_CANtest.git  
cd Mini_CANtest  
sudo ./canTest.sh
```

通过观察两个终端，您可以看到在**终端1**中，从**CAN0**发送的字节数正在增加。

![](https://files.seeedstudio.com/wiki/recomputer_mini/canTX.jpg)

**终端2**将打印**CAN1**从**CAN0**接收到的数据。

![](https://files.seeedstudio.com/wiki/recomputer_mini/canRX.jpg)

在在程序中使用 **CAN** 之前，你需要先启用它。在终端中运行以下命令：

```
sudo gpioset --mode=wait 0 106=0 #enable CAN1  
sudo gpioset --mode=wait 0 43=0 #enable CAN0
```

### CAN0 电源输出

**CAN0-PPOWER**的输出电压理论上等于reComputer Mini当前的**DC**输入电压。**DC**输入电压范围为`12-54V`。因此，\*\*CAN0 XT30 (2+2)\*\*的电源输出范围也是`12-54V`。

我们将为**DC**输入提供不同的电压，然后测量**CAN0-PPOWER**的输出电压。
使用稳定的电源和万用表，按照下图进行连接。

![](https://files.seeedstudio.com/wiki/recomputer_mini/CAN0connet.png)

当**DC**输入为`26.3V`时，万用表测量**CAN0-POWER**输出为`26.03V`。

![](https://files.seeedstudio.com/wiki/recomputer_mini/CAN0-power1.jpg)

当**DC**输入为`12.6V`时，万用表测量**CAN0-POWER**输出为`12.48V`。

![](https://files.seeedstudio.com/wiki/recomputer_mini/CAN0-power2.jpg)

根据上述测试结果，可以看出**CAN0-POWER**的输出接近**DC**输入。
如果您想了解更多详细信息，可以参考[原理图](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/reComputer_Mini_SCH.7z)。

## I2C

### 硬件连接

reComputer的扩展板具有两个**4针GH-1.25** IIC接口，IIC0和IIC1。

在[数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_mini_datasheet_V1.0.pdf)中，您可以找到IIC0/IIC1 4针GH-1.25接口的接线图，如下所示：

![](https://files.seeedstudio.com/wiki/recomputer_mini/IIC0-datasheet.jpg)

![](https://files.seeedstudio.com/wiki/recomputer_mini/IIC1-datasheet.jpg)

选择一个IIC接口设备进行测试；选择由您决定。这里使用一个[IIC接口传感器](https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-V2-0-DHT20-p-4967.html?qid=eyJjX3NlYXJjaF9xdWVyeSI6IkkyYyIsImNfc2VhcmNoX3Jlc3VsdF9wb3MiOjQ3LCJjX3RvdGFsX3Jlc3VsdHMiOjUxLCJjX3NlYXJjaF9yZXN1bHRfdHlwZSI6IlByb2R1Y3QiLCJjX3NlYXJjaF9maWx0ZXJzIjoic3RvcmVDb2RlOltyZXRhaWxlcl0gJiYgcXVhbnRpdHlfYW5kX3N0b2NrX3N0YXR1czpbMV0ifQ%3D%3D)连接到I2C0/I2C1进行测试。

这里的测试过程涉及扫描IIC0/IIC1上外部连接设备的地址。

![](https://files.seeedstudio.com/wiki/recomputer_mini/IICdraw.png)

### 使用说明

完成硬件连接后。

我们需要安装IIC测试工具。在扫描设备之前，在终端中输入以下内容：

```
sudo apt update  
sudo apt-get install i2c-tools
```

然后，在终端中输入以下命令以查看 IIC 总线上的映射名称。

```
i2cdetect -l
```

扩展板上的外部接口 **IIC0-J7** 对应 `i2c-1 i2c c240000.i2c`，外部接口 **IIC1-J7** 对应 `i2c-7 i2c c250000.i2c`。

![](https://files.seeedstudio.com/wiki/recomputer_mini/iic-l.jpg)

连接外部 I2C 设备并设置其地址后，打开两个不同的终端并输入以下命令来扫描 I2C0 和 I2C1：

```
sudo i2cdetect -y -r 1  
sudo i2cdetect -y -r 7
```

![](https://files.seeedstudio.com/wiki/recomputer_mini/iic0-addr.png)

![](https://files.seeedstudio.com/wiki/recomputer_mini/iic1-addr.png)

我们可以看到连接到 **I2C0** 的设备地址设置为 `0x15`，连接到 **I2C1** 的设备地址设置为 `0x19`。

## SPI

### 硬件连接

reComputer 的扩展板具有一个 **6 针 GH-1.25** 外部 SPI 接口。

在[数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_mini_datasheet_V1.0.pdf)中，您可以找到 SPI 6 针 GH-1.25 接口的接线图，如下所示：

![](https://files.seeedstudio.com/wiki/recomputer_mini/spi-datasheet.jpg)

如果您不使用外部 SPI 转 USB 模块，您可以自行连接 **6 针 GH-1.25** SPI 接口来测试数据传输和接收。将 **MOSI** 连接到 **MISO**，将 **CS0** 连接到 **SCK**。
接线图如下：

![](https://files.seeedstudio.com/wiki/recomputer_mini/SPIdraw.png)

![](https://files.seeedstudio.com/wiki/recomputer_mini/spi-photo.jpg)

### 使用说明

完成硬件连接后。

然后，从 GitHub 拉取 SPI 测试代码并编译：

```
git clone https://github.com/rm-hull/spidev-test  
cd spidev-test  
gcc spidev_test.c -o spidev_test
```

在终端中输入以下命令来查看SPI映射的设备名称。例如，`/dev/spidev0.0`对应扩展板上的SPI0（J17）。

```
ls -l /dev/spi*
```

![](https://files.seeedstudio.com/wiki/recomputer_mini/spi-dev.png)

在终端中输入以下命令来运行 SPI 测试程序：

```
sudo ./spidev_test -v
```

您可以在扩展板（J17）上观察到在SPI0上传输和接收的数据。

![](https://files.seeedstudio.com/wiki/recomputer_mini/spi-res.jpg)

## 资源

* [reComputer Mini 数据手册](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_mini_datasheet_V1.0.pdf)
* [reComputer Mini 原理图](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/reComputer_Mini_SCH.7z)
* [reComputer Mini 3D 模型](https://files.seeedstudio.com/wiki/reComputer-Jetson/mini/reComputer_Mini_3D.7z)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。