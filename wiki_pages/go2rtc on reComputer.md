# go2rtc on reComputer

## Introduction

[go2rtc](https://github.com/AlexxIT/go2rtc) is an open-source WebRTC framework designed to facilitate real-time media streaming over the internet. It is developed by the XTLS team and aims to combine WebRTC with other media protocols like RTSP, RTMP, and HLS for efficient real-time video and audio transmission.

[WebRTC](https://github.com/webrtc) (Web Real-Time Communication) is a widely used protocol for establishing peer-to-peer connections and enabling real-time media exchange such as video calls, live broadcasts, and other real-time applications. go2rtc makes it easier to implement WebRTC in environments where different media protocols need to be converted into WebRTC streams for low-latency and scalable transmission.

## Prerequisites

### Hardware Requirements

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html) | | | | | | | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

## Download and run go2rtc

### Update system

Please use the following command to run.

```
sudo apt update  
sudo apt upgrade -y
```

### Download go2rtc

Please use the following command to run.

```
wget https://nightly.link/AlexxIT/go2rtc/workflows/build/master/go2rtc_linux_arm64.zip  
tar -xvzf go1.24.0.linux-arm64.tar.gz  
chmod +x go2rtc_linux_arm64
```

### Create go2rtc.yaml

Please use the following command to run.

```
nano go2rtc.yaml
```

Please fill in the following configuration with your actual IP address.

```
streams:  
  stream1:  
    url: rtsp://admin:[email protected]:554/cam/realmonitor?channel=1&subtype=1  
    protocol: rtsp  
    codec: h264  
  
server:  
  api: :1984   
  rtsp: :8554    
  webrtc: :8555
```

### Run go2rtc

Please use the following command to run.

```
 ./go2rtc_linux_arm64
```

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/go2rtc/run_go2rtc.png)

Open port `1984` on the host, and click the `Stream`button.

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/go2rtc/go2rtc.png)

## Result

Once we have configured everything, we can view the live feed from the current camera.

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/go2rtc/go2rtc.gif)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.