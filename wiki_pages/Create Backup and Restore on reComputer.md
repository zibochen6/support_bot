# Create Backup and Restore on reComputer

## Introduction

reComputer is a powerful and compact intelligent edge box to bring up to 275TOPS modern AI performance to the edge.When you have configured and installed the software and environment necessary for your business on recomputer, and need to replicate the project from another new recomputer, reinstalling the software is not efficient. Therefore, this wiki page will use [reComputer J3011](https://www.seeedstudio.com/reComputer-J3011B-p-6405.html) to introduce how to back up your existing software and environment on the recomputer series, making it convenient for you to restore and transplant it to the new recomputer.

note

Our testing platform is reComputer J3011, JetPack 5.1.3 is provided for reference.

## Prerequisite

* Ubuntu Host Computer
* USB Type-C data transmission cable
* reComputer J3011 (with JetPack 5.1.3 OS)

info

Installed and configured necessary software and applications on your reComputer. Ensure these modifications do not impair the device's boot functionality. It's recommended to reboot the device after making changes to confirm stability.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/jtop.png)

Like the screenshot above, we installed the jtop software, where we can use these commands on the terminal directly.

## Backing Up the System

**Step 1.** Setting the device into recovery mode refer to this [wiki page](https://wiki.seeedstudio.com/reComputer_J4012_Flash_Jetpack/#enter-force-recovery-mode).

**Step 2.** Obtain the JetPack BSP corresponding to your Jetson module. For JetPack 5.1.3, download the Jetson Linux R35.5.0 BSP from [NVIDIA's official site.](https://developer.nvidia.com/embedded/jetson-linux-r3550)

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/download_bsp.jpg)

**Step 3.** Extract the BSP file to access the Linux\_for\_Tegra directory.

```
tar -xvzf jetson-linux-*.tbz2  
# For Jetpack 5.1.3: tar -xvzf Jetson_Linux_R35.5.0_aarch64.tbz2
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/zip.jpg)

**Step 4.** Copy the contents of Linux\_for\_Tegra to your JetPack flashing package directory (e.g., mfi\_recomputer-orin).

note

"flashing package directory" is the directory file used during the process of flashing the system.

Use the `-rn` options to preserve existing files:

```
sudo cp -rn Linux_for_Tegra/* mfi_recomputer-orin
```

**Step 5.** Navigate to your JetPack flashing package directory:

```
cd /path/to/mfi_recomputer-orin
```

**Step 6.** Execute the backup script, specifying your storage device and desired backup name:

```
sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -b recomputer-orin
```

info

-b `<target_board>` replace with your device

note

you can navigate to your Jepack flashing package directory and find a `xxx.conf` file.
`xxx` is your `<target_board>`

```
ls | grep *.conf
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/conf_file1.jpg)

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/backup_start.png)

wait patiently until it finished.
If all goes well, you will see something similar to the screenshot below in the terminal:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/success_back1.png)

note

During this process, your device may reboot many times like the flashing process, you are not recommended to use virtual machines or WSL because it might lose connection and cause the backup/restore process failed. You may encounter some missing files; you can open the `recomputer-orin.conf` and remove the file that didn’t exist.
Usually these are temporary device tree overlay object files; they don't affect the backup and restore results. But if you made modifications to BSP, you will need to merge your overlay files.

## Restoring the System

**Step 1.** Insert a new, empty [SSD](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html) into your reComputer.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/new_ssd.jpg)

**Step 2.** Enter force recovery mode as [previously described.](#Recovery)

**Step 3.** On your host system, navigate to your JetPack flashing package directory and execute the restore command on host:

```
sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -r recomputer-orin
```

If all goes well, you will see something similar to the screenshot below in the terminal:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/finish_store1.png)

**Step 4.** Power up the jetson device, use the username and password we previously set. And test some software we previously installed. If it worked, then our restore is successful.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/jtop2.png)

Because we had installed jtop in our previous system, we can directly launch jtop in the terminal of the new system.

info

Additionally, following cases have been tested for backup and restore:

* Restore the backup to original SSD.
* Restore the backup to different SSD.
* Restore the backup to same carrier board, with Jetson module in same batch, different SSDs.