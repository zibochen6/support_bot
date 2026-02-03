# reComputer 上的 iSpy

## 简介

[iSpy](https://www.ispyconnect.com/) 是一个开源视频监控应用程序，专为消费级网络摄像头和 IP 摄像头而设计。它最初于 2007 年推出，现已发展成为一个功能齐全的监控解决方案。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/ispy_1.png)

## 先决条件

### 硬件要求

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html) | | | | | | | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

## 下载 iSpy

### 更新系统

请使用以下命令运行。

```
sudo apt update  
sudo apt upgrade -y
```

### 下载 docker 和 docker compose

请使用以下命令安装 docker。

```
wget https://get.docker.com -O get-docker.sh  
chmod +x   
sudo sh get-docker.sh  
sudo systemctl start docker  
sudo systemctl enable docker  
docker --version
```

结果如下所示：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/moonfire/docker_install.png)

请使用以下命令安装 docker compose。

```
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r .tag_name)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose  
sudo chmod +x /usr/local/bin/docker-compose  
docker-compose --version
```

结果如下所示：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/moonfire/docker_compose_version.png)

### 创建 `docker-compose.yaml`

请使用以下命令创建 `docker-compose.yaml`。

```
cd ~ && nano docker-compose.yaml
```

然后将以下内容输入到 `YAML` 文件中。

```
services:  
  agentdvr:  
    image: mekayelanik/ispyagentdvr:latest  
    container_name: AgentDVR  
    restart: unless-stopped  
    environment:  
      - PUID=1000  
      - PGID=1000  
      - TZ=America/New_York  
      - AGENTDVR_WEBUI_PORT=8090  
    ports:  
      - "8090:8090"  
      - "3478:3478/udp"  
      - "50000-50100:50000-50100/udp"  
    volumes:  
      - /appdata/AgentDVR/config/:/AgentDVR/Media/XML/  
      - /appdata/AgentDVR/media/:/AgentDVR/Media/WebServerRoot/Media/  
      - /appdata/AgentDVR/commands:/AgentDVR/Commands/
```

请使用以下命令创建必要的文件夹。

```
sudo mkdir -p /appdata/AgentDVR/config /appdata/AgentDVR/media /appdata/AgentDVR/commands
```

## 配置 iSpy

### 运行 docker compose

请使用以下命令初始化数据库。

```
sudo docker compose up -d
```

结果如下所示。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/ispy_docker.png)

### 配置

打开 `localhost:8090` 端口：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/ispy_windows.png)

按照以下步骤添加摄像头：

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/config_1.png)

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/config_2.png)

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/config_3.png)

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/config_4.png)

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/config_5.png)

## 结果

一旦我们配置好所有内容，就可以查看当前摄像头的实时画面。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/ispy/result.gif)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。