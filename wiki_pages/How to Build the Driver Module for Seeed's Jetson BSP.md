# How to Build the Driver Module for Seeed's Jetson BSP

**When the required `.ko` driver module is not available in reComputer/reServer, you can compile the driver module on Jetson and load it. This wiki demonstrates the specific steps and important notes, using JetPack 6.2 as an example.**

## 1. Prepare workspace

This article uses **L4T 36.4.3**, which corresponds to **JetPack 6.2** BSP, as an example to show how to compile the .ko driver module for `pl2303` (a USB-to-serial related driver) on **reComputer/reServer**.

tip

This tutorial downloads the source code on the Jetson and compiles the `.ko` kernel modules.

First, download the BSP source code from NVIDIA’s official website according to your L4T version.

If you're unsure about the relationship between L4T versions and JetPack versions, you can refer to this link:
<https://developer.nvidia.com/embedded/jetpack-archive>.

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/L4T-jetpack.png
)

Search for the specific **L4T (Linux for Tegra)** release you want to compile, e.g.:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/google_L4T.jpg)

Download the corresponding BSP source code from NVIDIA’s website:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/download-src.png)

Place the downloaded BSP source code archive into your working directory, then run the following commands in the terminal to fully extract it:

```
# First extract the main file  
tar -xjf public_sources.tbz2  
  
# Enter the extracted directory  
cd Linux_for_Tegra/source  
  
# Recursively extract all .tbz2, .tar.bz2, .tar.gz, .tgz, .tar.xz files  
find . -type f \( -name "*.tbz2" -o -name "*.tar.bz2" -o -name "*.tar.gz" -o -name "*.tgz" -o -name "*.tar.xz" \) -exec bash -c '  
    dir=$(dirname "$1")  
    filename=$(basename "$1")  
    cd "$dir"  
    if [[ "$filename" == *.tbz2 || "$filename" == *.tar.bz2 ]]; then  
        tar -xjf "$filename"  
    elif [[ "$filename" == *.tar.gz || "$filename" == *.tgz ]]; then  
        tar -xzf "$filename"  
    elif [[ "$filename" == *.tar.xz ]]; then  
        tar -xJf "$filename"  
    fi  
    cd - > /dev/null  
' _ {} \;
```

After extracting all the archives, navigate to `Linux_for_Tegra/source` and locate the driver source path based on keywords:

```
sudo find . -type f -name "*<keyword>*"  
  
# For exmaple:  
sudo find . -type f -name "*pl2303*"
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/path-pl2303.png)

Create a new workspace for compilation. According to the printed source path in the terminal, copy the driver source code into this workspace.

Then, inside the workspace, create a `Makefile` for compilation with the following content:

```
obj-m   += pl2303.o  
all:  
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules  
clean:  
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

Here, `pl2303.o` should be replaced with the corresponding name of the driver you want to compile.

The workspace will look similar to the figure below, containing both the source file and the `Makefile`:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/wkspace-ko.png)

Before compiling, you need to establish a symbolic link:

```
# Remove existing redundant directory if it exists  
sudo rm -r /lib/modules/$(uname -r)/build  
  
# Create symbolic link  
sudo ln -s /usr/src/linux-headers-$(uname -r)-ubuntu22.04_aarch64/3rdparty/canonical/linux-jammy/kernel-source /lib/modules/$(uname -r)/build
```

After creating the symbolic link, run the following command in your workspace to compile and obtain the `.ko` driver module:

```
make
```

After compilation, the `.ko` file will be generated in the current directory:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/compiled-ko.png)

Next, copy the `.ko` file to the correct target path:

```
sudo cp pl2303.ko /lib/modules/$(uname -r)/kernel/drivers/usb/serial/
```

For compiled `.ko` driver modules, the target path prefix is always `/lib/modules/$(uname -r)/kernel/`. The suffix depends on the type of driver module and can be inferred from the relative path of the source code, which gives the full target path:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/mark_path.png)

After copying to the target path, load the `.ko` driver module:

```
sudo depmod -a  
sudo modprobe pl2303
```

Once successfully loaded, you can run `modinfo <driver_name>` to verify:

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/modinfo-pl.png)