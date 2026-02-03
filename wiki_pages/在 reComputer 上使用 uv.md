# 在 reComputer 上使用 uv

## 简介

本 wiki 解释了如何在 reComputer 设备上使用 [uv](https://github.com/astral-sh/uv)。uv 是一个快速、现代且轻量级的 Python 包管理器和解析器。它被设计为传统 Python 包管理工具（如 `pip` 和 `pip-tools`）的直接替代品，在速度、效率和可用性方面提供了显著改进。

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_speed.png)

## 准备硬件

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html) | | | | | | | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**立即购买 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

## 准备软件

### 更新系统

```
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"  
sudo apt update  
sudo apt full-upgrade
```

### 安装 uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 使用 uv

### 初始化项目

在这里，我们使用 `uv_test` 作为示例来演示 `uv` 的用法。

> **注意：** 请使用不同的项目名称，确保它与 PyPI 上的任何包都不同。

```
uv init uv_test --package  
cd uv_test
```

检查项目的结构

```
ls -la  
tree
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_tree.png)

### 创建 python 环境

在这里您可以创建一个 python 环境

```
uv venv   
source .venv/bin/activate
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_environment.png)

### 添加依赖项

使用 `numpy` 来构建功能：

```
uv add numpy
```

### 创建功能

使用 NumPy 在 `add.py` 上编写一个 `add` 函数作为示例：

add.py

```
import numpy as np  
  
def add(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:  
    """  
    Adds two NumPy arrays element-wise.  
  
    Parameters:  
    arr1 (np.ndarray): The first input array.  
    arr2 (np.ndarray): The second input array.  
  
    Returns:  
    np.ndarray: The element-wise sum of arr1 and arr2.  
  
    Raises:  
    ValueError: If the input arrays have different shapes and cannot be broadcasted.  
    """  
    # Ensure that both arrays have compatible shapes for element-wise addition  
    try:  
        result = np.add(arr1, arr2)  
    except ValueError:  
        raise ValueError("Input arrays have incompatible shapes for element-wise addition.")  
  
    return result  
  
if __name__ == "__main__":  
    # Example usage  
    arr1 = [1, 2, 3]  
    arr2 = [4, 5, 6]  
    print("Result of addition:", add(arr1, arr2))
```

结果如下：

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/pytest.png)

### 构建包

要将项目构建为可用的 `.whl` 文件，请按如下方式修改 `toml` 文件：

构建包：

```
uv build  
ls -a
```

结果如下：

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_build.png)

### 测试包

按如下方式安装包：

```
uv pip install dist/uv_test-0.1.0-py3-none-any.whl
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_install.png)

使用 `python` 脚本来测试包：

add.py

```
from uv_test.add import add  
  
if __name__ == "__main__":  
    arr1 = [1, 2, 3]  
    arr2 = [4, 5, 6]  
    print("Result of addition:", add(arr1, arr2))
```

### 将包推送到 PyPi

如果您没有 PyPI 账户，请注册一个[账户](https://pypi.org/account/register/)并创建[令牌](https://pypi.org/manage/account/token/)。

```
uv publish
```

结果如下所示，并输入您的令牌：

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_pubilsh.png)

## 结果

最后，您可以在 PyPI 上看到您上传的项目。

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_result.png)

## 技术支持与产品讨论

感谢您选择我们的产品！我们在这里为您提供不同的支持，以确保您使用我们产品的体验尽可能顺畅。我们提供多种沟通渠道，以满足不同的偏好和需求。