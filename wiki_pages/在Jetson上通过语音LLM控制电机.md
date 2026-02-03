# 在Jetson上通过语音LLM控制电机

## 介绍

本wiki基于Jetson平台（reComputer Robotics J4012）构建了一个端到端的语音控制电机系统，集成了语音识别、边缘大语言模型（LLM）意图理解和硬件控制，实现自然的人机交互——用户可以通过简单的语音命令（例如"顺时针旋转90度"）来控制MyActuator X系列电机。

## 前提条件

* reComputer Robotics J4012
* reSpeaker XVF3800
* MyActuator X系列电机

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer Robotics J4012 reSpeaker XVF3800 MyActuator X系列电机|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**立即获取 🖱️**](https://www.seeedstudio.com/reComputer-Robotics-J4012-p-6505.html)  [**立即获取 🖱️**](https://www.seeedstudio.com/ReSpeaker-XVF3800-4-Mic-Array-With-XIAO-ESP32S3-p-6489.html)  [**立即获取 🖱️**](https://www.seeedstudio.com/Myactuator-X4-P36-Planetary-Actuator-p-6469.html) | | | | | | | | |

## 硬件连接

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_control/hardware_connect.jfif)

## 开始使用

整个系统的工作流程包括三个步骤：

1. ASR：麦克风捕获用户的音频命令，并使用 Whisper 将其转换为文本。
2. 函数调用：大语言模型根据用户的输入指令生成满足要求的电机控制参数。
3. 电机控制：调用相应的控制程序驱动电机旋转到指定位置。

接下来，我们将详细解释每个步骤的实现。

### 安装 Whisper 服务器

首先，我们需要安装 Whisper 服务以启用 ASR 功能。请在 Jetson 设备上打开终端窗口并运行以下命令。

```
git clone https://github.com/jjjadand/whisper-stable4curl  
cd whisper-stable4curl  
export PATH=/usr/local/cuda-12.6/bin${PATH:+:${PATH}}  
export LD_LIBRARY_PATH=/usr/local/cuda-12.6/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}  
cmake --build build -j --config Release
```

如果一切顺利，您将在终端窗口中看到以下日志。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_control/whisper.png)

然后我们启动 Whisper 推理服务：

```
./build/bin/whisper-stream -m ./models/ggml-base.en-q5_1.bin -t 8 --step 0 --length 7000 -vth 0.7 --keep 1200
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_control/launch_whisper.png)

### 安装 Ollama

Ollama 是一个极其用户友好的边缘计算 LLM 推理框架，只需一条命令即可在 Jetson 上部署。在您的 Jetson 设备上打开一个新的终端窗口并执行：

```
curl -fsSL https://ollama.com/install.sh | sh  
ollama pull qwen2.5
```

info

这里，我们使用 Qwen 2.5 大语言模型来理解用户的意图。

### 安装电机控制脚本

执行以下命令来启动电机控制脚本：

```
git clone https://github.com/yuyoujiang/voice_control.git  
cd voice_control  
sudo ip link set can0 type can bitrate 1000000  
sudo ip link set can0 up  
python app.py
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_control/motor_control.png)

## 效果演示

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。