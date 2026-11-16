# Advanced Settings - System

System is to manage the AP controller's systematic features. It includes System Time, Firmware, Backup/Restore, Administration, Admin Account, Language, Timed Reboot, Reboot, Reset, LED Control, and TR069 (not in Wireless Access Point mode).

- For *Main AP controller and AP Controller* mode
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/advanced-mc.webp" alt="" width="800px" style="border: 1px solid #eee;display:block; margin:0 auto;" />
- For *AP Controller* mode
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/advanced-ac.webp" alt="" width="800px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

## System Time
It is the time displayed while the AP controller is running. The system time you configure here will be used for other time-based functions like WiFi schedule, parental control, etc. 

*To configure the system time, please follow the steps below.*

1. Select your Timezone from the drop-down list.
2. Select a *Set Time* method: Get from Internet, Get from Managing Device, or Manual.
    - Get from the Internet: AP controller will synchronize the time with the Internet of the NTP server, for 	which you've entered its IP address or domain name.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/system-time-internet.webp" alt="" width="400px" style="border: 1px solid #eee; display:block; margin:0 auto;"/>
    - Get from Managing Device: AP controller will synchronize the time with your device connected.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/system-time-device.webp" alt="" width="400px" style="border: 1px solid #eee;display:block; margin:0 auto;"/>
    - Manual: AP controller will display the time you have manually set (YY/MM/DD HH:MM:SS).
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/system-time-manual.webp" alt="" width="400px" style="border: 1px solid #eee;display:block; margin:0 auto;"/>

3. Click *Save & Apply*.

## Auto Upgrade
It is to automatically download and install the latest firmware for connected APs during scheduled maintenance windows.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/advanced-system-autoupdate.webp" alt="" width="500px" style="border: 1px solid #eee; display:block; margin:0 auto;" />

1. Toggle to enable *Auto Update*.
2. Check the *Current Time*.
3. Select an appropriate *Update Time* from the pull-down list.
4. Select the AP(s) you would like to upgrade at the scheduled time.

## Backup/Restore
The settings are stored as a configuration file in the AP controller. You can back up the configuration file in your computer for future use, or restore the AP controller to a previous settings from the backup file when needed.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/advanced-system-backup.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

- To back up the configuration file, just click *Generate backup* to download and save a copy of the current settings in your local computer in the form of *.bin* file.
- To restore the backup configuration file later on, click *Browser...* to locate and upload the backup configuration file stored in your computer, and then click *Restore* to restore and reboot. It may take a few minutes. Please do not turn off or reset the AP controller in this process.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/advanced-system-restore.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

## Administration
It allows you to access and manage the AP controller from the local network devices via Local Management, and access and manage the AP controller over the Internet via Remote Management.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/admin.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

- Local Management
    - HTTPS Only: Enable to force secure HTTPS connections for all management access.
    - Local Managers: Define who can access the controller among the local network devices. 
        - All Devices: Allow all LAN-connected devices to manage the AP controller. 
        - Specified Devices：Specify certain devices to manage the AP controller by enter the custom MAC address in *Other Devices* field.
    - Current Device: Refers to the AP controller itself (not its managed APs), used to configure local system settings like firmware/IP.
- Remote Management
    - HTTPS Port: Specify the secure port for encrypted web management access. Default is 443; change if conflicted.
    - Web Address: Displays custom domain/IP to access the controller's interface.
    - Remote Managers: Define external users/IPs permitted to manage the controller.
    - Only this IP Address: Restricts admin access to a single trusted IP for maximum security.

Click *Save & Apply* to save and activate the settings, and then the devices on the Internet can log in to *https://AP controller's WAN IP address:port number* to manage the AP controller.

!!! Note
    You can find the WAN IP address of the AP controller on *System Status -> WAN*. The AP controller's WAN IP is usually a dynamic IP. Please refer to *Advanced Settings -> Network -> DDNS* if you want to log into the AP controller via a domain name.

## Admin Account
To change your login password for the AP controller's web management page.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/admin-account.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

1. Enter the old password.
2. Create a new password and Confirm it. 
3. Click *Save & Apply* for the new password to take effect. 

!!! Note
    The password should be a value between 8 and 64 characters long.

## Language
To customize the AP controller's web management language. Otherwise, the AP controller will auto-detect your system language and synchronize it. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/language.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

If any change, please click *Save & Apply* for the settings to take effect.

## Timed Reboot
It will clean the cache to enhance the running performance of the AP controller as scheduled. 
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/timed-reboot.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

*To set the reboot schedule, please follow the steps below.*

1. Enable Timed Reboot.
2. Select the *Week Day* to specify how often you would like the AP controller to reboot.
3. Set a specific *Hour* and *Minute* when the AP controller should reboot on the specified day.
4. Click *Save & Apply* for the settings to take effect.

## Reboot 
Rebooting the AP controller after working for a long periods of time can release some storage space in the RAM and improve system performance, making the operation of the AP controller smoother. Rebooting does not affect any settings of the AP controller.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/reboot.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Click *OK* to reboot the system immediately. Wait a few minutes for the system to reboot. 

!!! Note
    You may also reboot the AP controller by turning off its power supply.

## Reset
will help you erase all the current settings and restore the AP controller to its factory defaults. Alternatively, you may reset the AP controller via the *RESET* button on the AP controller panel, or on this web management page.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/reset.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Before clicking *OK* to reset it, please note down the SSID and password (or refer them to the product label) for later reconnection.

Wait a moment for it to reboot and reset. When completed, it will pop up the login page requiring you to create a password again. Create a new login password and reconfigure your AP controller.

!!! Note
    - During the rebooting process, do not turn off or reset the AP controller. 
    - It's recommended to [back up](#backuprestore) the current configurations before resetting the AP controller.

## TR069

**This is only available in Main AP controller and AP Controller mode.**

TR-069, also known as CWMP (CPE WAN Management), allows Auto-Configuration Server (ACS) to perform auto-configuration, provision, connection, and diagnostics to this device. You may configure this function under your ISP's instructions.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/tr069.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Configure the parameters according to your ISP instructions, and click *Save & Apply*.

- Enable: Click to enable the TR069/CWMP function.
- Inform: Enable to send an inform message to the ACS periodically.
- Inform Interval: Enter the time interval when the inform message will be sent to the ACS.
- Data Model: Select the data model of the inform message sent to the ACS, according to your ISP's 
instructions. 
    - TR-098: Legacy data model for basic home gateways.
    - TR-181: A modern Broadband Forum Device:2 data model providing a hierarchical structure for CPE and connected device management. It supports IoT-related device modeling and is widely used in TR-069 and TR-369 (USP) management frameworks.
- ACS URL: Enter the web address of the ACS provided by your ISP.
- ACS Username/Password: (Optional) Enter the username/password to log in to the ACS server.
- Connection Request Auth: If enabled, you may optionally enter the *Username* and *Password* for the ACS server to log in to the AP controller; otherwise just ignore it.
- Port: Enter the port (a value from 1024~65535) that connects to the ACS server.
- STUN: If enabled, you need to enter the STUN server port and kept-alive period, and optionally the STUN username/password/server address to log in the AP controller.

## Operation Mode

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/operation_mode.webp" alt="" width="200px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Displays the current operation mode. Select to switch to the other operation mode from the drop-down list, and click *Save & Apply* .

## Cloud Management

Cloud Management allows you to remotely manage your AP through Cudy Cloud. Enable this feature to prepare the AP for binding to a Cudy Cloud account. Once bound, you can manage the AP remotely through the cloud platform.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/cloud_management.webp" alt="" width="200px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

- Cloud Status: Displays the current cloud management status of the AP.
- Serial Number: Displays the AP's serial number, which can be used to identify the device when binding it to Cudy Cloud.
- Unbind account when disable Cloud Management: Select this option to unbind the AP from its Cudy Cloud account when Cloud Management is disabled.

For more instruction, please refer to the tutorial: [How to manage AP controller remotely?](/tutorial/how_to_remote_manage_ap_controller/)

## SSH

SSH (Secure Shell) is a secure protocol that allows to remotely access and manage the AP through a command-line interface (CLI). It encrypts data transmitted between the SSH client and the AP to protect your login credentials and management data.

Enable SSH to allow secure remote access to the AP through an SSH client. Disable it to prevent new SSH connections. Only enable this when requested by technical support.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/ssh.webp" alt="" width="200px" style="border: 1px solid #eee;display:block; margin:0 auto;" />
