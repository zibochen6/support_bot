# Use Zoneminder on reComputer

## Introduction

[Zoneminder](https://github.com/ZoneMinder/zoneminder) is an open-source video surveillance software that allows you to monitor and manage security cameras. It supports various types of cameras, including IP cameras, USB webcams, and analog cameras. ZoneMinder offers features like motion detection, video recording, alarm notifications, and remote viewing through a web interface. It's highly customizable, making it suitable for both personal and professional surveillance needs. Plus, being open-source, it’s free to use and can be adapted to different setups.

## Prerequisites

### Hardware Requirements

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html) | | | | | | | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

## Download Zoneminder

### Update system

Run the following commands.

```
sudo apt update  
sudo apt upgrade -y
```

### Install MariaDB and do initial database configuration

Run the following commands.

```
sudo apt install apache2 mariadb-server
```

Switch into root user and create database and database user.

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

By default MariaDB uses [unix socket authentication](https://mariadb.com/kb/en/authentication-plugin-unix-socket/), so no root user password is required (root MariaDB user access only available to local root Linux user). If you wish, you can set a root MariaDB password (and apply other security tweaks) by running [mariadb-secure-installation](https://mariadb.com/kb/en/mysql_secure_installation/).

### Install Zoneminder

By default Debian will install the version published in Debian (stable). However there may be newer versions by using backports. At the time of this writing, bookworm (stable) ships with v.1.36.33.

To install the version in bookworm stable, just run the following command.

```
sudo apt install zoneminder
```

If instead you prefer to install the newer version using backports, run the following commands. The first line will add this bookworm-backports repository. The backports repository is deactivated by default, so with the second line we explicitly state we want the backported version of zoneminder.

```
sudo bash -c "echo 'deb http://deb.debian.org/debian bookworm-backports main contrib' >> /etc/apt/sources.list"  
sudo apt update  
sudo apt -t bookworm-backports install zoneminder
```

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/zoneminder/zm_2.png)

## Configure Zoneminder

### Configure database

Run the following commands, Use `zmpass` as password.

```
mariadb -u zmuser -p zm < /usr/share/zoneminder/db/zm_create.sql
```

### Setup permissions for zm.conf

To make sure zoneminder can read the configuration file, run the following command.

```
sudo chgrp -c www-data /etc/zm/zm.conf
```

### Tweak Apache configuration

```
sudo a2enconf zoneminder  
sudo a2enmod cgi  
sudo systemctl reload apache2.service  
sudo systemctl restart zoneminder.service  
sudo systemctl status zoneminder.service  
sudo systemctl enable zoneminder.service
```

If the zoneminder.service show to be active and without any errors, you should be able to access zoneminder at `http://yourhostname/zm`

### Configure Zoneminder

Add the video source to the zoneminder.

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/zoneminder/zm_3.png)

## Result

Once we have configured everything, we can view the live feed from the current camera, and when motion is detected, it will be recorded.

![pir](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/zoneminder/zone_m.gif)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.