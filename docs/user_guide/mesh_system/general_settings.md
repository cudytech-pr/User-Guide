# General Settings 

!!! Note
    M1200 is used as an example in this guide. Refer to your actual product for more details.

## WAN Mode

*WAN Mode* is to set your Internet connection. Select your Internet connection type from the drop-down list of Protocol. Follow the instructions on the page to continue the configuration. Parameters on the figures are just used for demonstration.

### DHCP
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wan-dhcp.webp" alt="" width="800px" style="border: 1px solid #eee;" />

If you choose *DHCP*, keep MTU as default unless your ISP provides differently. The Host name and MAC address Clone are optional. Then *Save & Apply* your configurations.

### PPPoE
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/wan-pppoe.webp" alt="" width="800px" style="border: 1px solid #eee;" />

If you choose *PPPoE*, enter the Username and Password provided by your ISP. Then *Save & Apply* your configurations.

### Static (Fixed IP)
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/wan-staticip.webp" alt="" width="800px" style="border: 1px solid #eee;" />

If you choose *Static (Fixed IP)*, enter the parameters provided by your ISP, including IP Address / Subnet Mask / Default Gateway / Preferred DNS. Keep MTU as default unless your ISP provides differently. Then *Save & Apply* your configurations.

### L2TP
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/wan-l2tp.webp" alt="" width="800px" style="border: 1px solid #eee;" />

If you  choose  *L2TP*,  enter parameters for Server Address/Username/Password. And then select Addressing Type provided by your ISP, and configure the required parameters. Keep MTU as default unless your ISP provides differently. Then *Save & Apply* your configurations.

### PPTP
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/wan-pptp.webp" alt="" width="800px" style="border: 1px solid #eee;" />

If you choose *PPTP*,  enter parameters for Server Address/Username/Password. And then select Addressing Type provided by your ISP, and configure the required parameters. Keep MTU as default unless your ISP provides differently. Then *Save & Apply* your configurations.

## WISP

WISP supports the router to wirelessly connect to a distant Wi-Fi network and share that connection locally via Ethernet/Wi-Fi, acting as a client bridge. 

You may check the Host Network status on the *System Status -> WISP -> More details -> Status*.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wisp1.webp" alt="" width="800px" style="border:1px solid #eee; display:block; margin:0 auto;" />

You may configure the WISP function through *System Status -> WISP -> More details -> Settings* or *General Settings -> WISP* page.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wisp2.webp" alt="" width="800px" style="border:1px solid #eee; display:block; margin:0 auto;" />

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wisp3.webp" alt="" width="800px" style="border:1px solid #eee; display:block; margin:0 auto;" />

Please follow the steps to configure it.

1. Turn on *Enabled* to activate the WISP function.
2. Select to connect to 5GHz or 2.4GHz WiFi network. Then click *Scan* to search for available Wi-Fi networks. If necessary, click *Rescan* to re-search or update the host network list.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wisp4.webp" alt="" width="800px" style="border:1px solid #eee; display:block; margin:0 auto;" />
    - *BSSID*: Displays the MAC address of the host network.
    - *SSID*: Displays the visible name of the host Wi-Fi network.
    - *Channel*: Displays the frequency band the host network uses.
    - *Signal*: Displays the host network's signal strength.

3. Select your target host network and click *Connect* to pop up the connection page.

4. Enter the password if required and click *Save & Apply*.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wisp5.webp" alt="" width="500px" style="border:1px solid #eee; display:block; margin:0 auto;" />

*Success!*

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wisp3.webp" alt="" width="800px" style="border:1px solid #eee; display:block; margin:0 auto;" />

## Wireless

*Wireless* is to customize the Router’s wireless settings, including SSID and password, mode, channel, channel width and transmit power, and so on. You may configure on the page *General Settings -> Wireless*.

### 2.4G/5G

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wireless.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- Smart Connect: 
    When it is enabled, 2.4GHz and 5GHz networks will share the same network name and password (only one SSlD will be displayed). Your wireless devices will automatically switch to connect to the Wi-Fi band providing the fastest speed. No manual configuration is needed.

*To manually configure the 2.4G/5G wireless settings, please follow the steps below.*

1. Go to *General Settings -> Wireless -> 2.4GHz/5GHz*.
2. Enable *Wireless 2.4G/Wireless 5G*;
3. Customize your 2.4G/5G SSID (wireless network name);
4. Select a strong Encryption and create a secure password for your wireless network;
5. Select a proper *Mode*, *Channel*, *Channel Width* and *Transmit Power*;
6. (Optional) Enter the maximum number of devices you want to allow on your network in the *Max Stations* field.
7. Enable *Hidden Network*, if you don’t want your SSID to display automatically. Then you need to manually join the network.
8. Enable *Separate Clients* to isolate the wireless clients from each other.
9. Click *Save & Apply* to apply your new settings.

### 6G

Wireless 6G is only available for tri-band products, such as M11000 and more.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images//mesh_system/wireless_6g.webp" alt="" width="800px" style="border: 1px solid #eee;" />

1. Go to *General Settings -> Wireless -> 6GHz*.
2. Enable *Wireless 6G*;
3. Customize your *SSID* (wireless network name);
4. Select a strong *Encryption* and create a secure *Password* for your wireless network. Click *Save & Apply* to save these basic settings, or *Advanced* to continue with more and advanced settings.
5. Select a proper *Mode* and *Transmit Power*;
6. (Optional) Enter the maximum number of devices you want to allow on your network in the *Max Stations* field.
7. Enable *Hidden Network*, if you don’t want your SSID to display automatically. Then you need to manually join the network.
8. (If any) Enable *Separate Clients* to isolate the wireless clients from each other. 
9. Click *Save & Apply* to apply your new settings.

### MLO

MLO (Multi-Link Operation) enables Wi-Fi 7 devices to simultaneously send and receive data across different frequency bands and channels. This ensures fast and reliable connections even in dense network environments. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/wireless-mlo.webp" alt="" width="800px" style="border: 1px solid #eee;" />

1. Enable *MLO Network*.
2. Customize the SSID for your wireless network.
3. Select the *Band*.
4. Select the *Encryption* and set the *Password*.
5. Enable *Hidden Network*, if you don’t want your SSID to display automatically. Then you need to manually join the network.
6. Click *Save & Apply* to apply your new settings.

## Guest Network
Guest Network allows you to provide Wi-Fi access for guests without disclosing your main network. When you have guests in your house, apartment, or workplace, you can create a guest network for them. In addition, you can customize guest network options to ensure network security and privacy. Please follow the steps below to set up a guest network.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-2.4g.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**To set up a guest network, please follow the steps below.**

1. Enable *2.4G/5G* (and *6G* if any) Guest Network.
2. Customize the *SSID*. Don’t enable *Hidden Network* unless you want your guests to manually input the SSID for guest network access.
3. Select your *Encryption* type and create a *Password*.
4. Enable *Access Filter*. If enabled, the firewall-related functions (such as MAC filter, IP filter, and domain filter, parental control, etc.) will take effect on clients connected to the guest network.
5. Click *Save & Apply*. 

Now your guests can access your guest network using the SSID and password you set.

## IPTV/VLAN
If you want to enjoy IPTV or VoIP service, or your ISP requires VLAN tags, please follow the steps below to configure the IPTV/VLAN.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-iptv.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Enable IPTV/VLAN.
2. Select the Mode according to your ISP from the drop-down list.
    - Select Bridge if your ISP is not listed and no other parameters are required.
    - Select Custom if your ISP is not listed but provides necessary parameters.

    !!! Note
        Once Mode is selected, the necessary parameters are predetermined, including Internet VLAN ID, IPTV VLAN ID and LAN port for IPTV connection. Otherwise, please select the LAN type to determine which port is used to support IPTV service. 

3. Click *Save & Apply*.
4. Connect the set-top box to the corresponding LAN port predetermined by the ISP or specified by you in STEP 2. You may need to configure your set-top box before enjoying your TV.

!!! Success
    Congratulations! Your IPTV setup is done now.

## VPN
**VPN (Virtual Private Network)** helps you access Internet resources remotely, securely, and privately through tunneling technology. When you access the Internet, VPN encrypts your personal information and hides your IP address from the public. For VPN users, it looks like the devices are directly connected. Cudy Router supports 6 types of VPN connections: PPTP, L2TP, OpenVPN, WireGuard, ZeroTier, IPSec (site-to-site). Please choose an appropriate VPN according to your needs and circumstances.

!!! Note
    Before you enable VPN Server, it is recommended to configure Dynamic DNS Service or assign a Static IP Address for router’s WAN port and synchronize your System Time with Internet. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/vpn.webp" alt="" width="800px" style="display: block; margin: 0 auto;" />

### PPTP VPN
**PPTP VPN** is used to create a PPTP VPN connection for remote devices to access your home network. Fast connection/disconnection and simple configuration satisfy the needs for users who is apt to frequently switch VPN environments. Please follow the steps below to set up a PPTP VPN connection.

**STEP 1. Configure the PPTP Server on Mesh A:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/pptp-server.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Mesh A’s management web page [https://cudy.net](https://cudy.net) (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select PPTP Server as Protocol. 
3. Select Client Access (Internet and Local Network/Internet/Local Network).
4. Configure the PPTP Server.
    - MPPE Encryption: Enable to encrypt the data transmitted via PPTP VPN, thus improve the communication security.
    - Server IP/IP Start/Limit: Set to assign IP address for the VPN Clients.
    - Username/Password: Set for the VPN client to access the VPN Server.

5. Click *Save & Apply*.	

**STEP 2. Configure PPTP Client on Mesh B:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/pptp-client.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Mesh A’s management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select PPTP Client as Protocol. 
3. Select Allow all devices or Ban all devices as Default Rule.
4. Enable Site-to-Site to allow communication between VPN server and Clients.
5. Select VPN Policy. 
    - Disable: VPN Policy is disabled. No restriction.
    - VPN kill switch: Internet access will be disconnected upon VPN disconnection. It is highly recommended for users who transmit data all through VPN. Preferred (and optionally Alternate DNS) is required. 
    - Domain: Select and configure to allow specified domain(s) to transmit data through VPN or not. DNS and Domain are required.
    - Remote Subnet: Select and configure to allow devices with the specified subnet to transmit data through VPN. IP address and Subnet mask are required.

6. Configure the PPTP Client:
    - Server Address/ Username/Password: Enter the parameters provided by the PPTP Server.
    - Encryption: Enable to ensure the data security for the PPTP clients.	

7. Click *Save & Apply*.

### L2TP VPN 

**L2TP VPN Server** is used to create a L2TP VPN connection for remote devices to access your home network. Compared with PPTP, L2TP supports multi-tunnel with authentication between two endpoints, thus users can set up different tunnels with various service quality. Please follow the steps below to set up a L2TP VPN connection.

**STEP 1. Configure the L2TP Server on Mesh A:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/l2tp-server.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Mesh A’s management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select L2TP Server as Protocol. 
3. Select Client Access (Internet and Local Network/Internet/Local Network).
4. Configure the L2TP Server.
    - Server IP/IP Start/Limit: Set to assign IP address for the VPN Clients.
    - Tunnel Secret (Optional): To set a L2TP VPN encryption as needed.
    - Pre-shared Key (Optional): To set a IPSec encryption as needed.
    - MTU: Maximum Transmission Unit is 1400 by default. You may change it if necessary.
    - Username/Password: Set to authenticate the VPN clients to access the VPN Server.

5. Click *Save & Apply*.

**STEP 2. Configure L2TP Client on Mesh B:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/l2tp-client.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Mesh A’s management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select L2TP Client as Protocol. 
3. Select Allow all devices or Ban all devices as Default Rule.
4. Enable Site-to-Site to allow communication between VPN server and Clients.
5. Select VPN Policy. 
    - Disable: VPN Policy is disabled. No restriction.
    - VPN kill switch: Internet access will be disconnected upon VPN disconnection. It is highly recommended for users who transmit data all through VPN. Preferred (and optionally Alternate DNS) is required. 
    - Domain: Select and configure to allow specified domain(s) to transmit data through VPN or not. DNS and Domain are required.
    - Remote Subnet: Select and configure to allow devices with the specified subnet to transmit data through VPN. IP address and Subnet mask are required.

6. Configure the L2TP Client:
    - Server Address/ Username/Password: Enter the parameters provided by the PPTP Server.
    - Local Hostname: Customize or keep it as default.
    - Tunnel Secret / Pre-shared Key: Enter the encryption if the L2TP Server has set it.
    - MTU: Maximum Transmission Unit is 1400 by default, you may change it if necessary.
    - Use custom tunnel IP: Enable and enter it if the L2TP Server provides a tunnel IP bound with the account.

7. Click *Save & Apply*.

### OpenVPN

**OpenVPN Server** is used to create an OpenVPN connection for remote devices to access your home network. OpenVPN server requires a public IP. You can confirm whether the router has a public IP on the router management page System Status -> WAN -> More details -> Status. If the public IP displayed is consistent with the IP address of the router's WAN port, it means that the router has a public IP. Please follow the steps below to set up an OpenVPN connection.

**STEP 1. Configure the OpenVPN Server on Mesh A:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/openvpn-server.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Mesh A’s management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select OpenVPN Server as Protocol. 
3. Select the Client Access (Internet and Local Network / Internet / Local Network).
4. Configure the OpenVPN Server.
    - OpenVPN Protocol: Select UDP or TCP as desired.
    - Service Port: 1194 by default, keep it or change it as needed.
    - VPN Subnet: Set up a VPN subnet segment.
    - Subnet Mask: Select or customize as needed.

5. Click *Save & Apply*.
6. Click EXPORT to export the configuration file, for the OpenVPN Client to upload.

**STEP 2. Configure OpenVPN Client on Mesh B:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/openvpn-client.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Mesh A’s management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select OpenVPN Client as Protocol. 
3. Select Allow all devices or Ban all devices as Default Rule.
4. Enable Site-to-Site to allow communication between VPN server and Clients.
5. Select VPN Policy. 
    - Disable: VPN Policy is disabled. No restriction.
    - VPN kill switch: Internet access will be disconnected upon VPN disconnection. It is highly recommended for users who transmit data all through VPN. Preferred (and optionally Alternate DNS) is required. 
    - Domain: Select and configure to allow specified domain(s) to transmit data through VPN or not. DNS and Domain are required.
    - Remote Subnet: Select and configure to allow devices with the specified subnet to transmit data through VPN. IP address and Subnet mask are required.

6. Click *Browse...* to locate the Configuration file (client.ovpn) you exported previously from the OpenVPN Server. The uploaded configuration file will be automatically read and the Server IP will be displayed.  
7. Click *Save & Apply*.

### WireGuard VPN

**WireGuard VPN Server** is used to create a Wire Guard VPN connection for remote devices to access your home network. WireGuard VPN server requires a public IP. You can confirm whether the router has a public IP on the router management page System Status -> WAN -> More details -> Status. If the public IP displayed is consistent with the IP address of the router's WAN port, it means that the router has a public IP. Please follow the steps below to set up a WireGuard VPN connection.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/wireguard-server.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**STEP 1. Configure the WireGuard Server on Mesh A:**

1. Log into the Mesh A’s management web page https://cudy.net (or 192.168.10.1).
2. Go to General Settings ->VPN. Enable VPN, and select WireGuard Server as Protocol. 
3. Select Client Access (Internet and Local Network / Internet / Local Network).
4. Configure the WireGuard Server:
    - IP Address: 10.10.10.1 by default. You may change it if necessary.
    - Listen Port: 51820 by default. You may change it if necessary.
    - MTU: Maximum Transmission Unit is 1400 by default. You may change it if necessary.

5. Click *Save & Apply*. Then you will be required to configure the Client parameters.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/client-edit.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

6. Click Edit Items to add entries. Enter the required parameters and then click Save.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/client-edit2.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

    - IP Address: Enter the Client IP address.
    - Remote Subnet: Enter the Client Subnet.
    - Hostname: Customize the client hostname.
    - Delete: Click to delete as needed.

7. Click to export the configuration file, and then upload it on the client for VPN connection.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/client-export.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**STEP 2. Configure WireGuard Client on Mesh B:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/wireguard-client.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Mesh A’s management web page https://cudy.net (or 192.168.10.1).
2. Go to General Settings ->VPN. Enable VPN, and select WireGuard Client as Protocol. 
3. Select Allow all devices or Ban all devices as Default Rule.
4. Enable Site-to-Site to allow communication between VPN server and Clients.
5. Select VPN Policy. 
    - Disable: VPN Policy is disabled. No restriction.
    - VPN kill switch: Internet access will be disconnected upon VPN disconnection. It is highly recommended for users who transmit data all through VPN. Preferred (and optionally Alternate DNS) is required. 
    - Domain: Select and configure to allow specified domain(s) to transmit data through VPN or not. DNS and Domain are required.
    - Remote Subnet: Select and configure to allow devices with the specified subnet to transmit data through VPN. IP address and Subnet mask are required.

6. Click *Browse...* to locate the Configuration file (wg-client-x.conf) you exported previously from the WireGuard Server. The uploaded configuration file will be automatically read and such parameters as below will be displayed.  
7. Confirm the parameters and then click *Save & Apply*.

### ZeroTier VPN

**Zerotier** is a third-party cloud platform for VPN connections. It can establish a VPN connection without any public IP address node to achieve secure and remote access. It is free for use with less than 50 nodes. It is simple and convenient to set up. Please follow the steps below to set up a ZeroTier VPN connection.

**STEP 1. Register for a ZeroTier Account and Obtain a Network ID.**

1. Visit Zerotier website http://my.zerotier.com/, sign up for an account and log in.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

2. Click Network - > Create A Network. 
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier2.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

3. Zerotier will create a new network and assign a NETWORK ID for you. Then click on the assigned NETWORK ID, and its setting page will display.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier3.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

4. Set Access Control to be Public for later convenient settings, and note down the Network ID.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier4.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

!!! Note
    Private Access Control requires authorization for the terminal or router to access the network, which is more secure but inconvenient. While Public Access Control allows for a direct the network access with authentication rather than authorization. You may choose either one accordingly.

**STEP 2. Configure ZeroTier Master on Mesh A.**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier-master.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Mesh A’s management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select ZeroTier Master as Protocol. 
3. Select Client Access (Internet and Local Network/Internet/Local Network).
4. Enter the ZeroTier Network ID noted down previously.
5. Click *Save & Apply*. Then it will display the Device ID.
6. Back to the ZeroTier web page, you will see One device has joined this network.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier5.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />


**STEP 3. Join ZeroTier Network on your device.**

1. Download and Install ZeroTier Software from https://www.zerotier.com/download/.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier6.webp" alt="" width="400px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

2. Click the ZeroTier icon and then Join New Network..., enter the Network ID and click Join.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier7.webp" alt="" width="400px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

3. Back to the ZeroTier web page, you will see this new device and its Managed IP.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier8.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**STEP 4. Configure the Static Route.**

Go to Settings -> Advanced on the ZeroTier web page. Under Add Routes, enter Router’s LAN IP segment 192.168.10.0/24 in Destination field and its Managed IP in Via field, and then click Submit.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier9.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

Now your client devices can directly access the router's management web page via 192.168.10.1 as well as the server via its IP address.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/zerotier10.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

### IPSec (site-to-site) VPN

**IPSec (site-to-site) VPN** is a secure tunneling protocol used to connect two different networks, typically a corporate network and a remote branch office network, over the Internet. It allows multiple users at the remote site to access resources on the main office network as if they were directly connected to it. Please follow the steps below to set up an IPSec (site-to-site) VPN connection.

**STEP 1. Get both Routers in the Headquarter and Branch Office ready.**

1. Make sure both Routers are connected to the Internet, but two network can not be in the same LAN segment. 
For example, if the headquarter is in the LAN segment 192.168.10.0/24, then the branches should be in a different LAN segment, say, 192.168.20.0/24.
2. Check and note down the WAN and LAN IP addresses of the Headquarter Router and Branch Office Router on their management Status page. WAN IP of the headquarters router is the remote gateway of the branch offices, and its LAN IP is the remote subnet of the branch offices; and vice versa.

**STEP 2: Configure the IPSec VPN on the Router in the Headquarter.**

1. Log into the  Mesh A’s management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select IPSec (site-to-site) as Protocol. 
3. Click Add to add IPSec Policies and configure the required parameters.
    - Policy Name: Name the policy as desired. 
    - Remote Gateway: Enter the WAN IP of the Router in branch office.
    - Local Subnet: Auto-filled the LAN segment of the local router.
    - Remote Subnet: Enter the LAN segment of the Router in branch office.
    - Pre-shared key: Set an encryption key as desired.

4. Set the Dead Peer Detection parameters.
    - Dead Peer Detection: Enable to detect whether the peer end is alive or not;
    - Check Interval: Keep 30 seconds as default or change as needed;
    - DPD Timeout: Set when to perform PDP checking again. Keep 2 Minutes as default or change it as needed.
    - DPD Action: Decide what to do after DPD detection failure, Restart, Hold or Clear. It is recommended to keep Restart as default.

5. Click *Save & Apply*. 

**STEP 3: Configure the IPSec VPN on the Router in the Branch Office.**

1. Log into the  Mesh A’s management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select IPSec (site-to-site) as Protocol. 
3. Click *Add* to add IPSec Policies and configure the required parameters.
    - Policy Name: Name the policy as desired. 
    - Remote Gateway: Enter the WAN IP of the Router in the Headquarter.
    - Local Subnet: Auto-filled the LAN segment of the local router.
    - Remote Subnet: Enter the LAN segment of the Router in the Headquarter.
    - Pre-shared key: Enter the encryption key set on the headquarter Router.

4. Set the Dead Peer Detection parameters as the same as the headquarter Router.
5. Click *Save & Apply*. 

Then, you can go confirm the connection between Headquarter Router and Branch Router.

!!! Note
    If one of the routers does not have a public IP address, for instance the Branch Router, but the Headquarter Router has a public IP address, you can: 
       
    - Set Branch Router in the Initiator Mode and change the Headquarter Router from Initiator Mode to Responder Mode.
    - Change the remote gateway on the Headquarter Router to be 0.0.0.0.

## Firmware

Router’s latest firmware will be released at the Cudy official website <a href="http://www.cudy.com">www.cudy.com</a>, and you can download it from <a href="http://www.cudy.com/download">www.cudy.com/download</a>. Please choose an appropriate update method and follow the instructions.

### Auto Update

The Router will automatically update firmware to the latest version at the specified time.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/auto-update.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1) Enable Auto Update.

2) Specify the *Update Time*. 

3) Click *Save & Apply*.

!!! Note
    - Backup your Router’s configurations before firmware update.
    - Do NOT turn off the Router during the firmware update.

### Online Update

If there is a new firmware available for the Router, a prompt will appear upon your login to the Router web management page. Click *Update Now* and then *Update* to upgrade the firmware to the latest version.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/online-update.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

If you miss the prompt, please go to General Settings -> Firmware -> Online Update and click *Check for update*. If there is one, click *Update* and wait a few minutes for the update and reboot to complete. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/online-update.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

### Local Update

Click *Browse...* to locate and upload the latest firmware file you’ve downloaded from <a href="http://www.cudy.com">www.cudy.com</a>. Wait a few minutes for the update and reboot to complete.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/local-update.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

!!! Note
    - *Local Update* is available for models M1200/M1300.
    - If you fail to update the firmware for the Router, please contact our <a href="mailto:support@cudy.com">technical support</a>.

### Satellite Update

The table will display the firmware versions for the satellite mesh units connected to this main mesh. You may update the firmware for the satellite mesh units on this page. Click *Check for updates* and click *Update* if a latest firmware is detected. Wait a few minutes for the update and reboot to complete.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/mesh_system/satellite-update.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

!!! Note
    - *Satellite Update* is available for models M1500/M3000/M3600/M6500/M11000/M21000.
    - If you fail to update the firmware for the Router, please contact our <a href="mailto:support@cudy.com">technical support</a>.