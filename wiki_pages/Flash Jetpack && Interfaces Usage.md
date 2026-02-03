# Robotics J501 carrier board Hardware and Getting Started

The reComputer Robotics J501 Mini is a compact, high-performance edge AI carrier board designed for advanced robotics. Compatible with NVIDIA Jetson AGX Orin modules (32GB/64GB) in MAXN mode, it delivers up to 275 TOPS of AI performance. Equipped with extensive connectivity options—including dual Gigabit Ethernet ports, M.2 slots for 5G and Wi-Fi/BT modules, 2 USB 3.2 ports, CAN, GMSL2 (via optional expansion), I2C, and UART—it serves as a powerful robotic brain capable of processing complex data from various sensors. Pre-installed with JetPack 6.2.1 and Linux BSP, it ensures seamless deployment.​

Supporting frameworks like NVIDIA Isaac ROS, Hugging Face, PyTorch, and ROS 2/1, the reComputer Robotics J501 Mini bridges large language model-driven decision-making with physical robotics control, such as motion planning and sensor fusion. Ideal for the rapid development of autonomous robots, it accelerates time-to-market with ready-to-use interfaces and optimized AI frameworks.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/2-100020039-reComputer-Mini-J501---Carrier-Board-for-Jetson-AGX-Orin.jpg)

[**Get One Now 🖱**](https://www.seeedstudio.com/reComputer-Robotics-J401-Carrier-Board-optional-accessories.html)

## reComputer Jetson Robotics J501-Mini Carrier Board overview

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Top View**|  |  |  |  |  | | --- | --- | --- | --- | --- | | fig1| **side View**| fig2| **bottom View**| fig3 | | | | | |

## 📝 Part List

* reComputer Robotics J501-Mini Carrier Board x 1
* Power Supply and JST expansion board x 1
* XT30 to DC cable x 1
* USB Cable, Type A to Type C x 1
* Heat Sink for expansion board x 1
* Stud(M3\*30) x 5
* M3 Hexagon nut x 5
* Screw(CM2.5\*L.4) for Jetson Module and M.2 Key M x3
* Screw(CM2\*3.0) for M.2 Key E x1
* Stud(M2\*2.0) for M.2 Key B x1
* Screw(CM3\*4.0) for M.2 Key B x1
* User Manual x 1

note

1.Please design a robust heat dissipation solution according to the Thermal Design Guide, when in high voltage power supply and operating temperature.
2.Please attach heat sink for module for better performance.
3.During the operation with high voltage input and high load, please do not touch the heat sink to prevent scalding.
4.Power Adapter Recommendation for Validation, please use the power adapter recommended on the Seeed official website.

* 19V/4.74A 5525 Barrel Jack Power Adapter
* Ensure maximum power consumption requirements are met.
  2.AC Power Cord Compatibility
* Purchase region-specific AC cloverleaf power cords according to your location.
  3.Accessory Compatibility
* Use only officially recommended accessories (e.g., wireless modules, cameras, peripherals) for optimal performance and compatibility.

## 🔍 Specification

### Carrier Board Specifications

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Category Item Details|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Storage M.2 KEY M PCIe 1x M.2 KEY M PCIe (M.2 NVMe 2280 SSD)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Networking M.2 KEY E 1x M.2 Key E for WiFi/Bluetooth module|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Ethernet 1x RJ45 10GbE && 1x RJ45 1GbE|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | I/O USB 2x USB 3.2 Type-A (10Gbps); 1x USB 2.0 Type C (Debug); 1x USB 3.0 Type C (Recovery/Debug)| Camera 2x 4 in 1 GMSL2 Mini-Fakra Connector (Optional);|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | CAN 2x CAN JST 4-Pin Connector(GH 1.25);|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | DI/DO 1x DI JST 6-Pin Connector(GH 1.25); 1x DO JST 5-Pin Connector(GH 1.25);| I2S 1x I2S JST 6-Pin Connector(GH 1.25)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | RS485 1x RS-485 JST 4-Pin Connector(GH 1.25)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | UART 1x UART JST 6-Pin Connector (Multiplexed with DO)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Display 1x HDMI 2.1|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Fan 1x 4 Pin Fan Connector(12V PWM)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Extension Port 2x Camera Expansion Header (for GMSL2 board)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | RTC 1x RTC 2-pin;|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | LED 1x PWR LED, Green; 1x SSD LED, Green; 1x USR LED, RGB| Button 1x Recovery Button; 1x RESET Button| Power 19-48V XT30 (XT30 to 5525 DC Jack Cable included)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Jetpack Version Jetpack 6.2.1|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Mechanical Dimensions (W x D x H) 115mm x 115mm x 38mm|  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Weight 200g|  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Installation Desk, Wall-mounting|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Operating Temperature -20℃~60℃ (25W Mode); -20℃~55℃ (MAXN Mode); (with reComputer Robotics heat sink with fan)| Warranty 2 Years|  |  |  | | --- | --- | --- | | Certification RoHS, REACH, CE, FCC, UKCA, KC | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

## 📦 Flash JetPack OS

### Supported Module

* [NVIDIA® Jetson AGX Orin™ Module 64GB](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Orin-Module-64GB-p-5957.html)
* [NVIDIA® Jetson AGX Orin™ Module 32GB](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Orin-Module-32GB-p-5956.html)

### Prerequisites

* Ubuntu host PC
* Robotics J501 Mini Carrier Board
* NVIDIA® Jetson AGX Orin Module
* Nano/NX Module Active Fan
* NVMe M.2 2280 Internal SSD
* USB Type-C data transmission cable

info

We recommend that you use physical ubuntu host devices instead of virtual machines.
Please refer to the table below to prepare the host machine.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| JetPack Version Ubuntu Version (Host Computer)|  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | 18.04 20.04 22.04|  |  |  |  | | --- | --- | --- | --- | | JetPack 6.x ✅ ✅ | | | | | | | | | | |

### Prepare the Jetpack Image

Here, we need to download the system image to our Ubuntu PC corresponding to the Jetson module we are using:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jetpack Version Jetson Module GMSL Download Link1 SHA256|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 6.2.1 AGX Orin 64GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQDxBYYGqIfaSZqJT3uPt0alAa47BjjqCGvXWhD5tBsKx1M?e=3SW4Jf) f0efee5f265dbaef49dc14d517b269e 7f6582ff9977d9193d377966f36408ec3| AGX Orin 32GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQBohA1Z3GuSSJ7tFOQU8v22AYu8NNk9AS-1Cne78jOnSHw?e=dejuH9) 0a97cbb6d708776bd97608594c60c3 4208b5d5dc6efbfc5553edd9c5a95802f6 | | | | | | | | | | | | | |

danger

The Jetpack6 image file is approximately **14.2GB** in size and should take around 60 minutes to download. Please kindly wait for the download to complete.

info

To verify the integrity of the downloaded firmware, you can compare the SHA256 hash value.

On an Ubuntu host machine, open the terminal and run the command `sha256sum <File>` to obtain the SHA256 hash value of the downloaded file. If the resulting hash matches the SHA256 hash provided in the wiki, it confirms that the firmware you downloaded is complete and intact.

⚙️ **All `.dts` files and other source code for SEEED's Jetson carrier boards can be downloaded from** [Linux\_for\_Tegra](https://github.com/Seeed-Studio/Linux_for_Tegra)

### Enter Force Recovery Mode

info

Before we can move on to the installation steps, we need to make sure that the board is in force recovery mode.

 Step-by-Step 

**Step 1.** Keep pressing button to the RESET mode.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/reset.png)

**Step 2.** Power up the carrier board by connecting the power cable, then release **REC** button .

**Step 3.** Connect the board to the Ubuntu host PC with a USB Type-C data transmission cable.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/flash-port.png)

**Step 4.** On the Linux host PC, open a Terminal window and enter the command `lsusb`. If the returned content has one of the following outputs according to the Jetson SoM you use, then the board is in force recovery mode.

* For AGX Orin 32GB: **0955:7223 NVidia Corp**
* For AGX Orin 64GB: **0955:7023 NVidia Corp**

The below image is for AGX Orin 32GB:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/lsusb.png)

### Flash to Jetson

**Step 1:** Extract the downloaded image file:

```
cd <path-to-image>  
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-mini-agx-orin-32g-j501-6.2.1-36.4.4-2025-09-08.tar.gz
```

**Step 2:** Execute the following command to flash jetpack system to the NVMe SSD:

```
cd mfi_xxxx  
# For example: cd mfi_recomputer-orin-robotics-j501   
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```

You will see the following output if the flashing process is successful

![](https://files.seeedstudio.com/wiki/reComputer-J4012/4.png)

note

The flash command may run for 2-10 minutes.

**Step 3:** Connect the Robotics J501-Mini to a display use the PD to HDMI adapter to connect to a display that supports HDMI input, or directly connect to a display that supports PD input using the PD cable, and finish the initial configuration setup:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/J401/jetpack6_configuration.png)

info

Please complete the **System Configuration** according to your needs.

## 🔌 Interfaces Usage

The following will introduce the various interfaces of the Robotics j501-Mini board and how to use them.

## M.2 Key M

M.2 Key M is designed for high-speed NVMe SSDs, providing ultra-fast data transfer for robotics applications.

### Supported SSD are as follows

* [128GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html)
* [256GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-256GB-p-5333.html)
* [512GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-512GB-p-5334.html)
* [1TB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-1TB-p-5767.html)
* [2TB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-1TB-p-5767.html)

### Hardware Connection

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/nvme-real.png)

### Usage Instruction

Before testing the SSD read/write speed, you need to enter the following in the Jetson terminal:

```
sudo apt update  
sudo apt install smartmontools  
sudo smartctl -i /dev/nvme0n1
```

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/nvme-t.png)

Create a script file to test SSD read/write speed:

```
#You need to create a blank test file first  
cat <<'EOF' | sudo tee test_nvme.sh >/dev/null  
#!/usr/bin/env bash  
set -e  
  
sudo dd if=/dev/zero of=test bs=1000M count=1 conv=fdatasync  
sleep 1  
sudo sh -c "sync && echo 3 > /proc/sys/vm/drop_caches"  
sleep 1  
sudo dd if=test of=/dev/null bs=1000M count=1  
sudo rm -rf test  
EOF
```

Run the script to test SSD read/write speed:

```
sudo chmod +x test_nvme.sh  
./test_nvme
```

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/nvme-t2.png)

## M.2 Key E

The M.2 Key E interface is a standard M.2 connector primarily used for connecting wireless modules, such as Wi-Fi and Bluetooth, to expand wireless communication capabilities.

### Hardware Connection

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/KEY-E.png)

### Usage Instruction

To test Wi-Fi performance, use the following command (replace the IP address with your test server):

```
iperf3 -c 192.168.6.191
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/robotics_j401/wifi_speed.png)

Bluetooth functionality is available via the M.2 Key E slot.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/robotics_j401/bluetooth.png)

## Ethernet

The Robotics j501-Mini carrier board features one 1Gbps and one 10Gbps RJ45 Ethernet ports for high-speed wired network connectivity.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/ethernet-real.png)

To test Ethernet port speed, use `iperf3` as follows :

```
iperf3 -c <server_ip> -B <bind_ip>
```

info

`<server_ip>` is the IP address of the iperf3 server. The client will connect to this server to perform a bandwidth test.
`<bind_ip>` binds the specified local IP address as the source of the test traffic.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/ethernet-speed.png)

## LED

The J501 mini has two LEDs that can be controlled. The following demonstrates how to control the LEDs to be **green**, **red**, or **blue**.

### Usage Instruction

The reference commands for controlling the LEDs are as follows:

```
#change to red  
echo 1 | sudo tee /sys/class/leds/on-board:red/brightness  
echo 0 | sudo tee /sys/class/leds/on-board:red/brightness  
#change to green  
echo 1 | sudo tee /sys/class/leds/on-board:green/brightness  
echo 0 | sudo tee /sys/class/leds/on-board:green/brightness  
  
#change to blue  
echo 1 | sudo tee /sys/class/leds/on-board:blue/brightness  
echo 0 | sudo tee /sys/class/leds/on-board:blue/brightness
```

The LED control effect is shown in the figure below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/led-rg.jpg)![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/led-gg.jpg)![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/led-bg.jpg)

## USB

The Robotics j501-Mini carrier board is equipped with a variety of USB ports, including 2 USB 3.2 Type-A ports (10Gbps), a USB 3.0 Type-C port , and a USB 2.0 Type-C port for device mode/debugging, offering versatile connectivity options.

### USB-A Speed Test

Create a script to test USB device speed:

```
sudo vim test_usb
```

Paste the following content:

```
cat <<'EOF' | sudo tee test_usb.sh >/dev/null  
#!/bin/bash  
sudo dd if=/dev/zero of=/dev/$1 bs=1000M count=2 conv=fdatasync  
sleep 1  
sudo sh -c "sync && echo 3 > /proc/sys/vm/drop_caches"  
sleep 1  
sudo dd if=/dev/$1 of=/dev/null bs=1000M count=2  
EOF
```

Make the script executable and test:

```
sudo chmod +x test_usb  
./test_usb
```

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/usba-test.png)

### USB 2.0 Type-C port

Using this serial port, via the USB-C data cable, you can monitor the debugging information of input and output on the PC side.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/debug-port-real.png)

On your PC (not the Jetson), install a serial port login tool and log in to `/dev/ttyUSB0` (it might also be `ttyUSB1`, 2):

```
sudo apt update  
sudo apt install screen  
screen /dev/ttyUSB0 115200
```

You can then control the Jetson's terminal via the serial port on another Linux host, as shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/login-usb.png)

## Fan

The reComputer Jetson Robotics j501-Mini is equipped with:

* 1x 4-Pin Fan Connector (12V PWM): Compatible with standard 12V PWM fans, it also supports precise speed control, making it ideal for high-performance cooling requirements.

### Hardware Connection

The Robotics J501 Mini provides a standard 4-pin header for Fan.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/fan0.png)

The **Fan** datasheet schematic is shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/fan1.png)

The pin definitions for **J1** are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/fan2.png)

note

For more information, please check [here](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html?highlight=fan#fan-profile-control).

### Usage Instruction

**Create a script to set fan speed:**

```
cat test_fanSpeedSet
```

Paste the following content:

```
#!/bin/bash  
sudo systemctl stop nvfancontrol  
sleep 2  
echo "000000" | sudo -S chmod 777 /sys/devices/platform/pwm-fan/hwmon/hwmon1/pwm1  
echo $1 > /sys/devices/platform/pwm-fan/hwmon/hwmon1/pwm1
```

Additionally, we can manually set the fan speed using the `jtop` tool.

## CAN

CAN (Controller Area Network) is a robust vehicle bus standard that enables microcontrollers and devices to communicate with each other without a host computer.

The J501 Mini provides two CAN interfaces integrated into the JST 4-pin(GH1.25). Additionally, both CAN interfaces **support CAN-FD**, with CAN0 and CAN1 shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/can-real.png)

The pinout definitions for **CAN0** and **CAN1** are similar, and the interface diagram is shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/can-jst.png)

**CAN0** corresponds to **J6**, and the pin definitions are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/can0-ds.png)

**CAN1** corresponds to **J7**, and the pin definitions are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/can1-ds.png)

### CAN Communication

This section connects CAN0 and CAN1 on the Jetson to demonstrate how to send and receive data between CAN0 and CAN1 in `Classic CAN mode` and `CAN-FD mode`.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/CAN-connect.png)

The termination resistors for CAN0 and CAN1 can be controlled via two pins: PAA.04, located at gpiochip1 line4, and PAA.07, located at gpiochip1 line7.

Termination resistor control follows these rules:

```
When `PAA.04 = 1`, the 120 Ω termination resistor of CAN0 is **disconnected**;    
when `PAA.04 = 0`, the 120 Ω termination resistor of CAN0 is **connected**.  
  
When `PAA.07 = 1`, the 120 Ω termination resistor of CAN1 is **disconnected**;    
when `PAA.07 = 0`, the 120 Ω termination resistor of CAN1 is **connected**.
```

Enter the following command to view the pins on gpiochip 1:

```
gpioinfo gpiochip1
```

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/gpiochip1-can.png)

Refer to the following commands to set `PAA.04` and `PAA.07` to 0:

```
sudo gpioset --mode=wait gpiochip1 4=0  
sudo gpioset --mode=wait gpiochip1 7=0
```

Refer to the following commands to set `PAA.04` and `PAA.07` to 1:

```
sudo gpioset --mode=wait gpiochip1 4=1  
sudo gpioset --mode=wait gpiochip1 7=1
```

#### Classic CAN mode

Create `test_can.sh` to test data transmission and reception between **CAN0** and **CAN1** in standard mode:

```
touch test_can.sh  
chmod +x test_can.sh  
sudo ./tets_can.sh
```

The script code for `test_can.sh` is as follows:

 test\_can.sh 

```
#!/bin/bash  
  
echo "000000" | sudo -S ip link set can0 down  
echo "000000" | sudo -S ip link set can1 down  
  
# set buffer size  
echo "000000" | sudo -S sysctl -w net.core.rmem_max=524288  
echo "000000" | sudo -S sysctl -w net.core.wmem_max=524288  
echo "000000" | sudo -S sysctl -w net.core.rmem_default=524288  
echo "000000" | sudo -S sysctl -w net.core.wmem_default=524288  
  
 #set to 2M bps  
echo "000000" | sudo -S ip link set can0 type can bitrate 2000000  
echo "000000" | sudo -S ip link set can0 up  
  
echo "000000" | sudo -S ip link set can1 type can bitrate 2000000  
echo "000000" | sudo -S ip link set can1 up  
  
sleep 2  
  
#Enable 5s to test  
sudo pkill -f gpioset  
gpioset --mode=time --sec=200000 gpiochip1 7=0 &  
GPIO1_PID=$!  
gpioset --mode=time --sec=200000 gpiochip1 4=0 &  
GPIO2_PID=$!  
  
cangen can1 &  
candump can0
```

Data transmission and reception between **CAN0** and **CAN1** will be completed:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/can_normal.jpg)

#### CAN-FD mode

In the [datasheet](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_robotics_J401_datasheet.pdf), you can find the wiring diagram for the **CAN0/CAN1** interface as shown below:

Create `test_canfd.sh` to test data transmission and reception between CAN0 and CAN1 in CAN-FD mode:

```
touch test_canfd.sh  
chmod +x test_can.sh  
sudo ./tets_can.sh
```

The script code for `test_canfdfd.sh` is as follows:

 test\_canfd.sh 

```
#!/bin/bash  
  
# configure CAN FD mode  
#CAN bus rate set to 500 kbps, data rate set to 5 Mbps.  
echo "000000" | sudo -S ip link set can0 down  
echo "000000" | sudo -S sudo ip link set can0 type can bitrate 500000 dbitrate 5000000 berr-reporting on fd on restart-ms 100  
echo "000000" | sudo -S ip link set can0 up  
  
echo "000000" | sudo -S ip link set can1 down  
echo "000000" | sudo -S sudo ip link set can1 type can bitrate 500000 dbitrate 5000000 berr-reporting on fd on restart-ms 100  
echo "000000" | sudo -S ip link set can1 up  
  
  
# config buffer size  
echo "000000" | sudo -S sysctl -w net.core.rmem_max=524288  
echo "000000" | sudo -S sysctl -w net.core.wmem_max=524288  
echo "000000" | sudo -S sysctl -w net.core.rmem_default=524288  
echo "000000" | sudo -S sysctl -w net.core.wmem_default=524288  
  
  
# check CAN FD status  
echo "CAN0 status:"  
ip -details link show can0  
  
echo "CAN1 status:"  
ip -details link show can1  
  
#Enable 5s to test  
sudo pkill -f gpioset  
gpioset --mode=time --sec=200000 gpiochip1 7=0 &  
GPIO1_PID=$!  
gpioset --mode=time --sec=200000 gpiochip1 4=0 &  
GPIO2_PID=$!  
  
candump can0 &  
cangen can1 -f
```

Data transmission and reception between CAN0 and CAN1 will be completed:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/can-fd.jpg)

## GPI && GPO

### GPI

The Robotics J501 Mini provides a standard 6-pin JST header for GPI.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/GPI-real.png)

The **GPI** datasheet schematic is shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/GPI-jst.png)

The pin definitions for **J12** are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/GPI-ds.png)

Enable **GPI 1** to **GPI 4** for reading input status:

```
sudo gpioset --mode=wait 0 131=0
```

To read the input of **GPI 1** to **GPI 4**, refer to the following commands:

```
sudo gpioget 0 96  #read the input of GPI 1  
sudo gpioget 0 104 #read the input of GPI 2  
sudo gpioget 0 86  #read the input of GPI 3  
sudo gpioget 0 83  #read the input of GPI 4
```

When a high level is read, it will return 1; when a low level is read, it will return 0.

### GPO

The Robotics J501 Mini provides a standard 6-pin JST header for GPO.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/GPO-real.png)

The **GPO** datasheet schematic is shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/GPO-jst.png)

The pin definitions for **J14** are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/GPO-ds.png)

Enable **GPO 1** to **GPO 4** for output status:

```
sudo gpioset --mode=wait 0 79=1
```

To set the output of **GPO 1** to **GPO 4**, refer to the following commands:

```
sudo gpioset --mode=wait 0 110=1  #set output of GPO 1 to high voltag  
sudo gpioset --mode=wait 0 112=1  #set output of GPO 2 to high voltag  
sudo gpioset --mode=wait 0 111=1  #set output of GPO 3 to high voltag  
sudo gpioset --mode=wait 0 113=1  #set output of GPO 4 to high voltag  
  
  
sudo gpioset --mode=wait 0 110=1  #set output of GPO 1 to low voltag  
sudo gpioset --mode=wait 0 112=1  #set output of GPO 2 to low voltag  
sudo gpioset --mode=wait 0 111=1  #set output of GPO 3 to low voltag  
sudo gpioset --mode=wait 0 113=1  #set output of GPO 4 to low voltag
```

## UART

The Robotics J501 Mini provides a standard 6-pin JST header for UART serial communication.
UART and GPO use the same JST interface. This interface defaults to GPO functionality. **If you need to switch to UART functionality, you must point to a new device tree and restart the device for the change to take effect.**

For **UART** communication, please follow the following wiring. Here, we use the USB to TTL tool as an example.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/uart-real.png)

The **UART** datasheet schematic is shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/GPO-jst.png)

The pin definitions for **J14** are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/GPO-ds.png)

warning

UART and GPO share the same physical interface. By default, this interface functions as GPO. If you need to switch to UART, please refer to the content of this section.

For different modules, you need to download the corresponding device tree file.

`.dtb` download link for AGX Orin 32G:  
<https://files.seeedstudio.com/wiki/recomputer-j501-mini/tegra234-j501x-0000%2Bp3701-0004-recomputer-mini.dtb>

`.dtb` download link for AGX Orin 64G:  
<https://files.seeedstudio.com/wiki/recomputer-j501-mini/tegra234-j501x-0000%2Bp3701-0005-recomputer-mini.dtb>

Copy the device tree to the specified path:

```
# AGX Orin 32G  
sudo cp tegra234-j501x-0000%2Bp3701-0004-recomputer-mini.dtb /boot/  
  
# AGX Orin 64G  
sudo cp tegra234-j501x-0000%2Bp3701-0005-recomputer-mini.dtb /boot/
```

Back up and modify `/boot/extlinux/extlinux.conf`, adding a line to point to the new `.dtb` file:

```
sudo cp /boot/extlinux/extlinux.conf /boot/extlinux/extlinux.conf.bak  
sudo vim /boot/extlinux/extlinux.conf
```

Based on the device tree file name you are using, add a line `FDT=/your_path` in `extlinux.conf`. Taking AGX Orin 32G as an example:

```
LABEL primary  
      MENU LABEL primary kernel  
      LINUX /boot/Image  
      INITRD /boot/initrd  
      FDT=/boot/tegra234-j501x-0000+p3701-0004-recomputer-mini.dtb
```

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/uart-edit.png)

The 6-pin JST header **UART** is mapped to `/dev/ttyTHS1` on the Jetson. You can use `minicom` to view serial port data transmission and reception:

```
sudo apt install minicom  
sudo minicom -D /dev/ttyTHS1
```

## RS485

The RS485 interface provides a robust and noise-resistant differential communication channel commonly used in industrial environments. It supports long-distance, multi-drop serial communication and is ideal for connecting sensors, motor controllers, PLCs, and other industrial devices.

### Hardware Connection

Robotics J501-Mini provides a JST 4-pin(GH 1.25) headers for RS485.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/485-real.png)

The **RS485** datasheet schematic is shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/485-jst.png)

The pin definitions for **J8** are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/485-ds.png)

### Usage Instruction

Refer to the following commands to enable the **RS485** interface:

```
sudo gpioset --mode=wait 1 9=0  # Enable 120R resistance  
  
sudo gpioset --mode=wait 0 126=0 # Enable RS485
```

The **RS485** interface is mapped to `/dev/ttyTHS4` on the Jetson. You can use `cutecom` to test serial data transmission and reception with a PC:

```
sudo apt install cutecom  
sudo cutecom
```

Select `/dev/ttyTHS4`, set both Jetson and PC to a baud rate of 9600, and connect the Jetson and PC via an RS485 to USB module.
The serial data transmission and reception effect is shown in the figure below:

![Jetson side](https://files.seeedstudio.com/wiki/recomputer-j501-mini/485_jetson.png)![PC side](https://files.seeedstudio.com/wiki/recomputer-j501-mini/485_PC.png)

## I2S

The I2S interface provides a digital audio communication bus designed for transmitting stereo audio data between devices. The Robotics J501-Mini supports standard I2S signaling, allowing high-quality, low-latency audio input and output for applications such as voice interaction, sound localization, and real-time audio processing.

### Hardware Connection

Robotics J501-Mini provides a 1x JST 5-Pin Connector(GH 1.25) for **I2S**.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/I2S-real.png)

The **I2S** datasheet schematic is shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/i2s-jst.png)

The pin definitions for **J9** are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/i2s-ds.png)

### Usage Instruction

To enable **I2S**, you need to configure it in `jetson-io.py`. Run the following in the terminal:

```
sudo python /opt/nvidia/jetson-io/jetson-io.py
```

Then, refer to the four steps below to enable the I2S interface:

* step1: Select the **Jetson 40-pin header** option
* step2: Select **Configure header pins manually**
* step3: Select `i2s2`; after selection, it will be marked with `[*]`
* step4: Save the settings and reboot the Jetson

Step 1

![Step 1](https://files.seeedstudio.com/wiki/recomputer-j501-mini/1-i2s.png)

Step 3

![Step 3](https://files.seeedstudio.com/wiki/recomputer-j501-mini/3-i2s.png)

Step 2

![Step 2](https://files.seeedstudio.com/wiki/recomputer-j501-mini/2-i2s.png)

Step 4

![Step 4](https://files.seeedstudio.com/wiki/recomputer-j501-mini/4-i2s.png)

After enabling **I2S**, this section demonstrates how to use I2S to drive a dual-channel speaker. First, enter the following in the terminal:

```
amixer -c APE cset name="I2S2 Mux" "ADMAIF1" # Speaker
```

If you are using a microphone:

```
amixer -c APE cset name="ADMAIF2 Mux" "I2S2" # Microphone
```

Refer to the command below to drive the speaker, where `-c` should be changed to the number of speaker channels you are using:

```
speaker-test -t sine -f 440 -c 2
```

You can see the output in the terminal when the speaker is driven normally, as shown in the figure below.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/i2s-speaker.png)

## RTC

The Robotics J501-Mini provides a standard 2-pin header for **RTC** (3V).

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/rtc0.png)

The **RTC** datasheet schematic is shown below:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/rtc1.png)

The pin definitions for **J15** are as follows:

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/rtc2.png)

After plugging in the external battery, you can check the operating status of `rtc0` (main RTC, corresponding to the onboard battery) in the terminal:

```
cat /sys/class/rtc/rtc0/power/runtime_status
```

## Extension Port - GMSL

The Robotics j501-Mini carrier board features a Camera Expansion Header for GMSL extension board. It can simultaneously connect and operate four GMSL cameras at the same time.

### Hardware Connection

Here are the Robotics j501-Mini carrier board GMSL camera expansion board connection slot(need to prepare an extension board in advance):

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/gmsl-real1.png)![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/gmsl-real2.png)

The following are the GMSL camera models that we have already supported:

* [SG3S-ISX031C-GMSL2F](https://www.seeedstudio.com/SG3S-ISX031C-GMSL2F-p-6245.html)
* SG2-AR0233C-5200-G2A
* SG2-IMX390C-5200-G2A
* SG8S-AR0820C-5300-G2A

### Usage Instruction

note

Before enabling the GMSL functionality, please ensure that you have installed a JetPack version with the GMSL expansion board driver.

### Configure the Jetson IO file

```
sudo /opt/nvidia/jetson-io/jetson-io.py
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/robotics_j401/io_p1.png)

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/robotics_j401/io_p2.png)

note

There are three overlay files in total, namely Seeed GMSL 1X4 3G, Seeed GMSL 1X4 6G, Seeed GMSL 1X4, and Orbbec Gemini 335Lg. These correspond to the 3G camera of SG3S, the 6G camera of SG2 and SG8S, and the camera of Orbbec respectively. As shown in Figure 3, please configure the io file according to the model of your camera.

**step 2.** Install the video interface configuration tools.

```
sudo apt update  
sudo apt install v4l-utils
```

### Use the cameras of SGxxx Series

**step 1.** Set the channel format for the serializer and deserializer.The interface number in the figure corresponds to the serializer/deserializer number.

![](https://files.seeedstudio.com/wiki/recomputer-j501-mini/gmsl-Interface.png)

```
  media-ctl -d /dev/media0 --set-v4l2 '"ser_0_ch_0":1[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"des_0_ch_0":0[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"ser_1_ch_1":1[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"des_0_ch_1":0[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"ser_2_ch_2":1[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"des_0_ch_2":0[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"ser_3_ch_3":1[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"des_0_ch_3":0[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"ser_4_ch_0":1[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"des_1_ch_0":0[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"ser_5_ch_1":1[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"des_1_ch_1":0[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"ser_6_ch_2":1[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"des_1_ch_2":0[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"ser_7_ch_3":1[fmt:YUYV8_1X16/1920x1536]'  
  media-ctl -d /dev/media0 --set-v4l2 '"des_1_ch_3":0[fmt:YUYV8_1X16/1920x1536]'
```

note

`ser_0_ch_0` is the first channel of the decoder, `des_ch_0` is the serializer on the first camera, and the same applies to the others.If the connected camera has a different resolution, then the configuration here will be based on the actual format of the camera.
We need to set the channel format for the serializer and deserializer every time the device restarts.

**step 2.** Set the resolution of the camera.

info

Here we demonstrate how to configure cameras of different models and resolutions.

```
v4l2-ctl -V --set-fmt-video=width=1920,height=1080 -c sensor_mode=1  -d /dev/video0  
v4l2-ctl -V --set-fmt-video=width=1920,height=1080 -c sensor_mode=1  -d /dev/video1  
v4l2-ctl -V --set-fmt-video=width=1920,height=1536 -c sensor_mode=0  -d /dev/video2  
v4l2-ctl -V --set-fmt-video=width=3840,height=2160 -c sensor_mode=2  -d /dev/video3
```

note

`--set-fmt-video` follows the resolution which is selected based on the camera being connected. The sensor\_mode is also chosen accordingly. Currently, there are three sensor\_mode options, each corresponding to a different resolution.

* sensor\_mode=0 -------> YUYV8\_1X16/1920x1536
* sensor\_mode=1 -------> YUYV8\_1X16/1920x1080
* sensor\_mode=2 -------> YUYV8\_1X16/3840x2160

**step 3.** Start the camera.

```
gst-launch-1.0 v4l2src device=/dev/video0 ! \  
'video/x-raw,width=1920,height=1080,framerate=30/1,format=UYVY' ! \  
videoconvert ! autovideosink -ev  
  
gst-launch-1.0 v4l2src device=/dev/video1 ! \  
'video/x-raw,width=1920,height=1080,framerate=30/1,format=UYVY' ! \  
videoconvert ! autovideosink -ev  
  
gst-launch-1.0 v4l2src device=/dev/video2 ! \  
'video/x-raw,width=1920,height=1536,framerate=30/1,format=UYVY' ! \  
videoconvert ! autovideosink -ev  
  
gst-launch-1.0 v4l2src device=/dev/video3 ! \  
'video/x-raw,width=3840,height=2160,framerate=30/1,format=UYVY' ! \  
videoconvert ! autovideosink -ev
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/robotics_j401/camera1.png)

## Display

The Robotics J501 Mini is equipped with an HDMI for high-resolution display output.