# Getting Started with reComputer Super

The reComputer Super Series supercharges the reComputer Classic, delivering up to a 1.7x boost of 157 TOPS in AI performance. It features models with Jetson Orin Nano (11410311, 11410312) and Jetson Orin NX (11410313, 11410314).
Designed for both development and production, it comes with a rich array of interfaces, including M.2 Key E/M, dual RJ45 Ethernet, Mini-PCIe, 4xUSB 3.2, HDMI 2.1, 4xCSI, and CAN. With pre-installed Jetpack 6.2 and Linux OS BSP, it enables immediate market entry.
It also supports a wide range of LLM & Physical AI frameworks, such as NVIDIA, Hugging Face, ONNX, PyTorch, and ROS2/1 at the edge seamlessly, even merging these multimodal capacity with robotics application to enrich Physical AI development.

## Key Features

### 🚀 ​**Performance Boost**

* ​**1.7x AI performance boost** over reComputer Classic, delivering ​**157 TOPS**
* Powered by ​**Jetson Orin Nano** (Models: 11410311, 11410312) and ​**Jetson Orin NX** (Models: 11410313, 11410314)

### 🔌 ​**Rich Connectivity & Interfaces**

* ​**M.2 Key E/M** + ​**Mini-PCIe** for expandability
* ​**Dual RJ45 Ethernet** ports for high-speed networking
* ​**4x USB 3.2**, ​**HDMI 2.1**, ​**4x CSI** (Camera Serial Interface)
* ​**CAN bus** support for industrial/robotics applications

### 🛠️ ​**Ready for Development & Production**

* Pre-installed ​**Jetpack 6.2** and ​**Linux OS BSP** for out-of-the-box deployment
* Seamless edge AI integration with frameworks:
  + ​**NVIDIA**, ​**Hugging Face**, ​**ONNX**, ​**PyTorch**
  + ​**ROS2/1** for robotics applications
* Supports ​**multimodal AI** and ​**Physical AI** development

### 🤖 ​**Edge AI & Robotics Optimized**

* Merges ​**LLM (Large Language Model)** capabilities with ​**Physical AI** at the edge
* Ideal for robotics, industrial automation, and real-time AI inference
* Accelerates ​**market entry** with pre-configured software stack

### ⚠️ Power & Accessory Guidelines

#### 1. ​**Power Adapter**

* ​**Jetson Orin Nano**: 12V 5A (5525 barrel jack)
* ​**Jetson Orin NX**: 19V 4.74A (5525 barrel jack)
* Always use ​**official adapters** and meet power requirements.

#### 2. ​**AC Power Cord**

* Use ​**region-specific** cloverleaf cords.

#### 3. ​**Accessories**

* Only ​**officially recommended** accessories (e.g., cameras, wireless modules) for optimal performance and compatibility.

## Specifications

[TABLE COMPRESSED]
Columns: Jetson Orin Super System on Module | Specifications reComputer Super J3010 reComputer Super J3011 reComputer Super J4011 reComputer Super J4012 | Module NVIDIA Jetson Orin™ Nano 4GB NVIDIA Jetson Orin™ Nano 8GB NVIDIA Jetson Orin™ NX 8GB NVIDIA Jetson Orin™ NX 16GB | AI Performance 34 TOPS 67 TOPS 117 TOPS 157 TOPS | GPU 512-core NVIDIA Ampere architecture GPU with 16 Tensor Cores 1024-core NVIDIA Ampere architecture GPU with 32 Tensor Cores | CPU 6-core Arm® Cortex®-A78AE v8.2 64-bit CPU 1.5MB L2 + 4MB L3 6-core Arm® Cortex®-A78AE v8.2 64-bit CPU 1.5MB L2 + 4MB L3 8-core Arm® Cortex®-A78AE v8.2 64-bit CPU 2MB L2 + 4MB L3 | CPU Max Frequency 1.7 GHz (MAXN\_SUPER) 2 GHz | Memory 4GB 64-bit LPDDR5 34 GB/s 8GB 128-bit LPDDR5 68 GB/s 8GB 128-bit LPDDR5 102.4GB/s 16GB 128-bit LPDDR5 102.4GB/s | DL Accelerator / 1x NVDLA v2 2x NVDLA v2 | Video Encoder 1080p30 supported by 1-2 CPU cores 1x 4K60 (H.265) | 3x 4K30 (H.265) 6x 1080p60 (H.265) | 12x 1080p30 (H.265) ...

## Flash JetPack OS

### Supported Module

* [NVIDIA® Jetson Orin™ Nano Module 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5553.html)
* [NVIDIA® Jetson Orin™ Nano Module 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5551.html?___store=retailer)
* [NVIDIA® Jetson Orin™ NX Module 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5522.html)
* [NVIDIA® Jetson Orin™ NX Module 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5523.html)

### Prerequisites

* Ubuntu host PC
* reComputer Super
* USB Type-C data transmission cable

We recommend that you use physical ubuntu host devices instead of virtual machines.
Please refer to the table below to prepare the host machine.

[TABLE COMPRESSED]
Columns: JetPack Version Ubuntu Version (Host Computer) | 18.04 20.04 22.04 | JetPack 6.x ✅ ✅

### Prepare the Jetpack Image

Here, we need to download the system image to our Ubuntu PC corresponding to the Jetson module we are using:

[TABLE COMPRESSED]
Columns: Jetpack Version Jetson Module GMSL Download Link1 SHA256 | 6.2 Orin Nano 4GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EQiC_is_O2tEkvFzu-3SrWYBFdcQr0zZRUf81lkjnXpnkQ?e=f3ISaO) 8FF204A65C006717ED45241186C14B4  FAA8ACE5BEBCDCE755F94C3CBF1311C38 | Orin Nano 8GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EbEYa6n_P6pCh1TQbVBSpcQBZlFVm_-il3sqXEBDGpdPJA?e=S1dgfv) 7EC06C0D17E33AE43D3C69EED791F64 CB9CFDC497E01D525E18EBAC1547A0236 | Orin NX 8GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EevZ9hO7BfhDuJvDPYIdHGkBGhrKcWgCyAuTQu1gpHsz4g?e=xbXfbL) 06B175484220DA7A63CC7CDAAE339F7E FF8997180AF1C4B836D1098CBD8A169D | Orin NX 16GB ✅ [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EeIg8k2osZFAuPzOlcO-FtIBdhbgULGQrsQOg4uUrXoK4w?e=uo29A8) CF37D028D6466DCC13201367E6358A6 9B7B5305CAE2A2B785E3ECFD3D8C66304

The Jetpack6 image file is approximately **14.1GB** in size and should take around 60 minutes to download. Please kindly wait for the download to complete.

To verify the integrity of the downloaded firmware, you can compare the SHA256 hash value.

On an Ubuntu host machine, open the terminal and run the command `sha256sum <File>` to obtain the SHA256 hash value of the downloaded file. If the resulting hash matches the SHA256 hash provided in the wiki, it confirms that the firmware you downloaded is complete and intact.

### Enter Force Recovery Mode

Before we can move on to the installation steps, we need to make sure that the board is in force recovery mode.

 Step-by-Step 

**Step 1.** Switch the switch to the RESET mode.

**Step 2.** Power up the reComputer Super by connecting the power cable.

**Step 3.** Connect the Super to the Ubuntu host PC with a USB Type-C data transmission cable.

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
# For example: sudo tar xpf mfi_recomputer-super-orin-nx-16g-j401-6.2-36.4.3-2025-05-22.tar.gz
```**Step 2:** Execute the following command to flash jetpack system to the NVMe SSD:
```
cd mfi_xxxx  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```You will see the following output if the flashing process is successful

The flash command may run for 2-10 minutes.

**Step 3:** Connect the monitor using an HDMI cable and complete the initialization configuration of the reComputer Super system:

Please complete the **System Configuration** according to your needs.
