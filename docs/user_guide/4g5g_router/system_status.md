# System Status

On the **System Status** page, you can check the status of the router system, including Status, Mesh, Devices, WAN, LAN, WISP, Wireless 2.4G/5G/6G (if supported), VPN, DHCP Server, and System.

!!! Note
    P2 is used as an example in this guide. Refer to your actual product for more details.

- **Status**: Shows whether the router has connected to the Internet or not, and its work mode and interface. Click [*Quick Setup*](qig.md){ data-preview } to redirect to the Quick Setup page.

- **Mesh** (if available for your model): Shows the router’s Mesh network status (SOLE or MESH), the mesh device name and the amount of mesh units. Click [*More Details*](mesh.md){ data-preview } to know more information or add/manage mesh unit(s).

- **Devices**: Shows the number of devices connected to this Router, via Ethernet cable or 2.4G WiFi or 5G WiFi. Click *More Details* to know more information about these devices, or configure the settings.
    - *Status* shows the number of devices connected to this Router, via Ethernet cable or 2.4G WiFi or 5G WiFi. 
        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/devices-status.webp" alt="" width="800px" style="border: 1px solid #eee;" />

    - *Devices* allows for some settings about these connected devices.
        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/devices-devices.webp" alt="" width="800px" style="border: 1px solid #eee;" />

        - Internet: Click to enable/disable the Internet for the devices.
        - VPN: Click to enable/disable VPN for the devices.
        - Operation: Click to pop up the editing page as below, where you can customize the device name and limit the download/upload rate.

- **5G** (or **Cellular**): Shows the cellular network status, SIM card status and APN profile type. Click [*More Details*](general_settings_cellular.md){ data-preview } to know more information about it or make changes on Settings page. 

- **WAN**: Shows the WAN port connection status. Click [*More Details*](general_settings_wan_mode.md){ data-preview } to know more information about it or make changes.

- **LAN**: Shows the connected LAN port status. Click [*More Details*](advanced_settings_network.md#lan){ data-preview } to know more information about it or make changes.

- **WISP** (if available for your model): Shows the router's status of the connection to an existing Wi-Fi network and share its internet connection with connected devices. Click [*More Details*](mesh.md){ data-preview } to know more information or change to connect with another network.

- **Wireless 2.4G**: Shows the Wireless 2.4G status. Click [*More Details*](general_settings_wireless.md){ data-preview } to know more information about it or make changes.

- **Wireless 5G**: Shows the Wireless 5G status. Click [*More Details*](general_settings_wireless.md){ data-preview } to know more information about it or make changes.

- **Wireless 6G** (if available for your model): Shows the Wireless 6G status. Click [*More Details*](general_settings_wireless.md){ data-preview } to know more information about it or make changes.

- **IPv6**: Shows IPv6 connection status. Click [*More Details*](advanced_settings_network.md#ipv6){ data-preview } to know more information about it or make changes.

- **VPN**: Shows VPN connection status. Click [*More Details*](general_settings_vpn.md){ data-preview } to know more information about it or make changes.

- **DHCP Server**: Shows the DHCP Server status. Click [*More Details*](advanced_settings_network.md#dhcp){ data-preview } to know more information about it or make changes.

- **System**: Shows the System status. Click *More Details* to view more information about it.

    - *Status* shows the Router info about firmware version, model, hardware version, local time and uptime.
        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/system_status_1.webp" alt="" width="800px" style="border: 1px solid #eee;" />

    - *Statistics* shows the detailed traffic information of each interface in the statistics list.
        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/system_status_2.webp" alt="" width="800px" style="border: 1px solid #eee;" />

    - *ARP* lists the connected devices' IP address with its bound MAC address, Hostname and Interfaces.
        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/system_status_3.webp" alt="" width="800px" style="border: 1px solid #eee;" />

    - *Active IP Routes* table contains a list of routes to network destinations associated with and known by the Router.
        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/system_status_4.webp" alt="" width="800px" style="border: 1px solid #eee;" />

    - *System Log* tracks all the Router behaviors. It is used for [*technical support*](mailto:support@cudy.com) to diagnose and troubleshoot for the Router.  It is also available on *Diagnostic Tools -> System Log* page.

        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/system_status_5.webp" alt="" width="800px" style="border: 1px solid #eee;" />

        - Update: Click to refresh the system log.
        - Clear: Click to erase all the system log up till now.
        - Download: Click to download the system log for technical support.