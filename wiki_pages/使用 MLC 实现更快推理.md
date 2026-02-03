# 在 Jetson 上使用 MLC LLM 量化 Llama2-7B

## 介绍

近年来，GPT-3 等大型语言模型彻底改变了自然语言处理任务。然而，这些模型大多在大规模数据集上训练，需要强大的计算资源，不适合在边缘设备上部署。为了解决这个问题，研究人员开发了量化技术，在不牺牲性能的情况下将大型模型压缩为更小的模型。

在这个项目中，我们介绍了 [Llama2-7B](https://huggingface.co/meta-llama/Llama-2-7b-hf) 的量化版本，这是一个在 1.5TB 数据上训练的大型语言模型，并将其部署在 Jetson Orin 上。我们还利用 [机器学习编译器大语言模型](https://llm.mlc.ai)(MLC LLM) 来加速模型的推理速度。通过在 [Jetson Orin NX](https://www.seeedstudio.com/reComputer-J4012-p-5586.html) 上部署量化的 Llama2-7B 和 MLC LLM，开发者可以构建强大的自然语言处理应用程序，在边缘设备上提供高精度和低延迟。

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/MLC_LLM.gif)

## 硬件组件

|  |  |  |
| --- | --- | --- |
| reComputer（或其他基于 Jetson 的设备）|  |  | | --- | --- | | | [**立即获取 🖱️**](https://www.seeedstudio.com/reComputer-J4012-p-5586.html) | | |

## 安装依赖

```
sudo apt-get update && sudo apt-get install git python3-pip
```

```
git clone --depth=1 https://github.com/dusty-nv/jetson-containers
```

```
cd jetson-containers pip3 install -r requirements.txt
```

```
cd ./data && git clone https://github.com/LJ-Hao/MLC-LLM-on-Jetson-Nano.git && cd ..
```

## 安装并运行容器

### 第一步：安装镜像

```
./run.sh --env HUGGINGFACE_TOKEN=<YOUR-ACCESS-TOKEN> $(./autotag mlc) /bin/bash -c 'ln -s $(huggingface-downloader meta-llama/Llama-2-7b-chat-hf) /data/models/mlc/dist/models/Llama-2-7b-chat-hf'
```

使用 `sudo docker images` 检查镜像是否已安装

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/docker_image.png)

### 第二步：安装 Llama2-7b-chat-hf 并使用 MLC 量化模型

```
./run.sh $(./autotag mlc) \  
python3 -m mlc_llm.build \  
--model Llama-2-7b-chat-hf \  
--quantization q4f16_ft \  
--artifact-path /data/models/mlc/dist \  
--max-seq-len 4096 \  
--target cuda \  
--use-cuda-graph \  
--use-flash-attn-mqa
```

### 第三步：运行并进入 docker

```
./run.sh <YOUR IMAGE NAME>   
#对我来说是 dustynv/mlc:51fb0f4-builder-r35.4.1，请检查第一步的结果
```

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/docker_run.png)

## 让我们运行它

### 运行未经 MLC LLM 量化的 Llama

```
cd /data/MLC-LLM-on-Jetson && python3 Llama-2-7b-chat-hf.py
```

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Llama-2-7b-chat-hf.png)

你可以看到，在没有使用 MLC 量化的情况下，Jetson Nano 16GB 可以加载模型但无法运行。

### 运行经过 MLC LLM 量化的 Llama

```
cd /data/MLC-LLM-on-Jetson && python3 Llama-2-7b-chat-hf-q4f16_ft.py
```

结果如下：

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Llama-2-7b-chat-hf-q4f16_ft.png)

## 在 Jetson Orin NX 16GB 上使用 MLC 运行 Llama 的视频

## 项目展望

在这个项目中，我们演示了如何在 Jetson Orin 上部署量化版本的 Llama2-7B 和 MLC LLM。凭借 Jetson Orin 强大的计算能力，开发者可以构建在边缘设备上提供高精度和低延迟的自然语言处理应用程序。未来，我们将继续探索在边缘设备上部署大型语言模型的潜力，并开发更高效和优化的部署方法。