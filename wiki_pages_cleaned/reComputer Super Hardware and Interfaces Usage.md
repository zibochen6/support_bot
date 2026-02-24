# reComputer Super Hardware and Interfaces Usage

This wiki introduces the various different hardware and interfaces on the reComputer Super and how to use them to expand your project ideas.

## CSI Camera

The reComputer Super supports standard 4 MIPI CSI cameras for image and video capture. Please follow the steps below to connect and test your camera.

### Hardware Connection

**Step1.** Open the back cover of the Recomputer Super.

**Step2.** Connect the MIPI CSI camera to the appropriate CSI port on the reComputer Super board.

**Step3.** Secure the camera and ensure the connection is firm.

### Usage Instruction

Before using the CSI camera, please ensure you have installed a JetPack version with the necessary camera drivers.

**Step1.** Check if the camera is recognized by the system:
```
ls /dev/video*
```**Step2.** (Optional) Install video utilities if not already present:
```
sudo apt install v4l-utils
```**Step3.** Start the camera and display the video stream using the following command:
```
nvgstcapture-1.0 --sensor-id=0
```Change `--sensor-id` to the appropriate value if you have multiple cameras.

---

## USB

The reComputer Super has a total of 4 USB 3.2 ports and 1 USB 2.0 Type-C port for debugging.

### USB 3.2 port

We can enter `watch -n 1 lsusb -tv` in the Jetson terminal to probe the USB ports. Once a USB device is connected, the detailed information about that port will be displayed here.

Additionally, you can test the read and write speed of USB storage devices by using the `dd` command:

* **Read:**
```
  sudo dd if=/dev/sda of=/dev/null bs=1024M count=5 iflag=direct
  ```* **Write:**
```
  sudo dd if=/dev/zero of=/dev/sda bs=1024M count=5 conv=fdatasync
  ```### USB 2.0 Type-C port

Using this serial port, via the USB C data cable, you can monitor the debugging information of input and output on the PC side.

**Step1.** Switch the switch to the debug mode.

**Step2.** Connect the PC via a USB data cable, downloaded the [CP210X Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads) on your PC.

**Step3.** Connect the PC via a USB data cable, extract the downloaded file and install driver on your PC.

**Step4.** Open Open the Device Manager on your Windows PC and check the COM port number assigned to the reComputer Super. It should appear under "Ports (COM & LPT)" as "Silicon Labs CP210x USB to UART Bridge (COMX)", where X is the COM port number.

**Step5.** Open the serial port tool(Here, we use the MobaXterm tool as an example), create a new session.

**Step6.** Select the Serial tool.

**Step7.** Select corresponding serial port, set the baud rate to 115200 and click "OK".

**Step8.** Login your reComputer Super with the username and password.

## M.2 Key M

M.2 Key M is an interface designed for high-speed solid-state drives (SSDs), providing ultra-fast data transfer speeds, ideal for high-performance applications.

### Supported SSD are as follows

* [128GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html)
* [256GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-256GB-p-5333.html)
* [512GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-512GB-p-5334.html)
* [1TB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-1TB-p-5767.html)
* [2TB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-2TB-p-6265.html)

### Hardware Connection

### Usage Instruction

Open the terminal in Jetson device and enter the following command to test the SSD's read and write speed.
```
#create a blank test file first  
sudo touch /ssd/test  
dd if=/dev/zero of=/home/seeed/ssd/test bs=1024M count=5 conv=fdatasync
```Please run `sudo rm /home/seeed/ssd/test` command to delete the cache files after the test is complete.

## M.2 Key E

The M.2 Key E interface is a compact, high-speed data interface designed for wireless communication modules such as Wi-Fi and Bluetooth, used to expand wireless capabilities.

### Hardware Connection

### Usage Instruction

After installing the Wi-Fi module and powering on the device, we can configure the device's Wi-Fi and Bluetooth settings.

Of course, we can also check the device's operating status using the following commands.
```
ifconfig
```**Bluetooth:**
```
bluetoothctl  
scan on
```## Mini PCIe

The reComputer super comes with a mini-PCIe for LTE 4G module.

#### Hardware Connection

If you want to remove the SIM card, push the card in to hit the internal spring so that the SIM will come out of the slot

### Usage Instruction

**Step1.** Install minicom:
```
sudo apt update  
sudo apt install minicom -y
```**Step2.** Enter the serial console of the connected 4G module so that we can enter AT commands and interact with the 4G module:
```
sudo minicom -D /dev/ttyUSB2 -b 115200
```**Step3.** Press Ctrl+A and then press E to turn on local echo.

**Step4.** Enter the command "AT" and press enter. If you see the response as "OK", the 4G module is working properly.

**Step5.** Enter the command "ATI" to check the module information.

Using 4G network for internet access

## RTC

The reComputer Super features RTC interfaces, providing accurate timekeeping even when the system is powered off.

### Hardware Connection

Connect a 3V CR1225 coin cell battery to the RTC socket on the board as shown below. Make sure the **positive (+)** end of the battery is facing upwards.

### Usage Instruction

**Step1.** Connect an RTC battery as mentioned above.

**Step2.** Turn on reComputer Super.

**Step3.** On the Ubuntu Desktop, click the drop-down menu at the top right corner, navigate to `Settings > Date & Time`, connect to a network via an Ethernet cable and select **Automatic Date & Time** to obtain the date/ time automatically.

If you have not connected to internet via Ethernet, you can manually set the date/ time here.

**Step4.** Open a terminal window, and execute the below command to check the hardware clock time:
```
cat /sys/devices/platform/bpmp/bpmp\:i2c/i2c-4/4-003c/nvvrs-pseq-rtc/rtc/rtc0/time
```.png)

**Step5.** Disconnect the network connection and reboot the device. You will find that the system time has lost power but still functions normally.

## Ethernet

There are 2 RJ45 Gigabit Ethernet on reComputer Super supported 10/100/1000M. ETH0 is the native Ethernet port, and the other one ETH1 is converted from PCIe.

There are 2 LEDs (green and yellow) on each Ethernet port:

* Green LED: ON only when connected to 1000M/10G network.
* Yellow LED: Shows the network activity status.

Test the Ethernet speed:
```
iperf3 -c 192.168.254.100 -R
```-c `<ip address>` is the server IP address, and -R means reverse mode.
```
iperf3 -c 192.168.254.100
```## LED Indicators

The reComputer Super is equipped with 2 LED indicators (PWR and ACT) to show power status and system activity, allowing users to monitor device operation in real time.

## Fan

The reComputer Super is equipped with two types of fan connectors to meet different voltage and cooling needs:

* 1x 4-Pin Fan Connector (5V PWM): Designed for low-voltage, low-power silent fans, this connector supports PWM speed control, allowing intelligent fan speed adjustment based on system temperature to improve energy efficiency and reduce noise.
* 1x 4-Pin Fan Connector (12V PWM): Compatible with standard 12V PWM fans, it also supports precise speed control, making it ideal for high-performance cooling requirements.

### Hardware Connection

For more information, please check [here](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html?highlight=fan#fan-profile-control).

**Set fan speed:**
```
sudo -i  
echo 100 > /sys/bus/platform/devices/pwm-fan/hwmon/hwmon1/pwm1
```Additionally, we can manually set the fan speed using the jtop tool.

## CAN

The reComputer Super series provides a CAN interface where the CAN signal is output directly from the SOM at TTL/CMOS levels, which is a non-standard differential signal requiring an external CAN transceiver to connect to a standard CAN bus; it supports CAN FD frame formats, allowing extended data length and higher data rates, making it suitable for industrial automation, robotics, automotive prototyping, and other applications requiring reliable, real-time communication.

### Hardware Connection

Please note the sequence of the connected lines (R OUT ↔ RX, D IN ↔ TX), and then convert them to CAN\_L and CAN\_H through the CAN bus transceiver.

According to the [Datasheet of reComputer Super](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_super_user_manual.pdf), connect the CAN heater to the CAN bus transceiver in the corresponding manner, then connect the CAN bus transceiver to the [USB to CAN Analyzer Adapter](https://www.seeedstudio.com/USB-CAN-Analyzer-p-2888.html), and finally connect it to the Jetson for loopback communication testing.

### Usage Instruction

**Step 1.** Configure and open can0:
```
sudo ip link set can0 down  
sudo ip link set can0 type can bitrate 500000  
sudo ip link set can0 up
```**Step 2.** Communication test.
Open a terminal to receive signals.
```
candump can0
```**Step 3.** Open another terminal to send the signal.
```
cansend can0 123#abcdabcd
```## Extension Port

The Extension Port includes a 40-pin extension header and a 12-pin control and UART header, providing versatile connectivity options for peripherals and communication interfaces.

### 40-Pin Extension Header

The 40-Pin Extension Header is a versatile expansion interface that provides various functions such as GPIO, I2C, SPI, and UART, making it convenient for connecting sensors, peripherals, or other modules.

The detail of 40-pin header is shown below:

[TABLE COMPRESSED]
Columns: Header Pin Signal BGA Pin Default Function | 1 3.3V - Main 3.3V Supply | 2 5V - Main 5V Supply | 3 I2C1\_SDA PDD.02 I2C #1 Data | 4 5V - Main 5V Supply | 5 I2C1\_SCL PDD.01 I2C #1 Clock | 6 GND - Ground | 7 GPIO09 PAC.06 General Purpose I/O | 8 UART1\_TXD PR.02 UART #1 Transmit | 9 GND - Ground | 10 UART1\_RXD PR.03 UART #1 Receive | 11 UART1\_RTS PR.04 UART #1 Request to Send ...

### Usage Instruction

Simple GPIO control example
```
#install  
sudo apt-get install gpiod  
  
# Search for the corresponding number for the pin  
sudo gpiofind PH.00  
gpiochip0 43  
  
#Set the pin to H, then press Enter to release.  
sudo gpioset --mode=wait 0 43=1  
  
#Set the Pin to L, then press Enter to release.  
sudo gpioset --mode=wait 0 43=0  
  
#gpio 0_119 Low level maintained for 2 seconds  
sudo gpioset --mode=time -s 2 0 119=0  
  
#input  
sudo gpioget 0 43
```**If you want to configure the GPIO that is not enabled by default, please refer to the following steps:**

Enable 40-Pin Header:
```
  sudo /opt/nvidia/jetson-io/jetson-io.py
```Save and reboot.

**Configure the uncontrolled GPIO through the Overlay configuration:**

**Step 1.** Download and extract the [overlay package](https://files.seeedstudio.com/wiki/overlay.zip) to your jetson device.
```
wget https://files.seeedstudio.com/wiki/overlay.zip
```**Step 2.** Copy build.sh and gpio-overlay.dts to Jetson.

**Step 3.** Edit the `pio-overlay.dts` file and modify it to include the pinmux definitions for the pins you need.

more details you can see in [jetson-orin-nx-and-orin-nano-series-pinmux-config](https://developer.nvidia.com/downloads/jetson-orin-nx-and-orin-nano-series-pinmux-config-template)

**Step 3.** Enable overlay configuration.
```
sudo bash ./build.sh  
#The following command needs to be executed only once.  
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "seeed gpio config Overlay"
```**Step 4.** Reboot the device enables the configuration to take effect.
```
sudo reboot
```**Step 5.** Now you can control the pins by `gpioset` that were just modified.
```
#For example px7  
sudo gpioset --mode=wait 0 121=1
```### 12-Pin Control and UART Header

The 12-Pin Control and UART Header provides essential control signals and UART communication interfaces for connecting and managing external devices.

The pin functions of reComputer Super are similar to those of reComputer Classic. For more detailed information, please refer to [here](https://wiki.seeedstudio.com/J401_carrierboard_Hardware_Interfaces_Usage/#gpio).

## HDMI

reComputer Super is equipped with an HDMI 2.1 Type A port, which supports a resolution of 7680x4320. This allows for ultra-high-definition video output.
