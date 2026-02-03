# Use uv on reComputer

## Introduction

This wiki explains how to use the [uv](https://github.com/astral-sh/uv) on reComputer box. uv is a fast, modern, and lightweight package manager and resolver for Python. It is designed to be a drop-in replacement for traditional Python package management tools like `pip` and `pip-tools`, offering significant improvements in speed, efficiency, and usability.

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_speed.png)

## Prepare Hardware

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reComputer R1125 reComputer AI R2130 reComputer AI Industrial R2145|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-R1125-10-p-6256.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-R2130-12-p-6368.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-AI-Industrial-R2145-12-p-6486.html) | | | | | | | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer Industrial R20xx reComputer Industrial R21xx|  |  |  |  | | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2035-12-p-6542.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-Industrial-R2135-12-p-6547.html) | | | | | |

## Prepare software

### update the system

```
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"  
sudo apt update  
sudo apt full-upgrade
```

### Install uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Use uv

### Init the project

Here, we use `uv_test` as an example to demonstrate the usage of `uv`.

> **Note:** Please make different project name make sure it is different from any package on PyPI.

```
uv init uv_test --package  
cd uv_test
```

Check the structure of the project

```
ls -la  
tree
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_tree.png)

### Creat a python environment

Here you can creat a python environmet

```
uv venv   
source .venv/bin/activate
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_environment.png)

### Add dependencies

Use `numpy` to build funcation:

```
uv add numpy
```

### Creat funcation

Use NumPy to write an `add` function on `add.py` as an example:

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

The results are as follows:

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/pytest.png)

### Build the package

To build the project into a usable `.whl` file, modify the `toml` file as follow:

Build the package:

```
uv build  
ls -a
```

The results are as follows：

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_build.png)

### Test the package

Install the package as below:

```
uv pip install dist/uv_test-0.1.0-py3-none-any.whl
```

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_install.png)

Use `python` script to test the packag:

add.py

```
from uv_test.add import add  
  
if __name__ == "__main__":  
    arr1 = [1, 2, 3]  
    arr2 = [4, 5, 6]  
    print("Result of addition:", add(arr1, arr2))
```

### Push the package to PyPi

If you don't have a PyPI account, please register an [account](https://pypi.org/account/register/) and get creat [token](https://pypi.org/manage/account/token/).

```
uv publish
```

The result is like as below, and input your token:

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_pubilsh.png)

## Result

Finally, you can see your uploaded project on PyPI.

![](https://files.seeedstudio.com/wiki/00_AI_Sensing/Application/uv/uv_result.png)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.