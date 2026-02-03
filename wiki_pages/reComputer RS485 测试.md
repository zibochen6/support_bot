# reComputer RS485 测试

## 简介

本教程适用于所有带有 RS485 接口的 reComputer 设备，包括 reComputer R10/R11/R20/R21，可用于测试 RS485 接收和发送功能是否正常工作。

## 硬件准备

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer r1000 reComputer r1100 reComputer r2000 reComputer r2100|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-R1035-10-p-5925.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-R1113-10-p-6258.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | | | | | | | |

## 连接

选择一对 RS485 接口进行测试，请将 A1 连接到 A2，将 B1 连接到 B2：

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/RS485/RS485_connection.jpg)

## 准备软件

使用以下命令下载：

```
git clone https://github.com/ackPeng/R1100_TEST.git
```

编译

```
gcc -o serial_test serial_test.c
```

## 测试

```
#From ttyACM0 to ttyACM1, send RS485_1 to RS485_2  
./serial_test /dev/ttyACM0 /dev/ttyACM1 115200
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/RS485/compile_and_test.png)

```
# From ttyACM1 to ttyACM0, send RS485_2 to RS485_1  
./serial_test /dev/ttyACM1 /dev/ttyACM0 115200
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/RS485/send_test.png)

## 技术支持

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。