# 在 A603 Jetson 载板上使用 IMX477 摄像头

## Jetpack 5.1.2

如果您需要使用 IMX477 摄像头，请下载[此驱动程序包](https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/ERJdh3pvdYZOqJWugsnMJKEBMkGXtU8ngY03kJeLDWSkLw?e=TuLWmL)并按照[此教程](https://wiki.seeedstudio.com/cn/reComputer_A603_Flash_System/)重新刷写 Jetpack 系统。

caution

请注意，您需要使用适用于  [**JP5.1.2**](https://developer.nvidia.com/embedded/jetson-linux-r3541)  的 BSP。

## Jetpack 6.0

如果您需要使用 IMX477 摄像头，请下载[此驱动程序包](https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/ETIsoZ25I69KsSiA6TweK4UBVfo7gBrvPyKX9pJ68J8oIA?e=a9uumE)并按照[此教程](https://wiki.seeedstudio.com/cn/reComputer_A603_Flash_System/)重新刷写 Jetpack 系统。

caution

请注意，您需要使用适用于  [**JP6.0**](https://developer.nvidia.com/embedded/jetson-linux-r363)  的 BSP。

系统刷写完成后，连接 CSI 摄像头并使用以下命令启动摄像头：

```
nvgstcapture-1.0 --sensor-id=0
```

![](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/camera.png)

## Jetpack 6.2

如果您需要使用 IMX477 摄像头，请下载[此驱动程序包](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQC58VP43oyWQY48K__qIXBsAfz5meLpWtldH6SML_BgvCE?e=dXXvuK)并按照[此教程](https://wiki.seeedstudio.com/cn/reComputer_A603_Flash_System/)重新刷写 Jetpack 系统。

caution

请注意，您需要使用适用于  [**JP6.2**](https://developer.nvidia.com/embedded/jetson-linux-r3643)  的 BSP。

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。