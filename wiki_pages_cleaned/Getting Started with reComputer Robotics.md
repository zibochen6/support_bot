# Getting Started with reComputer Robotics

The reComputer Robotics J401 is a compact, high-performance edge AI carrier board designed for advanced robotics. Compatible with NVIDIA Jetson Orin Nano/Orin NX modules in Super/MAXN mode, it delivers up to 157 TOPS of AI performance. Equipped with extensive connectivity options—including dual Gigabit Ethernet ports, M.2 slots for 5G and Wi-Fi/BT modules, 6 USB 3.2 ports, CAN, GMSL2 (via optional expansion), I2C, and UART—it serves as a powerful robotic brain capable of processing complex data from various sensors. Pre-installed with JetPack 6 and Linux BSP, it ensures seamless deployment.​

## Features

* **Robust Hardware Design**: A compact, high-performance edge AI computer with NVIDIA® Jetson™ Orin™ NX 16GB module in Super/MAXN mode, providing up to 157 TOPS of AI performance.
* **Multiple Interfaces for robotics**: Including dual RJ45, M.2 slots for 5G/Wi-Fi/BT modules, 6x USB 3.2, 2x CAN, GMSL2(additional purchase), I2C, and UART, functioning as a powerful robotic brain.
* **Software Setup**: Pre-installed with JetPack 6.2 and Linux BSP for seamless deployment.
* **Application and Benefit**: Ideal for rapid development of autonomous robots, accelerating time-to-market with ready-to-use interfaces and optimized AI frameworks.
* **Wide Operating Range**: Operates reliably across a temperature range of -20°C to 60°C at 25W mode and -20°C to 50°C at 40W mode

## Specification

### Carrier Board Specifications

[TABLE COMPRESSED]
Columns: Category Item Details | Storage M.2 KEY M PCIe 1x M.2 KEY M PCIe (M.2 NVMe 2280 SSD 128G included) | Networking M.2 KEY E 1x M.2 Key E for WiFi/Bluetooth module | M.2 KEY B 1x M.2 Key B for 5G module | Ethernet 2x RJ45 Gigabit Ethernet | I/O USB 6x USB 3.2 Type-A (5Gbps); 1x USB 3.0 Type-C (Host/DP 1.4); 1x USB 2.0 Type-C (Device Mode/Debug) | Camera 1x 4 in 1 GMSL2 (mini fakra) (optional board) | CAN 2x CAN0 (XT30(2+2)); 3x CAN1 (4-Pin GH 1.25 Header) | Display 1x DP1.4 (Type C Host) | UART 1x UART 4-Pin GH 1.25 Header | I2C 2x I2C 4-Pin GH 1.25 Header | Fan 1x 4-Pin Fan Connector (5V PWM); 1x 4-Pin Fan Connector (12V PWM) ...

## Hardware Overview

## Flash JetPack OS

### Supported Module

* [NVIDIA® Jetson Orin™ Nano Module 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5553.html)
* [NVIDIA® Jetson Orin™ Nano Module 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5551.html?___store=retailer)
* [NVIDIA® Jetson Orin™ NX Module 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5522.html)
* [NVIDIA® Jetson Orin™ NX Module 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5523.html)

### Prerequisites

* Ubuntu host PC
* reComputer Robotics
* NVIDIA® Jetson Orin™ Nano/NX Module
* USB Type-C data transmission cable

We recommend that you use physical ubuntu host devices instead of virtual machines.
Please refer to the table below to prepare the host machine.

[TABLE COMPRESSED]
Columns: JetPack Version Ubuntu Version (Host Computer) | 18.04 20.04 22.04 | JetPack 6.x ✅ ✅

### Prepare the Jetpack Image

Here, we need to download the system image to our Ubuntu PC corresponding to the Jetson module we are using:

[TABLE COMPRESSED]
Columns: Jetpack Version Jetson Module GMSL Download Link1 SHA256 | 6.2 Orin Nano 4GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EWqAOoqYYxNAky0Dbo847q0BDWsiSBUmyrxAMzNV9SQyNw?e=ZuOFnx) c63d1219531245abecc7bbdcafc73d3 4f75547454c7af85de40f08396a87e5ee | Orin Nano 8GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/ERy0O0zUQGlKh8cDHZIoSPEBcHFJOGY6rE0gVBGCE6tBvA?e=eDw71c) 5d1f3cd28eb44ca60132c87ccce5aca f806ee945b486df9061a34de73fbb582b | Orin NX 8GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EewEJTne6ltJlP0IDzahaCYB9rJWUIvKXe5b0p76rlYr_A?e=tsuNbP) e7f0c8e6b578d411f81122879f92c76 66adfada5ed493a4cc458dc169ca8c1b7 | Orin NX 16GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EdXbblXVvqZDv3DqdJOR8u8BXV6rW6BVwoss0EMC-sLcfQ?e=WiW2F9) b08cbdad8ab6e50222146d3175a9d2 627d499bf1d67cfaf69cc737b5bfa9e33a

The Jetpack6 image file is approximately **14.2GB** in size and should take around 60 minutes to download. Please kindly wait for the download to complete.

To verify the integrity of the downloaded firmware, you can compare the SHA256 hash value.

On an Ubuntu host machine, open the terminal and run the command `sha256sum <File>` to obtain the SHA256 hash value of the downloaded file. If the resulting hash matches the SHA256 hash provided in the wiki, it confirms that the firmware you downloaded is complete and intact.

### Enter Force Recovery Mode

Before we can move on to the installation steps, we need to make sure that the board is in force recovery mode.

 Step-by-Step 

**Step 1.** Switch the switch to the RESET mode.

**Step 2.** Power up the carrier board by connecting the power cable.

**Step 3.** Connect the board to the Ubuntu host PC with a USB Type-C data transmission cable.

**Step 4.** On the Linux host PC, open a Terminal window and enter the command `lsusb`. If the returned content has one of the following outputs according to the Jetson SoM you use, then the board is in force recovery mode.

* For Orin NX 16GB: **0955:7323 NVidia Corp**
* For Orin NX 8GB: **0955:7423 NVidia Corp**
* For Orin Nano 8GB: **0955:7523 NVidia Corp**
* For Orin Nano 4GB: **0955:7623 NVidia Corp**

The below image is for Orin Nano 8GB

### Flash to Jetson

**Step 1:** Extract the downloaded image file:
```
cd <path-to-image>  
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-robo-orin-nano-8g-j401-6.2-36.4.3-2025-05-23.tar.gz
```**Step 2:** Execute the following command to flash jetpack system to the NVMe SSD:
```
cd mfi_xxxx  
# For example: cd mfi_recomputer-orin-robotics-j401   
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```You will see the following output if the flashing process is successful

The flash command may run for 2-10 minutes.

**Step 3:** Connect the Robotics J401 to a display use the PD to HDMI adapter to connect to a display that supports HDMI input, or directly connect to a display that supports PD input using the PD cable, and finish the initial configuration setup:

Please complete the **System Configuration** according to your needs.

## Hardware Interfaces Usage

If you want to learn more about the detailed specifications and usage of the hardware interface, please refer to [this wiki](https://wiki.seeedstudio.com/recomputer_jetson_robotics_j401_getting_started/#interfaces-usage).
