# Flash JetPack OS to A603 Carrier Board

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/A603_Carrier_Board.png)

[**Get One Now 🖱️**](https://www.seeedstudio.com/A603-Carrier-Board-for-Jetson-Orin-NX-Nano-p-5635.html)

A603 Carrier Board is a powerful extension board that supports Jetson Orin™ NX/Nano modules. It features 1 GbE port, M.2 Key M for SSD, M.2 Key E for WiFi/BlueTooth, CSI, and HDMI for high-quality video capture and display. It also contains 4x USB ports, fan, RTC, flexible 9-20V power supply. By the compact design, it can be flexible and easy to integrate into a variety of edge computing applications. In this wiki, we will show you how to flash [Jetpack](https://developer.nvidia.com/embedded/jetpack) to an NVMe SSD and a USB Flash drive connected to the A603 Carrier Board.

## Supported Module

* [NVIDIA® Jetson Orin™ Nano Module 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5553.html)
* [NVIDIA® Jetson Orin™ Nano Module 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5551.html?___store=retailer)
* [NVIDIA® Jetson Orin™ NX Module 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5522.html)
* [NVIDIA® Jetson Orin™ NX Module 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5523.html)

## Prerequisites

* Ubuntu Host PC
* A603 Carrier Board with Jetson Orin module
* Micro-USB data transmission cable

## Enter Force Recovery Mode

note

Before we can move on to the installation steps, we need to make sure that the board is in force recovery mode.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/recovery.gif)

 step-by-step detailed tutorial 

**Step 1.** Connect a USB cable between the micro-USB connector on the board and the Linux host PC

![](https://files.seeedstudio.com/wiki/A603/2.jpg)

**Step 2.** Connect a jumper wire between pin3 and pin4 of the 14-pin header

![](https://files.seeedstudio.com/wiki/A603/3.jpg)

**Step 3.** Connect power adapter to the DC JACK on the board to power on the board

![](https://files.seeedstudio.com/wiki/A603/4.jpg)

**Step 4.** On the Linux host PC, open a Terminal window and enter the command `lsusb`. If the returned content has one of the following outputs according to the Jetson SoM you use, then the board is in force recovery mode.

* For Orin NX 16GB: **0955:7323 NVidia Corp**
* For Orin NX 8GB: **0955:7423 NVidia Corp**
* For Orin Nano 8GB: **0955:7523 NVidia Corp**
* For Orin Nano 4GB: **0955:7623 NVidia Corp**

The below image is for Orin NX 16GB.

![](https://files.seeedstudio.com/wiki/A607/4.png)

**Step 5.** Remove the jumper wire.

## Download the peripheral drivers

First of all, you need to install the peripheral drivers for this board. These are needed for some hardware peripherals to function on the board. Click the below links to download the drivers according to the Jetson module

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jetson Module JetPack Version L4T Version Download Link|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Jetson Orin NX 8GB/ 16GB 5.1 35.2.1 [Download](https://sourceforge.net/projects/nvidia-jetson/files/A603-Carrier-Board/Orin-NX/A603-Orin-NX-JP5.1.zip/download)| 5.1.1 35.3.1 [Download](https://sourceforge.net/projects/nvidia-jetson/files/A603-Carrier-Board/Orin-NX/A603-Orin-NX-JP5.1.1.zip/download)| Jetson Orin Nano 4GB/ 8GB 5.1.1 35.3.1 [Download](https://sourceforge.net/projects/nvidia-jetson/files/A603-Carrier-Board/Orin-Nano/A603-Orin-Nano-JP5.1.1.zip/download)| Jetson Orin NX 8GB/ 16GB, Jetson Orin Nano 4GB/ 8GB 5.1.2 35.4.1 [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EZC4-Ci8o0dNkc0wWWlphf0BEQHp2nV-TM2Qpn7WwmpB1g?e=heBSc2)| Jetson Orin NX 8GB/ 16GB, Jetson Orin Nano 4GB/ 8GB 5.1.4 35.6.0 [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EShnCiOVY3ZPqptpnJZ0tlABemb3chgmuUZyuvsqJpHpcA?e=hXxCRr)| Jetson Orin NX 8GB/ 16GB, Jetson Orin Nano 4GB/ 8GB 6.0 36.3 [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EY0H4iNmfUxPjCfiwfi59NEB8KQ9HuYEiu_0VLnsJVPjVw?e=oR4LYr)| Jetson Orin NX 8GB/ 16GB, Jetson Orin Nano 4GB/ 8GB 6.1 36.4 [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EdmS2OfqVg5IpQt9MeiBoT0BdS3Uft6DlJ1GPTJqZHoVNQ?e=ocmcHG)| Jetson Orin NX 8GB/ 16GB, Jetson Orin Nano 4GB/ 8GB 6.2 36.4.3 [Download](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EQLFs4vd8N5Lp0nhbP_KU-gB6kYGlXu3_N3KLiL25ze52Q?e=CWhIaE) | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

info

To verify the integrity of the downloaded firmware, you can compare the SHA256 hash value.

On an Ubuntu host machine, open the terminal and run the command `sha256sum <File>` to obtain the SHA256 hash value of the downloaded file. If the resulting hash matches the SHA256 hash provided [here](https://seeedstudio88-my.sharepoint.com/:x:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EXljqlpW3ZNNplIPBwJuyvsBdkW92geUmV7_7VN4SDlggA?e=Xea32u), it confirms that the firmware you downloaded is complete and intact.

**Note:** Currently we provide the above drivers. We will keep updating the drivers in the future with the release of new JetPack versions.

## Flash to Jetson

Here is a video for flashing JetPack 6.1 onto the A603 carrier board + Orin Nx 16GB module. You can refer to the video and the detailed steps below to flash your device.

note

Before moving onto flashing, it should be noted that Jetson Orin NX module only supports JetPack 5.1 and above, while Jetson Orin Nano module only supports JetPack 5.1.1 and above.

* JP5.1.1 for Jetson Orin NX* JP5.1.1 for Jetson Orin Nano* JP5.1.2* JP5.1.4* JP6.0* JP6.1* JP6.2

Here we will install **Jetpack 5.1.1** on the A603 Carrier Board with Jetson Orin NX module.

**Step 1:** [Download](https://developer.nvidia.com/embedded/jetson-linux-r3531) the NVIDIA drivers on the host PC. The required drivers are shown below:

![](https://files.seeedstudio.com/wiki/Jetson-AGX-Orin-32GB-H01-Kit/2.jpg)

**Step 2:** Move the downloaded peripheral drivers from before into the same folder with NVIDIA drivers. Now you will see three compressed files in the same folder.

![](https://files.seeedstudio.com/wiki/A603/6.png)

**Step 3:** Extract **Jetson\_Linux\_R35.3.1\_aarch64.tbz2** and **Tegra\_Linux\_Sample-Root-Filesystem\_R35.3.1\_aarch64.tbz2** by navigating to the folder containing these files, apply the changes and install the necessary prerequisites

```
tar xf Jetson_Linux_R35.3.1_aarch64.tbz2  
sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_R35.3.1_aarch64.tbz2 -C Linux_for_Tegra/rootfs/  
cd Linux_for_Tegra/  
sudo ./apply_binaries.sh  
sudo ./tools/l4t_flash_prerequisites.sh
```

**Step 4:** Extract **A603-Orin-NX-JP5.1.1.zip**. Here we additionally install the **unzip** package which is needed to decompress the .zip file

```
cd ..  
sudo apt install unzip   
unzip A603-Orin-NX-JP5.1.1.zip
```

Here it will ask whether to replace the files. Type **A** and press **ENTER** to replace the necessary files

![](https://files.seeedstudio.com/wiki/A603/7.jpg)

**Step 5:** Configure your username, password & hostname so that you do not need to enter the Ubuntu installation wizard after the device finishes booting.

Using `cd Linux_for_Tegra` first to ensure you are in the right directory.

```
sudo tools/l4t_create_default_user.sh -u {USERNAME} -p {PASSWORD} -a -n {HOSTNAME} --accept-license
```

For example (username:"nvidia", password:"nvidia", device-name:"nvidia-desktop"):

```
sudo tools/l4t_create_default_user.sh -u nvidia -p nvidia -a -n nvidia-desktop --accept-license
```

**Step 6:** Flash the system to either NVMe SSD or USB Flash drive

```
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 \  
  -c tools/kernel_flash/flash_l4t_external.xml -p "-c bootloader/t186ref/cfg/flash_t234_qspi.xml" \  
  --showlogs --network usb0 p3509-a02+p3767-0000 internal
```

You will see the following output if the flashing process is successful

![](https://files.seeedstudio.com/wiki/A603/10.jpg)

Here we will use NVIDIA L4T **35.3.1** to install **Jetpack 5.1.1** on the A603 Carrier Board with Jetson Orin Nano module

**Step 1:** [Download](https://developer.nvidia.com/embedded/jetson-linux-r3531) the NVIDIA drivers on the host PC. The required drivers are shown below:

![](https://files.seeedstudio.com/wiki/Jetson-AGX-Orin-32GB-H01-Kit/2.jpg)

**Step 2:** Move the downloaded peripheral drivers from before into the same folder with NVIDIA drivers. Now you will see three compressed files in the same folder.

![](https://files.seeedstudio.com/wiki/A603/8.png)

**Step 3:** Extract **Jetson\_Linux\_R35.3.1\_aarch64.tbz2** and **Tegra\_Linux\_Sample-Root-Filesystem\_R35.3.1\_aarch64.tbz2** by navigating to the folder containing these files, apply the changes and install the necessary prerequisites

```
tar xf Jetson_Linux_R35.3.1_aarch64.tbz2  
sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_R35.3.1_aarch64.tbz2 -C Linux_for_Tegra/rootfs/  
cd Linux_for_Tegra/  
sudo ./apply_binaries.sh  
sudo ./tools/l4t_flash_prerequisites.sh
```

**Step 4:** Extract **A603-Orin-NX-JP5.1.1.zip**. Here we additionally install the **unzip** package which is needed to decompress the .zip file

```
cd ..  
sudo apt install unzip   
unzip A603-Orin-NX-JP5.1.1.zip
```

Here it will ask whether to replace the files. Type **A** and press **ENTER** to replace the necessary files

![](https://files.seeedstudio.com/wiki/A603/9.png)

**Step 5:** Configure your username, password & hostname so that you do not need to enter the Ubuntu installation wizard after the device finishes booting

```
sudo tools/l4t_create_default_user.sh -u {USERNAME} -p {PASSWORD} -a -n {HOSTNAME} --accept-license
```

For example (username:"nvidia", password:"nvidia", device-name:"nvidia-desktop"):

```
sudo tools/l4t_create_default_user.sh -u nvidia -p nvidia -a -n nvidia-desktop --accept-license
```

**Step 6:** Flash the system to either NVMe SSD or USB Flash drive

```
cd Linux_for_Tegra  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 \  
  -c tools/kernel_flash/flash_l4t_external.xml -p "-c bootloader/t186ref/cfg/flash_t234_qspi.xml" \  
  --showlogs --network usb0 jetson-orin-nano-devkit internal
```

You will see the following output if the flashing process is successful.

![](https://files.seeedstudio.com/wiki/A603/10.jpg)

Here we will install **Jetpack 5.1.2** on the A603 Carrier Board with Jetson Orin module.

**Step 1:** [Download](https://developer.nvidia.com/embedded/jetson-linux-r3541) the NVIDIA drivers on the host PC. The required drivers are shown below:

![](https://files.seeedstudio.com/wiki/Jetson-AGX-Orin-32GB-H01-Kit/2.jpg)

**Step 2:** Move the downloaded peripheral drivers from before into the same folder with NVIDIA drivers. Now you will see three compressed files in the same folder.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/jp512_files.png)

**Step 3:** Extract **Jetson\_Linux\_R35.4.1\_aarch64.tbz2** and **Tegra\_Linux\_Sample-Root-Filesystem\_R35.4.1\_aarch64.tbz2** by navigating to the folder containing these files, apply the changes and install the necessary prerequisites.

```
tar xf Jetson_Linux_R35.4.1_aarch64.tbz2  
sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_R35.4.1_aarch64.tbz2 -C Linux_for_Tegra/rootfs/  
cd Linux_for_Tegra/  
sudo ./apply_binaries.sh  
sudo ./tools/l4t_flash_prerequisites.sh
```

**Step 4:** Extract **A603-JP5.1.2.zip**. Here we additionally install the **unzip** package which is needed to decompress the .zip file.

```
cd ..  
sudo apt install unzip   
unzip A603-JP5.1.2.zip
```

**Step 5:** Configure your username, password & hostname so that you do not need to enter the Ubuntu installation wizard after the device finishes booting.

```
sudo tools/l4t_create_default_user.sh -u {USERNAME} -p {PASSWORD} -a -n {HOSTNAME} --accept-license
```

For example (username:"nvidia", password:"nvidia", device-name:"nvidia-desktop"):

```
sudo tools/l4t_create_default_user.sh -u nvidia -p nvidia -a -n nvidia-desktop --accept-license
```

**Step 6:** Flash the system to NVMe SSD.

```
cd Linux_for_Tegra  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_external.xml -p "-c bootloader/t186ref/cfg/flash_t234_qspi.xml" --showlogs --network usb0 jetson-orin-nano-devkit internal
```

You will see the following output if the flashing process is successful.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/flash_successful.png)

Here we will install **Jetpack 5.1.4** on the A603 Carrier Board with Jetson Orin module.

**Step 1:** Download the NVIDIA drivers on the host PC:

```
wget https://developer.nvidia.com/downloads/embedded/l4t/r35_release_v6.0/release/jetson_linux_r35.6.0_aarch64.tbz2  
wget https://developer.nvidia.com/downloads/embedded/l4t/r35_release_v6.0/release/tegra_linux_sample-root-filesystem_r35.6.0_aarch64.tbz2
```

**Step 2:** Assemble the Flashing Package
Execute the following commands in order:

```
tar xf jetson_linux_r35.6.0_aarch64.tbz2  
sudo tar xpf tegra_linux_sample-root-filesystem_r35.6.0_aarch64.tbz2 -C Linux_for_Tegra/rootfs/  
tar zxpf 603_jp514.tar.gz # Unzip the driver package  
sudo cp -r 603_jp514/Linux_for_Tegra/* Linux_for_Tegra/ # Replace all files in the Linux_for_Tegra directory with the files from the driver package  
cd Linux_for_Tegra/ # Navigate to the Linux_for_Tegra path to run the flashing commands  
sudo ./apply_binaries.sh  
sudo ./tools/l4t_flash_prerequisites.sh
```

**Step 3:** Put the Device in Recovery Mode. The device must be in recovery mode for flashing. Follow these steps to enter recovery mode:

1. Short-circuit the REC pin and GND pin on the carrier board.
2. Connect the carrier board to the PC using a Micro USB data cable.
3. Power on the device.
4. On the PC, run `lsusb` and check if the product ID is one of the following: 7323, 7423, 7523, or 7623. This indicates the device is in recovery mode:
   * 7323: Orin NX 16G
   * 7423: Orin NX 8G
   * 7523: Orin Nano 8G
   * 7623: Orin Nano 4G

**Step 4:** Flash the Device.

```
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_external.xml -p "-c bootloader/t186ref/cfg/flash_t234_qspi.xml" --showlogs --network usb0 jetson-orin-nano-devkit internal
```

**Tips:** Backup the System and Flash Using the Backup Image

1. If you flashed the system onto the SSD, run the following commands:

   * To backup the image (requires recovery mode):

     ```
     sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -b jetson-orin-nano-devkit
     ```
   * To flash using the backup image (requires recovery mode):

     ```
     sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -r jetson-orin-nano-devkit
     ```

   Once completed, the device can boot into the system.

Here we will install **Jetpack 6.0** on the A603 Carrier Board with Jetson Orin module.

**Step 1:** [Download](https://developer.nvidia.com/embedded/jetson-linux-r363) the NVIDIA drivers on the host PC. The required drivers are shown below:

![](https://files.seeedstudio.com/wiki/Jetson-AGX-Orin-32GB-H01-Kit/2.jpg)

**Step 2:** Move the downloaded peripheral drivers from before into the same folder with NVIDIA drivers. Now you will see three compressed files in the same folder.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/jp6.0_files.png)

**Step 3:** Extract **Jetson\_Linux\_R36.3.0\_aarch64.tbz2** and **Tegra\_Linux\_Sample-Root-Filesystem\_R36.3.0\_aarch64.tbz2** by navigating to the folder containing these files.

```
sudo tar xf Jetson_Linux_R36.3.0_aarch64.tbz2  
sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_R36.3.0_aarch64.tbz2 -C Linux_for_Tegra/rootfs/
```

**Step 4:** Extract **A603-JP6.0.zip**. Here we additionally install the **unzip** package which is needed to decompress the .zip file.

```
cd ..  
sudo apt install unzip   
sudo unzip A603-JP6.0.zip
```

Then, copy the three folders `(bootloader, kernel, rootfs in A603-JP6.0.zip)` to Linux\_for\_Tegra folder.

**Step 5:** Apply the changes and install the necessary prerequisites

```
cd Linux_for_Tegra/  
sudo ./apply_binaries.sh  
sudo ./tools/l4t_flash_prerequisites.sh
```

**Step 6:** Configure your username, password & hostname so that you do not need to enter the Ubuntu installation wizard after the device finishes booting.

```
sudo tools/l4t_create_default_user.sh -u {USERNAME} -p {PASSWORD} -a -n {HOSTNAME} --accept-license
```

For example (username:"nvidia", password:"nvidia", device-name:"nvidia-desktop"):

```
sudo tools/l4t_create_default_user.sh -u nvidia -p nvidia -a -n nvidia-desktop --accept-license
```

**Step 7:** Flash the system to NVMe SSD.

```
cd Linux_for_Tegra  
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_t234_nvme.xml -p "-c bootloader/generic/cfg/flash_t234_qspi.xml" --showlogs --network usb0 jetson-orin-nano-devkit internal
```

You will see the following output if the flashing process is successful.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/flash_successful.png)

Here we will install **Jetpack 6.1** on the A603 Carrier Board with Jetson Orin module.

**Step 1:** Download the NVIDIA drivers on the host PC:

```
wget https://developer.nvidia.com/downloads/embedded/l4t/r36_release_v4.0/release/Jetson_Linux_R36.4.0_aarch64.tbz2  
wget https://developer.nvidia.com/downloads/embedded/l4t/r36_release_v4.0/release/Tegra_Linux_Sample-Root-Filesystem_R36.4.0_aarch64.tbz2
```

**Step 2:** Assemble the Flashing Package
Execute the following commands in order:

```
tar xf Jetson_Linux_R36.4.0_aarch64.tbz2  
sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_R36.4.0_aarch64.tbz2 -C Linux_for_Tegra/rootfs/  
tar xpf 603_jetpack6.1.tar.gz # Unzip the driver package  
sudo cp -r 603_jetpack6.1/Linux_for_Tegra/* Linux_for_Tegra/ # Replace all files in the Linux_for_Tegra directory with the files from the driver package  
cd Linux_for_Tegra/ # Navigate to the Linux_for_Tegra path to run the flashing commands  
sudo ./apply_binaries.sh  
sudo ./tools/l4t_flash_prerequisites.sh
```

**Step 3:** Put the Device in Recovery Mode. The device must be in recovery mode for flashing. Follow these steps to enter recovery mode:

1. Short-circuit the REC pin and GND pin on the carrier board.
2. Connect the carrier board to the PC using a Micro USB data cable.
3. Power on the device.
4. On the PC, run `lsusb` and check if the product ID is one of the following: 7323, 7423, 7523, or 7623. This indicates the device is in recovery mode:
   * 7323: Orin NX 16G
   * 7423: Orin NX 8G
   * 7523: Orin Nano 8G
   * 7623: Orin Nano 4G

**Step 4:** Flash the Device.

```
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_t234_nvme.xml -p "-c bootloader/generic/cfg/flash_t234_qspi.xml"   --showlogs --network usb0 jetson-orin-nano-devkit internal
```

info

Backup the System and Flash Using the Backup Image

If you flashed the system onto the SSD, run the following commands:

* To backup the image (requires recovery mode):

  ```
  sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -b jetson-orin-nano-devkit
  ```
* To flash using the backup image (requires recovery mode):

  ```
  sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -r jetson-orin-nano-devkit
  ```

  Once completed, the device can boot into the system.

Here we will install **Jetpack 6.2** on the A603 Carrier Board with Jetson Orin module.

**Step 1:** Download the NVIDIA drivers on the host PC:

```
wget https://developer.nvidia.com/downloads/embedded/l4t/r36_release_v4.3/release/Jetson_Linux_r36.4.3_aarch64.tbz2  
wget https://developer.nvidia.com/downloads/embedded/l4t/r36_release_v4.3/release/Tegra_Linux_Sample-Root-Filesystem_r36.4.3_aarch64.tbz2
```

**Step 2:** Assemble the Flashing Package

Please note that we need to put the Nvidia driver and the peripheral drivers in the same directory, and then open the terminal in that directory and execute the following code:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/driver_files_directory_layout.png)

```
tar xf Jetson_Linux_r36.4.3_aarch64.tbz2  
sudo tar xpf Tegra_Linux_Sample-Root-Filesystem_r36.4.3_aarch64.tbz2 -C Linux_for_Tegra/rootfs/  
sudo tar zxpf 603_jp62.tar.gz  
sudo cp -r 603_jp62/Linux_for_Tegra/* Linux_for_Tegra/  
cd Linux_for_Tegra/  
sudo ./tools/l4t_flash_prerequisites.sh  
sudo ./apply_binaries.sh
```

**Step 3:** Put the Device in Recovery Mode. The device must be in recovery mode for flashing. Follow these steps to enter recovery mode:

1. Short-circuit the REC pin and GND pin on the carrier board.
2. Connect the carrier board to the PC using a Micro USB data cable.
3. Power on the device.
4. On the PC, run `lsusb` and check if the product ID is one of the following: 7323, 7423, 7523, or 7623. This indicates the device is in recovery mode:
   * 7323: Orin NX 16G
   * 7423: Orin NX 8G
   * 7523: Orin Nano 8G
   * 7623: Orin Nano 4G

**Step 4:** Flash the Device.

```
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 \  
  -c tools/kernel_flash/flash_l4t_t234_nvme.xml -p "-c bootloader/generic/cfg/flash_t234_qspi.xml" \  
  --showlogs --network usb0 jetson-orin-nano-devkit-super internal
```

info

Tips: Backup the System and Flash Using the Backup Image

If you flashed the system onto the SSD, run the following commands:

* To backup the image (requires recovery mode):

  ```
  sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -b jetson-orin-nano-devkit-super
  ```
* To flash using the backup image (requires recovery mode):

  ```
  sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -r jetson-orin-nano-devkit-super
  ```

  Once completed, the device can boot into the system.

## CAN Interfaces

Since there is a CAN transceiver on A603 carrier board, you don’t extra transceiver like dev kit.

**Step1.** Install `devmem2` to write values to registers:

```
sudo apt-get install devmem2
```

**Step2.** Write values according to [here](https://docs.nvidia.com/jetson/archives/r36.4/DeveloperGuide/HR/ControllerAreaNetworkCan.html#jetson-platform-details).

```
sudo devmem2 0x0c303010 w 0xc400  
sudo devmem2 0x0c303018 w 0xc458
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/send1.png)![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/send2.png)

**Step3.** Load Kernel modules:

```
sudo modprobe can  
sudo modprobe can_raw  
sudo modprobe mttcan
```

After loading these modules, you should be able to see these logs in `sudo dmesg`:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/check_can.png)

**Step4.** Bring up can0 interface:

```
sudo ip link set can0 type can bitrate 500000
```

Optionally, you can change the bitrate to 1000000. Then, bring up can0:

```
sudo ip link set can0 up
```

Check the interface with `ifconfig`:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/ifconfig.png)

**Step5.** Sending data (require can-utils installed). On the other side, we used a MCU with CAN Expansion board to receive data.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/hardware.png)

Run `cansend can0 123#11.22.33.50` on jetson terminal:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/cansend.png)

**Step6.** Receiving data. On the other side, we used a MCU with CAN Expansion board to send data.

Run `candump can0` on jetson terminal:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A603/candump.png)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.