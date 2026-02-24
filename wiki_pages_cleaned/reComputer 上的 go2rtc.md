# reComputer 上的 go2rtc

## 简介

[go2rtc](https://github.com/AlexxIT/go2rtc) 是一个开源的 WebRTC 框架，旨在促进通过互联网进行实时媒体流传输。它由 XTLS 团队开发，旨在将 WebRTC 与其他媒体协议（如 RTSP、RTMP 和 HLS）结合，以实现高效的实时视频和音频传输。

[WebRTC](https://github.com/webrtc)（Web 实时通信）是一种广泛使用的协议，用于建立点对点连接并实现实时媒体交换，如视频通话、直播和其他实时应用。go2rtc 使在需要将不同媒体协议转换为 WebRTC 流以实现低延迟和可扩展传输的环境中实现 WebRTC 变得更加容易。

## 先决条件

### 硬件要求

[TABLE COMPRESSED]
Columns: reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145 | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

## 下载并运行 go2rtc

### 更新系统

请使用以下命令运行。
```
sudo apt update  
sudo apt upgrade -y
```### 下载 go2rtc

请使用以下命令运行。
```
wget https://nightly.link/AlexxIT/go2rtc/workflows/build/master/go2rtc_linux_arm64.zip  
tar -xvzf go1.24.0.linux-arm64.tar.gz  
chmod +x go2rtc_linux_arm64
```### 创建 go2rtc.yaml

请使用以下命令运行。
```
nano go2rtc.yaml
```请使用您的实际 IP 地址填写以下配置。
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
```### 运行 go2rtc

请使用以下命令运行。
```
 ./go2rtc_linux_arm64
```在主机上打开端口 `1984`，然后点击 `Stream` 按钮。

## 结果

一旦我们配置好所有内容，就可以查看当前摄像头的实时画面。

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。
