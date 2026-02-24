# Getting started of NEQTO Engine for Linux on reComputer J30

## Introduction

NEQTO is a lightweight and secure software package allowing companies to remotely install and configure their software on edge devices. NEQTO enables companies to provide improved software services to end users through turnkey platform connectors and built-in software lifecycle management.

Devices installed with NEQTO can be managed through API or the ready-to-use NEQTO Console, which includes optional services for data storage, alerts, and watchdog monitoring. Businesses can enable AIoT with near-instant installation on any Linux device and seamless data integration with any on-premise or cloud servers.

## Prerequisites

### Hardware supported

You can choose either one:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| reComputer J3011 - NVIDIA Jetson Orin™ Nano 8GB reComputer J4011 - NVIDIA Jetson Orin™ NX 8GB|  |  |  |  | | --- | --- | --- | --- | | | [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-J3011-p-5590.html)  [**Get One Now 🖱️**](https://www.seeedstudio.com/reComputer-J4011-p-5585.html) | | | | | |

* (Any Linux machine)

* Supported Architectures: armv6l(32bit), armv7l(32bit), aarch64(64bit), x86\_64(64bit)
* Required disk space: ≥ 32 MB
* Required RAM space: ≥ 4MB (In default settings)
* Network Communication Interfaces: A physical network adapter must be on board.
* Monitor, keyboard, mouse (optional)

## Getting Started

### Sign Up for a NEQTO Account

* Step 1. Visit the [official page](https://console.neqto.com/register) to sign up for a NEQTO account
* Step 2. Enter your email address, create a password, and proceed
* Step 3. Verify the account from the activation email you receive

### Installation of NEQTO Linux

1. Select `Manage API Keys for Linux-based Device` from

in NEQTO Console

2. Click `CREATE API KEY`

And then the API Key will be displayed

3. Download `NEQTO Engine Linux Installer` by curl or wget.

   This time, use the wget command.

Copy the `Download link` of `Installer of NEQTO Engine for Linux` and paste it after "wget␣".

Installer downloads successfully

4. Change the execution permissions of the downloaded installer (`neqto-daemon-install.latest.sh`) with the chmod command before running the installation of NEQTO Engine for Linux.

5. Copy the `API Key` from `API Keys for NEQTO Engine for Linux` in the NEQTO Console and paste it after `sudo . /neqto-daemon-install.sh␣-k␣`.

6. Enter Password

7. Just after execution, important notes will be displayed. Please check it and enter "agree" if you agree. Thereafter, device registration will be executed, and software installation will continue.

8. Please wait until the final status `Installation completed successfully!` is displayed.

Confirmation that the device has been registered on the NEQTO Console

### Hello World

1. Click on `ADD GROUP` under `GROUPS`.

2. Enter `reComputer J30` in `Name` and click `SAVE`

3. Select the `reComputer J30` you created and click `SCRIPTS`

4. Click `ADD SCRIPT`

5. Enter `Hello World` in the `Name` field and click `SAVE`

6. Copy and paste the [sample code](https://docs.neqto.com/docs/en/getting-started/tutorial-step1#sample-code) from `Getting Started` into the NEQTO Console script editor and then click `Save`.

7. Click on `TEMPLATES`

And then click on `ADD TEMPLATE`

8. Set `DEVICE INFORMATION` as follows

   * Enter `reComputer J30 Template` for `Name` field
   * Select `Linux-based device` for `Firmware Type` field
   * Select the latest version for `Firmware Version` field

9. For `OPTIONS`, select `Hello World` in `Script` field and click `SAVE`

10. Click on `NODES`

And then click on `ADD NODE`

11. Set `META DATA` as follows

    * Set `Name` field to `reComputer J30`
    * Set `Template` field to `reComputer J30 Template`

12. Select the device you just registered in `DEVICE INFORMATION` and click `SAVE`

13. Type `tail -F /tmp/neqto/log/neqto.log` on the terminal on reComputer J30

14. After running `Reload Script` on NEQTO Console, you can see `Hello World!!!` on the terminal of reComputer J30

## What's More / Trouble Shooting

* [NEQTO Support](https://support.neqto.com/hc/en-us)
* [Support Guidelines](https://docs.neqto.com/docs/en/neqto/support-guidelines)

## Resource

* [NEQTO Resource Center](https://docs.neqto.com/docs/en/linux/software/requirements)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.
