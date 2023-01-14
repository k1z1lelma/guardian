# Guardian

![logo](https://github.com/k1z1lelma/guardian/blob/main/pictures/guardian_intro.png)

## Introduction

Today, we use our computers to communicate with people, do our jobs, have fun, and much more. Windows operating systemis one of the most used operating systems in the world. Microsoft leaks a lot of data in the background. These data are not just error messages. It also leaks personal data. It also shares this data with others. It clearly states this on its website. Now let's look at the privacy statement published by Microsoft.

![Microsoft Privacy Statements](https://github.com/k1z1lelma/guardian/blob/main/pictures/microsoft_privacy_statement.png)

[Microsoft Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)

As seen in the agreement, Microsoft admits to collecting personal data. It also tells us that if you refuse to provide this data, we will not be able to use Windows applications and services. One of the purposes for developing the Guardian tool is to protect privacy. Other aim of the project are to take basic security measures on devices with Windows operating system.

## Installation

The tool is written in Python programming language. There is no Python 2 support.

* `https://github.com/k1z1lelma/guardian.git`
* `cd guardian`
* `python main.py` or `python3 main.py`

## Usage

The program consists of three main menus. Full protection menu with simple security, privacy and adjustment of all settings in these menus.

![main menu](https://github.com/k1z1lelma/guardian/blob/main/pictures/main_menu.png)

* When we enter 1 from the keyboard, we enter the simple security menu and the hardening settings we can make in this menu are as in the image.

![basic security](https://github.com/k1z1lelma/guardian/blob/main/pictures/security_menu.png)


* I can say that the most important menu is menu number 2. Here, the collection of personal data collected by Microsoft is prevented.

![privacy security](https://github.com/k1z1lelma/guardian/blob/main/pictures/privacy_menu.png)

* If you do not want to adjust the settings in the privacy and security menu one by one, the full protection menu is for you :)

![full protection](https://github.com/k1z1lelma/guardian/blob/main/pictures/full_protection.png)

After making these settings, you will prevent many personal data collected by Windows from being sent. However, we need to enter some DNS records in the host file so that these settings are not withdrawn by Windows with any update. The DNS records entered here are the domain addresses to which the data is sent. The action taken here is very simple. When computers want to communicate with a remote computer, they need to decode the address of the remote device. Let's examine how Windows machines handle name resolutions. These steps are as follows:
* First of all, the host file in the file system is checked. Thanks to this file, it checks whether the device to be accessed is itself. In addition, the system information that it wants to access in the configuration files is queried.
* If the information about the device to be accessed is available in the cache, this information is retrieved from the DNS cache on the machine.
* If the information of the target machine is not in the cache, a query is sent to the DNS server defined in the network.
<br/>
In other words, when the device wants to go to a remote computer, the first place it will visit is the host file. In the DNS records we entered here, we give the 0.0.0.0 IP address, that is, localhost. This means that when our device wants to communicate with Windows Domain addresses, it will be directed to localhost and will not be able to send the collected data to Microsoft servers.

<br/>

Therefore, answer "Y" to the question asked when exiting the program.

![host](https://github.com/k1z1lelma/guardian/blob/main/pictures/exit_host.png)
