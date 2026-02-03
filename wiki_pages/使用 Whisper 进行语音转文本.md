# 在 NVIDIA Jetson Orin 上部署 Whisper 实现实时语音转文本

## 介绍

实时语音转文本（STT）系统在现代应用中发挥着重要作用，从语音助手到转录服务。以下是一些流行的 STT 模型：Whisper、Riva、DeepSpeech、Google Cloud Speech-to-Text API、Microsoft Azure Speech Service、IBM Watson Speech to Text、Kaldi、Wit.ai 等等。NVIDIA Jetson Orin 以其高性能和能效著称，为在边缘部署此类要求苛刻的应用提供了一个有前景的平台。

[Whisper](https://github.com/openai/whisper) 是一个利用深度学习的先进 STT 系统，在准确性和效率方面表现出色。[Riva](https://github.com/nvidia-riva) 是 NVIDIA 开发的综合性多模态对话式 AI 框架。通过在 Jetson Orin 上部署 Whisper 或 Riva，开发者可以利用其强大的 GPU 和 CPU 核心，以及 Tensor Cores 等硬件加速技术，实现低延迟的实时 STT。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Real-Time-Whisper.gif)

在本教程中，我们向您介绍 [Jetson 上的实时 Whisper](https://github.com/LJ-Hao/Deploy-Whisper-on-NVIDIA-Jetson-Orin-for-Real-time-Speech-to-Text.git)，这种集成使得语音处理可以直接在设备上进行，无需持续的网络连接，并增强了隐私和安全性。此外，我们还将比较 Whisper 和 Riva 在同一 Jetson Orin 设备上部署时的推理速度。最终，在 Jetson Orin 上部署 Whisper 使开发者能够构建强大、高效的 STT 应用，在从智能家居到工业自动化的各个领域提供高准确性和低延迟。

## 硬件设置

### 硬件组件

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer（或其他基于 Jetson 的设备） reSpeaker（或其他 USB 接口麦克风）|  |  |  |  | | --- | --- | --- | --- | | | [**立即获取 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-J3011-p-5682.html?queryID=c1e6f0b0bd38a98233ce64bce8083a22&objectID=5682&indexName=bazaar_retailer_products)  [**立即获取 🖱️**](https://www.seeedstudio.com/ReSpeaker-Mic-Array-v2-0.html?queryID=2baffb980bdb6d5e65b2b3f511657cb2&objectID=139&indexName=bazaar_retailer_products) | | | | | |

### 硬件连接

![pir](https://github.com/Seeed-Projects/Real-time-Subtitle-Recorder-on-Jetson/raw/main/sources/recorder_hardware_connection.png)

## 准备运行环境

#### 步骤1. 安装依赖项：

```
git clone https://github.com/LJ-Hao/Deploy-Whisper-on-NVIDIA-Jetson-Orin-for-Real-time-Speech-to-Text.git  
cd Deploy-Whisper-on-NVIDIA-Jetson-Orin-for-Real-time-Speech-to-Text  
pip install -r requirements.txt  
sudo apt update && sudo apt install ffmpeg  
arecord -D hw:2,0 --dump-hw-params #set microphone rate to 16000
```

#### 步骤 2. 测试环境

```
python test.py
```

如果您在终端中看到以下信息打印出来，这意味着您已经成功安装了必要的库。

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Deploy-whisper-on-Nvidia-Jetson-orin-for-real-time-speech-to-text-test.png)

在您的终端中（Ctrl+Alt+T），输入 `ffmpeg -version`，如果您得到类似以下的内容，这意味着您已经安装了 ffmpeg。

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Whisper-ffmpeg.png)

## 让我们运行它

```
python main.py
```

## Riva 与 Whisper 对比

Riva 以其先进的 AI 驱动语音识别和自然语言处理而闻名，为用户提供实时转录、翻译和口语对话分析功能。

Whisper 是一个自动语音识别（ASR）系统，在从网络收集的 680,000 小时多语言和多任务监督数据上进行训练。此外，它支持多种语言的转录，以及从这些语言翻译成英语。

在即将到来的对比视频中，我们将比较在 Nvidia Jetson 上开发的 [Riva](https://wiki.seeedstudio.com/cn/Real%20Time%20Subtitle%20Recoder%20on%20Nvidia%20Jetson/) 和 Whisper 在语音转文本方面的能力。

## 项目展望

在这个项目中，我们使用 Whisper 实时捕获麦克风输入的数据并在网页上显示。未来，我们将增强 Whisper 的实时处理能力，进一步减少延迟并提高语音识别的准确性，并探索与其他 AI 服务或 API 的集成，以增强应用程序的功能。