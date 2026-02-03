# 在 reComputer Mini 上为 Reachy Mini 部署本地语音 LLM！

双重 Mini！本项目将构建一个完全本地化、低延迟、高隐私的语音交互机器人助手系统。以 reComputer Mini J501 边缘计算设备为核心，部署本地语音识别、大语言模型和语音合成服务。使用开源机器人平台 Reachy Mini 作为人机交互的物理终端，实现具有感知、对话和行动能力的具身智能交互体验。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reachy_mini/workflow.png)

## 前提条件

* reComputer Mini J501 套件
* Reachy Mini Lite

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Mini J501 套件 Reachy Mini Lite|  |  |  |  | | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Robotics-J4012-p-6505.html)  [**立即购买 🖱️**](https://www.pollen-robotics.com/reachy-mini/#order) | | | | | |

info

请确保您的 Jetson 设备包含[载板](https://www.seeedstudio.com/reComputer-Robotics-J4012-p-6505.html)、Jetson 模块和[散热系统](https://www.seeedstudio.com/reComputer-Mini-J501-heatsink-with-fan-p-6605.html)，并且已安装 JP6.2 操作系统。

info

在配置软件之前，请将 Reachy Mini 连接到 reComputer Mini J501 的 Type-A 端口。

## 部署软件应用程序

**步骤 1.** 在 reComputer Jetson 中安装并运行 ollama 推理服务器。

在 reComputer Jetson 的终端窗口（`Ctrl + Alt + T`）中运行以下命令。

```
# Install Ollama (visit https://ollama.ai for platform-specific instructions)  
curl -fsSL https://ollama.com/install.sh | sh  
  
# Pull the required model  
ollama pull llama3.2-vision:11b
```

note

模型下载大约需要 10 分钟。请耐心等待。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reachy_mini/ollama.png)

**步骤 2.** 安装对话应用程序。

在 reComputer Jetson 的终端窗口中运行以下命令。

note

如果您想在 conda 虚拟环境中配置运行时环境，请在执行以下安装命令之前使用 `conda activate <name>` 命令激活目标环境。

```
cd Downloads  
git clone https://github.com/Seeed-Projects/reachy-mini-loacl-conversation.git  
cd reachy-mini-loacl-conversation  
pip install -r requirements.txt -i https://pypi.jetson-ai-lab.io/  
pip install "reachy-mini"
```

info

更多安装信息请参考[这里](https://github.com/Seeed-Projects/reachy-mini-loacl-conversation/tree/master)。

**步骤 3.** 启动应用程序。

在 reComputer Jetson 的终端窗口中运行以下命令来启动 reachy mini 守护进程。

```
reachy-mini-daemon
```

打开另一个终端并执行：

```
# Set environment variables  
export OLLAMA_HOST="http://localhost:11434"  
export OLLAMA_MODEL="qwen2.5:7b"  
export COQUI_MODEL_NAME="tts_models/zh-CN/baker/tacotron2-DDC-GST"  
export DEFAULT_VOLUME="1.5"  
  
# Start the voice assistant  
python main.py
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/reachy_mini/launch_app.png)

info

这里使用中文模型进行演示。您可以根据需要替换为其他语言的模型。

## 效果演示

程序正常启动后，我们可以使用键盘上的 `R` 键和 `S` 键来控制开始和停止录音。录音停止后，程序将调用本地大语言模型生成响应。

## 参考资料

* <https://ollama.com/download/linux>
* <https://github.com/modelscope/FunASR>
* <https://github.com/coqui-ai/TTS>
* <https://github.com/Seeed-Projects/reachy-mini-loacl-conversation/>

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。