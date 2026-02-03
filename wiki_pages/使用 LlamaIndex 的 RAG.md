# 基于 Jetson 和 LlamaIndex 的本地 RAG

## 介绍

如今，越来越多的人开始使用大型语言模型来解决日常问题。然而，大型语言模型在回答某些问题时可能会出现幻觉，向用户提供错误信息。不过，[RAG 技术](https://www.seeedstudio.com/blog/2024/04/25/build-a-local-rag-chatbot-on-jetson-orin-for-your-knowledge-base/)可以通过向大型语言模型提供相关数据来减少幻觉的发生。因此，使用 RAG 技术来减少大型语言模型中幻觉的产生已成为一种趋势。

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/RAG-MLC-Jetson.gif)

在这里我们向您介绍[基于 Jetson 的 RAG](https://github.com/Seeed-Projects/RAG_based_on_Jetson)，它使用 [LlamaIndex](https://www.llamaindex.ai) 作为 RAG 框架，[ChromaDB](https://github.com/chroma-core/chroma) 作为向量数据库，以及量化的 Llama2-7b 模型 [LLM MLC](https://llm.mlc.ai/) 作为问答模型。通过这个本地 RAG 项目，它可以保护您的数据隐私并为您提供低延迟的通信体验。

## 硬件组件

|  |  |  |
| --- | --- | --- |
| reComputer（基于 RAM >= 16GB 的 Jetson）|  |  | | --- | --- | | | [**立即获取 🖱️**](https://www.seeedstudio.com/reComputer-J4012-p-5586.html) | | |

## 准备运行环境

### 步骤 1：安装 MLC Jetson 容器

```
# 安装 jetson-container 及其依赖项  
git clone --depth=1 https://github.com/dusty-nv/jetson-containers  
cd jetson-containers   
pip install -r requirements.txt
```

### 步骤 2：安装项目

```
# 安装 RAG 项目  
cd data  
git clone https://github.com/Seeed-Projects/RAG_based_on_Jetson.git
```

### 步骤 3：安装由 MLC LLM 量化的 Llama2-7b 模型

```
# 安装 LLM 模型  
sudo apt-get install git-lfs  
cd RAG_based_on_Jetson  
git clone https://huggingface.co/JiahaoLi/llama2-7b-MLC-q4f16-jetson-containers
```

### 步骤 4：运行 docker 并安装依赖项

```
cd ../../  
./run.sh $(./autotag mlc)  
 # 这里您将进入 Docker，下面的命令将在 Docker 内运行  
cd data/RAG_based_on_Jetson/  
pip install -r requirements.txt  
pip install chromadb==0.3.29
```

运行 `pip install chromadb==0.3.29` 后，您将看到如下所示的界面。

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/RAG_Install_ChromaDB.png)

note

忽略错误是没有问题的。

## 让我们运行它

```
# 在 docker 中运行  
python3 RAG.py
```

## 项目展望

在这个项目中，TXT 和 PDF 文档被解析为向量数据库，并使用 RAG 技术来减少模型对特定问题的幻觉。未来，我们将使用多模态模型来支持图像和视频的检索。