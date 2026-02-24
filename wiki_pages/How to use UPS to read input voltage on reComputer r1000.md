# How to use UPS to read input voltage on reComputer r1000

## Introduction

This wiki article primarily explains how to install the UPS module on the reComputer R10 and R11 series and use the UPS to read the input voltage.

## Hardware Preparation

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer R1000 UPS model|  |  |  |  | | --- | --- | --- | --- | ||  |  |  |  | | --- | --- | --- | --- | | ||  |  | | --- | --- | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-R1025-10-p-5895.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/SuperCAP-UPS-LTC3350-Module-p-5934.html) | | | | | |

> Note
> Please refer to this [link](https://wiki.seeedstudio.com/recomputer_r1000_assembly_guide/#assemble-ups-and-poe-module) to install the UPS on the R1000.

## Software prepare

### Step 1: Check UPS module

```
sudo apt update  
sudo apt install i2c-tools  
sudo i2cdetect -y 6
```

![](https://files.seeedstudio.com/wiki/reComputer-R1000/ups/check_ups.png)

### Step 2: Download repository from GitHub

```
git clone https://github.com/Seeed-Projects/Read-UPS-input-voltage.git  
cd Read-UPS-input-voltage  
sudo apt update  
sudo apt install python3-smbus
```

### Step 3: Start monitoring voltage

```
python -m venv .venv --system-site-packages && source .venv/bin/activate  
python read_voltage.py
```

## Result

![](https://files.seeedstudio.com/wiki/reComputer-R1000/ups/ups_result.png)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.