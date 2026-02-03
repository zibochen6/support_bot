# 在 reComputer J30 上开始使用 NEQTO Engine for Linux

## 介绍

NEQTO 是一个轻量级且安全的软件包，允许公司远程安装和配置其在边缘设备上的软件。NEQTO 通过即插即用的平台连接器和内置的软件生命周期管理，使公司能够为最终用户提供改进的软件服务。

安装了 NEQTO 的设备可以通过 API 或即用型 NEQTO Console 进行管理，其中包括数据存储、警报和看门狗监控的可选服务。企业可以通过在任何 Linux 设备上的近乎即时安装和与任何本地或云服务器的无缝数据集成来启用 AIoT。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/header-img_2x.png)

## 先决条件

### 支持的硬件

您可以选择其中任何一种：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer J3011 - NVIDIA Jetson Orin™ Nano 8GB reComputer J4011 - NVIDIA Jetson Orin™ NX 8GB|  |  |  |  | | --- | --- | --- | --- | | | [**立即获取 🖱️**](https://www.seeedstudio.com/reComputer-J3011-p-5590.html)  [**立即获取 🖱️**](https://www.seeedstudio.com/reComputer-J4011-p-5585.html) | | | | | |

* (任何 Linux 机器)

tip

* 支持的架构：armv6l(32位)、armv7l(32位)、aarch64(64位)、x86\_64(64位)
* 所需磁盘空间：≥ 32 MB
* 所需内存空间：≥ 4MB（默认设置下）
* 网络通信接口：必须配备物理网络适配器。
* 显示器、键盘、鼠标（可选）

## 入门指南

### 注册 NEQTO 账户：

* 步骤 1. 访问[官方页面](https://console.neqto.com/register)注册 NEQTO 账户
* 步骤 2. 输入您的电子邮件地址，创建密码，然后继续
* 步骤 3. 从您收到的激活邮件中验证账户

### 安装 NEQTO Linux

1. 在 NEQTO 控制台中从

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65eee22eccae06004c6d9459.png)

选择 `Manage API Keys for Linux-based Device`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65effd1accae06004c6d94a0.png)

2. 点击 `CREATE API KEY`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65efff89ccae06004c6d94a6.png)

然后将显示 API 密钥

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65efff33ccae06004c6d94a5.png)

3. 使用 curl 或 wget 下载 `NEQTO Engine Linux Installer`。

   这次使用 wget 命令。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65eeeaa3ccae06004c6d945d.png)

复制 `Installer of NEQTO Engine for Linux` 的 `Download link` 并将其粘贴到 "wget␣" 之后。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f00259ccae06004c6d94a8.png)

安装程序下载成功

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f002fbccae06004c6d94aa.png)

4. 在运行 NEQTO Engine for Linux 安装之前，使用 chmod 命令更改下载的安装程序（`neqto-daemon-install.latest.sh`）的执行权限。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f00369ccae06004c6d94ab.png)

5. 从 NEQTO 控制台的 `API Keys for NEQTO Engine for Linux` 中复制 `API Key`，并将其粘贴到 `sudo . /neqto-daemon-install.sh␣-k␣` 之后。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f00476ccae06004c6d94ae.png)

6. 输入密码

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f00529ccae06004c6d94af.png)

7. 执行后，将显示重要说明。请检查并在同意的情况下输入 "agree"。之后，将执行设备注册，软件安装将继续。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f005c1ccae06004c6d94b1.png)

8. 请等待直到显示最终状态 `Installation completed successfully!`。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f00657ccae06004c6d94b3.png)

确认设备已在 NEQTO 控制台上注册

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f00722ccae06004c6d94b5.png)

### Hello World

1. 在 `GROUPS` 下点击 `ADD GROUP`。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65eef7b9ccae06004c6d947b.png)

2. 在 `Name` 中输入 `reComputer J30` 并点击 `SAVE`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65eef7d6ccae06004c6d947c.png)

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f007ddccae06004c6d94b6.png)

3. 选择您创建的 `reComputer J30` 并点击 `SCRIPTS`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f0392accae06004c6d9518.png)

4. 点击 `ADD SCRIPT`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f0379fccae06004c6d9512.png)

5. 在 `Name` 字段中输入 `Hello World` 并点击 `SAVE`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f03861ccae06004c6d9515.png)

6. 从 `入门指南` 中复制并粘贴[示例代码](https://docs.neqto.com/docs/en/getting-started/tutorial-step1#sample-code)到 NEQTO 控制台脚本编辑器中，然后点击 `保存`。

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f036f4ccae06004c6d950f.png)

7. 点击 `模板`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f035d5ccae06004c6d950d.png)

然后点击 `添加模板`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f03451ccae06004c6d950a.png)

8. 按如下设置 `设备信息`

   * 在 `名称` 字段中输入 `reComputer J30 Template`
   * 在 `固件类型` 字段中选择 `Linux-based device`
   * 在 `固件版本` 字段中选择最新版本

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f03337ccae06004c6d9505.png)

9. 在 `选项` 中，在 `脚本` 字段中选择 `Hello World`，然后点击 `保存`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f03261ccae06004c6d9501.png)

10. 点击 `节点`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f0313accae06004c6d94fe.png)

然后点击 `添加节点`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f03019ccae06004c6d94fb.png)

11. 按如下设置 `元数据`

    * 将 `名称` 字段设置为 `reComputer J30`
    * 将 `模板` 字段设置为 `reComputer J30 Template`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f02f56ccae06004c6d94f8.png)

12. 在 `设备信息` 中选择您刚刚注册的设备，然后点击 `保存`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f02e10ccae06004c6d94f5.png)

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f02d0dccae06004c6d94f2.png)

13. 在 reComputer J30 的终端中输入 `tail -F /tmp/neqto/log/neqto.log`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f00ac6ccae06004c6d94c8.png)

14. 在 NEQTO 控制台上运行 `重新加载脚本` 后，您可以在 reComputer J30 的终端中看到 `Hello World!!!`

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f02b89ccae06004c6d94ef.png)

![pir](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/neqto_engine_for_linux_recomputer/65f00bf7ccae06004c6d94cd.png)

## 更多信息 / 故障排除

* [NEQTO 支持](https://support.neqto.com/hc/en-us)
* [支持指南](https://docs.neqto.com/docs/en/neqto/support-guidelines)

## 资源

* [NEQTO 资源中心](https://docs.neqto.com/docs/en/linux/software/requirements)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。