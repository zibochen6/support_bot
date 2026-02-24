# 如何在 reComputer r1000 上使用 UPS 读取输入电压

## 介绍

本 wiki 文章主要说明如何在 reComputer R10 和 R11 系列上安装 UPS 模块，并使用 UPS 读取输入电压。

## 硬件准备

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer R1000 UPS 模块|  |  |  |  | | --- | --- | --- | --- | ||  |  |  |  | | --- | --- | --- | --- | | ||  |  | | --- | --- | | [**立即获取 🖱️**](https://www.seeedstudio.com/reComputer-R1025-10-p-5895.html)  [**立即获取 🖱️**](https://www.seeedstudio.com/SuperCAP-UPS-LTC3350-Module-p-5934.html) | | | | | |

> 注意
> 请参考此[链接](https://wiki.seeedstudio.com/cn/recomputer_r1000_assembly_guide/#assemble-ups-and-poe-module)在 R1000 上安装 UPS。

## 软件准备

### 步骤 1：检查 UPS 模块

```
sudo apt update  
sudo apt install i2c-tools  
sudo i2cdetect -y 6
```

![](https://files.seeedstudio.com/wiki/reComputer-R1000/ups/check_ups.png)

### 步骤 2：从 GitHub 下载仓库

```
git clone https://github.com/Seeed-Projects/Read-UPS-input-voltage.git  
cd Read-UPS-input-voltage  
sudo apt update  
sudo apt install python3-smbus
```

### 步骤 3：开始监控电压

```
python -m venv .venv --system-site-packages && source .venv/bin/activate  
python read_voltage.py
```

## 结果

![](https://files.seeedstudio.com/wiki/reComputer-R1000/ups/ups_result.png)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。