# 在 reComputer 上使用 Zoneminder

## 简介

[Zoneminder](https://github.com/ZoneMinder/zoneminder) 是一个开源视频监控软件，允许您监控和管理安全摄像头。它支持各种类型的摄像头，包括 IP 摄像头、USB 网络摄像头和模拟摄像头。ZoneMinder 提供运动检测、视频录制、报警通知和通过 Web 界面远程查看等功能。它高度可定制，适用于个人和专业监控需求。此外，作为开源软件，它免费使用，可以适应不同的设置。

## 先决条件

### 硬件要求

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html) | | | | | | | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

## 下载 Zoneminder

### 更新系统

运行以下命令。

```
sudo apt update  
sudo apt upgrade -y
```

### 安装 MariaDB 并进行初始数据库配置

运行以下命令。

```
sudo apt install apache2 mariadb-server
```

切换到 root 用户并创建数据库和数据库用户。

```
sudo su  
mariadb  
CREATE DATABASE zm;  
CREATE USER zmuser@localhost IDENTIFIED BY 'zmpass';  
GRANT ALL ON zm.* TO zmuser@localhost;  
FLUSH PRIVILEGES;  
exit;  
exit
```

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/zoneminder/zm_1.png)

默认情况下，MariaDB 使用 [unix socket authentication](https://mariadb.com/kb/en/authentication-plugin-unix-socket/)，因此不需要 root 用户密码（root MariaDB 用户访问仅对本地 root Linux 用户可用）。如果您愿意，可以通过运行 [mariadb-secure-installation](https://mariadb.com/kb/en/mysql_secure_installation/) 来设置 root MariaDB 密码（并应用其他安全调整）。

### 安装 Zoneminder

默认情况下，Debian 将安装在 Debian（稳定版）中发布的版本。但是，通过使用 backports 可能有更新的版本。在撰写本文时，bookworm（稳定版）附带 v.1.36.33。

要安装 bookworm 稳定版中的版本，只需运行以下命令。

```
sudo apt install zoneminder
```

如果您更愿意使用 backports 安装更新版本，请运行以下命令。第一行将添加此 bookworm-backports 存储库。backports 存储库默认情况下是停用的，因此在第二行中我们明确声明我们想要 zoneminder 的 backported 版本。

```
sudo bash -c "echo 'deb http://deb.debian.org/debian bookworm-backports main contrib' >> /etc/apt/sources.list"  
sudo apt update  
sudo apt -t bookworm-backports install zoneminder
```

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/zoneminder/zm_2.png)

## 配置 Zoneminder

### 配置数据库

运行以下命令，使用 `zmpass` 作为密码。

```
mariadb -u zmuser -p zm < /usr/share/zoneminder/db/zm_create.sql
```

### 设置 zm.conf 的权限

为确保 zoneminder 可以读取配置文件，请运行以下命令。

```
sudo chgrp -c www-data /etc/zm/zm.conf
```

### 调整 Apache 配置

```
sudo a2enconf zoneminder  
sudo a2enmod cgi  
sudo systemctl reload apache2.service  
sudo systemctl restart zoneminder.service  
sudo systemctl status zoneminder.service  
sudo systemctl enable zoneminder.service
```

如果 zoneminder.service 显示为活动状态且没有任何错误，您应该能够在 `http://yourhostname/zm` 访问 zoneminder

### 配置 Zoneminder

将视频源添加到 zoneminder。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/zoneminder/zm_3.png)

## 结果

一旦我们配置了所有内容，我们就可以查看当前摄像头的实时画面，当检测到运动时，它将被录制。

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/zoneminder/zone_m.gif)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。