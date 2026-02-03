# reComputer 与 VEYE 摄像头兼容性问题的解决方案

该问题已追溯到 USB 集线器芯片的固件问题。

具体步骤如下：

**步骤 1.** 使用 SSH 远程登录到您的 Jetson 设备，因为在升级过程中，要求不能有外部设备连接到 USB 接口。

**步骤 2.** 找到一种方法将[摄像头驱动程序](https://files.seeedstudio.com/wiki/reComputer/Hard_ware/VEYE_Camera/vl822-fw.tar.bz2)复制到 Jetson 系统中。如果使用 USB 驱动器进行复制，请记住在复制完成后拔出 USB 驱动器。

**步骤 3.** 按照以下说明执行升级。

```
$ tar -xjvf vl822-fw.tar.bz2  
$ cd vl822-fw
```

然后，请按照 `readme.md` 文件安装固件。

**步骤 4.** 关机并等待 5 秒钟后再开机。然后，执行以下命令确认 USB 集线器固件的版本。

```
$ ./run_2822_ver.sh
```

**步骤 5.** 恭喜，升级已成功。您现在应该能够使用 i2cdetect 在 0x3b 地址检测到 VEYE 摄像头。

## 技术支持

请随时将问题提交到我们的[论坛](https://forum.seeedstudio.com/)。

[![](https://files.seeedstudio.com/wiki/Wiki_Banner/new_product.jpg)](https://www.seeedstudio.com/act-4.html?utm_source=wiki&utm_medium=wikibanner&utm_campaign=newproducts)