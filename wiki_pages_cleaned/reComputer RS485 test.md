# reComputer RS485 test

## Introduction

This wiki applies to all reComputer devices with RS485 interfaces include reComputer R10/R11/R20/R21 and can be used to test whether the RS485 receiving and transmitting functions are working correctly.

## Hardware Preparation

[TABLE COMPRESSED]
Columns: reComputer r1000 reComputer r1100 reComputer r2000 reComputer r2100 | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-R1035-10-p-5925.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-R1113-10-p-6258.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html)

## Connection

Select a pair of RS485 interfaces to test， please connect A1 to A2 and connect B1 to B2:

## Prepare software

Use the following command to download：
```
git clone https://github.com/ackPeng/R1100_TEST.git
```Compile
```
gcc -o serial_test serial_test.c
```## Test
```
#From ttyACM0 to ttyACM1, send RS485_1 to RS485_2  
./serial_test /dev/ttyACM0 /dev/ttyACM1 115200
```
```
# From ttyACM1 to ttyACM0, send RS485_2 to RS485_1  
./serial_test /dev/ttyACM1 /dev/ttyACM0 115200
```## Tech Support

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.
