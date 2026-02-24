# Flash JetPack to J401-Mini Carrier Board

reComputer Mini is a tiny AI computer powered by NVIDIA Jetson Orin Nano/Orin NX module,delivering up to 100 TOPS AI performance. It‘s equipped with PCIe port at the bottom to provide rich expansion capabilities, which also can be customized flexibly. The whole system is designed for embedding into autonomous machines such as drones, patrol robots, delivering robots, etc. It can directly occupy 54V DC input, able to be widely used in battery powered systems.

## Features

* **Brilliant AI Performance for Production:** Achieves up to **100 TOPS** AI performance with low power and latency, built by NVIDIA Orin SoC combining the NVIDIA Ampere™ GPU architecture with 64-bit operating capability, integrated advanced multi-function video and image processing, and NVIDIA Deep Learning Accelerators.
* **Hand-Size Edge AI Device:** Compact size at **63mmx95mmx42mm**, featuring an NVIDIA Jetson Orin NX 16GB module, Mini J401 carrier board, fan and enclosure. Support desktop and wall mounting.
* **Expandable with Rich I/Os:** Includes up to 7x USB, 1x DP 2.1, 2x CSI, 1x RJ45 for GbE, M.2 Key E, M.2 Key M, dual channel CAN, and GPIO with extension board.
* **Accelerate Solutions to Market:** Pre-installed **JetPack 6.0** on 128GB NVMe SSD, Linux OS BSP, supporting Jetson software and leading AI frameworks.
* **Scale to deploy:** support OTA, remote management services powered by Allxon and Balena.
* **Flexible Customization:** inlcudes changing accessories modules, logo, and hardware interfaces modification based on reComputer Mini J4012 original design.

## Specifications

[TABLE COMPRESSED]
Columns: Jetson Orin System on Module | Specifications reComputer Mini J3010 reComputer Mini J3011 reComputer Mini J4011 reComputer Mini J4012 | Module Jetson Orin Nano 4GB Jetson Orin Nano 8GB Jetson Orin NX 8GB Jetson Orin NX 16GB | AI Performance 20 TOPS 40 TOPS 70 TOPS 100 TOPS | GPU 512-core NVIDIA Ampere architecture GPU with 16 Tensor Cores 1024-core NVIDIA Ampere architecture GPU with 32 Tensor Cores | CPU 6-core Arm® Cortex®-A78AE v8.2 64-bit CPU 1.5MB L2 + 4MB L3 6-core Arm® Cortex®-A78AE v8.2 64-bit CPU 1.5MB L2 + 4MB L3 8-core Arm® Cortex®-A78AE v8.2 64-bit CPU 2MB L2 + 4MB L3 | CPU Max Frequency 1.5 GHz 2 GHz | Memory 4GB 64-bit LPDDR5 34 GB/s 8GB 128-bit LPDDR5 68 GB/s 8GB 128-bit LPDDR5 102.4GB/s 16GB 128-bit LPDDR5 102.4GB/s | DL Accelerator / 1x NVDLA v2 2x NVDLA v2 | Video Encoder 1080p30 supported by 1-2 CPU cores 1x 4K60 (H.265) | 3x 4K30 (H.265) 6x 1080p60 (H.265) | 12x 1080p30 (H.265) ...

## Hardware Overview

## Flash JetPack OS

Here, we will show you how to flash [Jetpack 6.0](https://developer.nvidia.com/embedded/jetson-linux-archive) to an NVMe SSD connected to the reComputer Mini.

### Supported Nvidia Jetson Module

* [NVIDIA® Jetson Orin™ Nano Module 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5554.html)
* [NVIDIA® Jetson Orin™ Nano Module 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5552.html)
* [NVIDIA® Jetson Orin™ NX Module 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5523.html)
* [NVIDIA® Jetson Orin™ NX Module 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5524.html)

### Prerequisites

* Ubuntu Host Computer
* reComputer J401-Mini Carrier Board with Jetson Orin Module
* USB Micro-B data transmission cable

We recommend that you use physical ubuntu host devices instead of virtual machines.
Please refer to the table below to prepare the host machine.

[TABLE COMPRESSED]
Columns: JetPack Version Ubuntu Version (Host Computer) | 18.04 20.04 22.04 | JetPack 5.x ✅ ✅ | JetPack 6.x ✅ ✅

### Prepare the Jetpack Image

Here, we need to download the system image to our Ubuntu PC corresponding to the Jetson module we are using:

[TABLE COMPRESSED]
Columns: Jetpack Version Jetson Module Download Link SHA256 | 5.1.3 Orin Nx 16GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EfA7P_6gLnJAnxptIAURoCgBDF-emSfyD9uGWYY2vuFhmg?e=DF6a8l) 099bf8e706468dc36600ffdb3444168 3cde7454646621017fc39db49c16a2c53 | Orin Nx 8GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/Eew7pWvWB3RLtT5vMkVTFHABADBzxS8id4xNtrQHGcO3eg?e=drxTwI) 6ce30b9e212310498eee2c0a363cb35 14b1c607ae6a1ab403d5029115bc3a71b | Orin Nano 8GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcEvOGxB9DpOuFubj-xJ1oYBixiZy4vd0t_chXQcezPy9A?e=RnX7NN) b8f7a0b6d5974add33c3102824c671b 61ca8e278b0c5e3c38a7c5a45e251251e | Orin Nano 4GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EYi8K66PG6xOjwiU-_x3Ey4BpZhEiLFS8c_JoEDzeTVaxg?e=TkAgJV) cc6efd6e4a42f099dde47e9ed71a34e 0981e77c50e3dc74f38338210c1f3bda0 | 6.0 Orin Nx 16GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcQFCfXEWVREuzwvvBX7vRsBlr9H6HQpTBzmDw0rigIt1Q?e=IzLuYu) 7B4ABE1D1A8711D5D4E9B676DBB1E76 CDA35C614608CE7ECE112BC4A50E71C7C | Orin Nx 8GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EUpeLu1P7RJOv7-nqR7QbmABfmWR45xVUt95bMplpp25mQ?e=oiWB6b) 3956B968F2BFB9FDF37D952E83DDB70 3980C813156919BC367CA5E23BBDEC89F | Orin Nano 8GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EWbSLkBX0XpIrFjkT0vndGsBysfm51HvFkBFsRnfRaWBxA?e=t7vRcH) BF6921DF313B467254154BDA835C379 AD86D817E03D0301543B62F7CA0C9222F | Orin Nano 4GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EUB7YoQeCrVHnDjsrfFaL8EBxkjRrclpDxFwDB3dJpM3xQ?e=oYHLp7) 8941C13204A8069CE70B109B6A13EA2 40CBB02F69B8D4028D465134B3744BC28 | 6.2 Orin Nano 8GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EVjuq6G9y_5OjIxMIHFiBj0BVckYdcRQBunaXMHFBLZ3tw?e=tY89se) A1C5F44B19B6C06E11AC38ABDA79AD6 CBFF2AAFBEEA7BF3A14B2FE08EA37267F | Orin Nano 4GB [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EcdaeIBdGRpCp0Dev5R3o1sB2Tr4HIwjgtp3d_XX7lE9Gg?e=bxteCW) 23855098982DD1E05C025D3F078BCA0 2F396C1FB68DC58E539D83569A894571D

The Jetpack6 image file is approximately **16.7GB** in size and should take around 60 minutes to download. Please kindly wait for the download to complete.

To verify the integrity of the downloaded firmware, you can compare the SHA256 hash value.

On an Ubuntu host machine, open the terminal and run the command `sha256sum <File>` to obtain the SHA256 hash value of the downloaded file. If the resulting hash matches the SHA256 hash provided in the wiki, it confirms that the firmware you downloaded is complete and intact.

### Enter Force Recovery Mode

Before we can move on to the installation steps, we need to make sure that the board is in force recovery mode.

 Step-by-Step 

* **Step 1.** Connect a USB Micro-B cable between USB2.0 DEVICE port and the ubuntu host PC.
* **Step 2.** Use a pin and insert into the RECOVERY hole to press recovery button and while holding this.
* **Step 3.** Connect the power supply.
* **Step 4.** Release the recovery button.

On the Linux host PC, open a Terminal window and enter the command `lsusb`. If the returned content has one of the following outputs according to the Jetson SoM you use, then the board is in force recovery mode.

* For Orin NX 16GB: 0955:7323 NVidia Corp
* For Orin NX 8GB: 0955:7423 NVidia Corp
* For Orin Nano 8GB: 0955:7523 NVidia Corp
* For Orin Nano 4GB: 0955:7623 NVidia Corp

The below image is for Orin Nx 16GB:

### Flash to Jetson Step by Step

**Step 1:** Extract the downloaded image file on ubuntu host PC:
```
cd <path-to-image>  
sudo tar xpf mfi_xxxx.tar.gz  
# For example: sudo tar xpf mfi_recomputer-orin-nano-8g-j401-6.0-36.3.0-2024-06-07.tar.gz
```**Step 2:** Execute the following command to flash jetpack system to the NVMe SSD:
```
cd mfi_xxxx  
# For example: cd mfi_recomputer-orin-j401  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```You will see the following output if the flashing process is successful

The flash command may run for 2-10 minutes.

**Step 3:** Connect the J501 to a display using the HDMI connector on the board and finish the initial configuration setup:

Please complete the **System Configuration** according to your needs.

**Step 4 (Optional):** Install Nvidia Jetpack SDK

Please open the terminal on the Jetson device and execute the following commands:
```
sudo apt update  
sudo apt install nvidia-jetpack
```## Hardware Interfaces Usage

If you want to learn more about the detailed specifications and usage of the hardware interface, please refer to [this wiki](https://wiki.seeedstudio.com/recomputer_jetson_mini_hardware_interfaces_usage/).
