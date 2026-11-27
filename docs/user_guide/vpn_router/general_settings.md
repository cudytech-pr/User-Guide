# General Settings 

## WAN Mode

R700 supports connecting to the internet via ethernet cable. Please connect the WAN port of R700 to the LAN port of ONT, Modem or the main router.  

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/general_settings_wan_mode.webp" alt="" width="800px" style="border: 1px solid #eee;" />

Configure the number of WAN ports. When a WAN port is added, the port-related entries are automatically added in WAN Settings page. When a WAN port is deleted, the port-related entries are automatically deleted. Any change to the number of WAN ports may lead your current configurations to be lost. Make sure you have backed up your configurations before proceeding.

Any change needs to click *Save & Apply*.

!!! Note
    The three WAN/LAN ports are LAN status by default. You can change them to WAN status here, and then you can set the *WAN2* connection on the *WAN Settings* page.

## WAN Settings

*WAN Settings* is to set your Internet connection. Select your Internet connection type from the drop-down list of Protocol. Follow the instructions on the page to continue the configuration. Parameters on the figures are just used for demonstration.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/general_settings_wan_settings.webp" alt="" width="800px" style="border: 1px solid #eee;" />

### DHCP

DHCP is the default and most common protocol. It is a network management protocol used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client–server architecture.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/wan_settings_dhcp.webp" alt="" width="800px" style="border: 1px solid #eee;" />

If you choose *DHCP*, keep MTU as default unless your ISP provides differently. The *Hostname* and MAC address Clone are optional. Then *Save & Apply* your configurations.

- MAC Clone: If your broadband ISP binds the MAC address, you can enter the bound MAC address here..
- MTU: The default value is 1500.

### PPPoE

PPPoE is required by many Internet Service Providers (ISP). Generally, your ISP will give you a modem and provide you a username & password that you needed when you are creating the Internet connection.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/wan_settings_pppoe.webp" alt="" width="800px" style="border: 1px solid #eee;" />

If you choose *PPPoE*, enter the Username and Password provided by your ISP. Then *Save & Apply* your configurations.

- Access Concentrator: If you broadband ISP need you to input this, you can enter the Access Concentrator name here.
- Service Name: If your broadband ISP binds the Service Name, you can enter the Service Name here. 
- MAC Clone: If your broadband ISP binds the MAC address, you can enter the bound MAC address here.
- MTU: The default value is 1500.

### Static (Fixed IP)

Static is required if your Internet Service Provider (ISP) has provided a fixed IP address for you or you want to configure the network information such as IP address, Gateway, Netmask manually.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/wan_settings_staticip.webp" alt="" width="800px" style="border: 1px solid #eee;" />

If you choose *Static (Fixed IP)*, enter the parameters provided by your ISP, including IP Address / Subnet Mask / Default Gateway / Preferred DNS. Keep MTU as default unless your ISP provides differently. Then *Save & Apply* your configurations.

- MAC Clone: If your broadband ISP binds the MAC address, you can enter the bound MAC address here..
- MTU: The default value is 1500.

## Load balancing 

It is the load distribution of network traffic across multiple back-end servers. It needs a minimum of two WAN interfaces to work effectively.

### Interface

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images//vpn_router/general_settings_load_balancing.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- Interface: For each WAN interface configure an interface section and define how each WAN interface is tested for up/down status. Each interface section must have a name that corresponds with the interface name in WAN Settings.  
- Tracking reliability: Number of track_ip hosts that must reply for the test to be considered as successful. Ensure there are at least this many track_ip hosts defined or the interface will always  
be considered down. 
- Ping interval: The WAN interface will detect the connection with the Internet through ping packets. This parameter sets the time interval for sending ping packets. The default is 10 seconds.
- Interface down: When multiple ping detection packets fail continuously and reach the set threshold, the WAN port will be turned offline. The default threshold is 5 ping packets.
- Interface up: When multiple ping detection packets success continuously and reach the set threshold, the WAN port will be turned online. The default threshold is 1 ping packets.
- Edit: If you want to edit all the parameters of the WAN interface, you can click it.

### Member

Each member represents an interface with a metric and a weight value. Members are referenced in policies to define a pool of interfaces with corresponding metric and load-balancing weight. Members can't be used for rules directly.  

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images//vpn_router/general_settings_load_balancing_member.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- Name: The name of this member configuration, which is then referenced in policies. (eg. WAN1_M1_W3 means metric 1, weight 3 for WAN 1).
- Interface: Member applies to this interface.  
- Metric: Define the priority of the route. A smaller value means a higher priority.  
- Weight: Members with same metric will distribute load based on the weight value. 
- Edit: If you want to edit all the parameters of the WAN interface, you can click it.

### Policy

Policies define how traffic is routed through the different WAN interface(s). Every policy has to have one or more members assigned to it, which defines the policy's traffic behavior. If a policy has a single member, traffic will only go out of that member. If a policy has more than one member, it will either load-balance among members or use one member but fail-over to another, depending on how the members are configured.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images//vpn_router/general_settings_load_balancing_policy.png" alt="" width="800px" style="border: 1px solid #eee;" />

- Name: Unique name for the policy.  
- Member Used: One or more members assigned to this policy.  
- Last resort: Determine the fallback routing behavior if all WAN members in the policy are down. 
- Edit: If you want to edit all the policies, you can click it.

!!! Note
     - Member interfaces with lower metrics are used first. 
    - Member interfaces with the same metric will be load-balanced. 
    - Load-balancing members (with same metric) will distribute load based on assigned weights values. 
    - The policy has one member and traffic will only go out of that member. 

### Rule

Rules specify which traffic will use a particular policy. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images//vpn_router/general_settings_load_balancing_rule.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- Name: The unique name of the rule.  
- Source address: Match traffic from the specified source IP address.  
- Source port: Match traffic from the specified source port or port range.  
- Destination address: Match traffic directed to the specified destination IP address.  
- Destination port: Match traffic directed at the given destination port or port range.  
- Sticky: Allow traffic from the same source IP address within the timeout limit to use same wan interface as prior session.  
- Policy assigned: Choose policy that wants to be applied. 
- Edit: If you want to edit all the rules, you can click it.

!!! Note
    - Rules are based on IP address, port or protocol.  
    - Rules are matched from top to bottom.  
    - Rules below a matching rule are ignored. 

## VPN

**VPN (Virtual Private Network)** helps you access Internet resources remotely, securely, and privately through tunneling technology. When you access the Internet, VPN encrypts your personal information and hides your IP address from the public. For VPN users, it looks like the devices are directly connected. Cudy Router supports 6 types of VPN connections: PPTP, L2TP, OpenVPN, WireGuard, ZeroTier, IPSec (site-to-site). Please choose an appropriate VPN according to your needs and circumstances.

!!! Note
    Before you enable VPN Server, it is recommended to configure Dynamic DNS Service or assign a Static IP Address for router's WAN port and synchronize your System Time with Internet. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_topology.webp" alt="" width="800px" style="display: block; margin: 0 auto;" />

### PPTP VPN

PPTP VPN is used to create a PPTP VPN connection for remote devices to access your home network. Fast connection/disconnection and simple configuration satisfy the needs for users who is apt to frequently switch VPN environments. Please follow the steps below to set up a PPTP VPN connection.

**STEP 1. Configure the PPTP Server on Router A:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_pptp_server.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Router A's management web page [https://cudy.net](https://cudy.net) (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select PPTP Server as Protocol. 
3. Select Client Access (Internet and Local Network/Internet/Local Network).
4. Configure the PPTP Server.
    - MPPE Encryption: Enable to encrypt the data transmitted via PPTP VPN, thus improve the communication security.
    - Server IP/IP Start/Limit: Set to assign IP address for the VPN Clients.
    - Username/Password: Set for the VPN client to access the VPN Server.

5. Click *Save & Apply*.	

**STEP 2. Configure PPTP Client on Router B:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_pptp_client.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Router A's management web page https://cudy.net (or 192.168.10.1). 
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

**STEP 1. Configure the L2TP Server on Router A:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_l2tp_server.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Router A's management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select L2TP Server as Protocol. 
3. Select Client Access (Internet and Local Network/Internet/Local Network).
4. Configure the L2TP Server.
    - Server IP/IP Start/Limit: Set to assign IP address for the VPN Clients.
    - Tunnel Secret (Optional): To set a L2TP VPN encryption as needed.
    - Pre-shared Key (Optional): To set a IPSec encryption as needed.
    - MTU: Maximum Transmission Unit is 1400 by default. You may change it if necessary.
    - Username/Password: Set to authenticate the VPN clients to access the VPN Server.

5. Click *Save & Apply*.

**STEP 2. Configure L2TP Client on Router B:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_l2tp_client.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Router A's management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select L2TP Client as Protocol. 
3. Select Allow all devices or Ban all devices as Default Rule.
4. Enable Site-to-Site to allow communication between VPN server and Clients.
5. Select VPN Policy. 
    - Disable: VPN Policy is disabled. No restriction.
    - VPN kill switch: Internet access will be disconnected upon VPN disconnection. It is highly recommended for users who transmit data all through VPN. Preferred (and optionally Alternate DNS) is required. 
    - Domain: Select and configure to allow specified domain(s) to transmit data through VPN or not. DNS and Domain are required.
    - Remote Subnet: Select and configure to allow devices with the specified subnet to transmit data through VPN. IP address and Subnet mask are required.

6. Configure the L2TP Client:
    - Server Address/ Username/Password: Enter the parameters provided by the L2TP Server.
    - Local Hostname: Customize or keep it as default.
    - Tunnel Secret / Pre-shared Key: Enter the encryption if the L2TP Server has set it.
    - MTU: Maximum Transmission Unit is 1400 by default, you may change it if necessary.
    - Use custom tunnel IP: Enable and enter it if the L2TP Server provides a tunnel IP bound with the account.

7. Click *Save & Apply*.

### OpenVPN

**OpenVPN Server** is used to create an OpenVPN connection for remote devices to access your home network. OpenVPN server requires a public IP. You can confirm whether the router has a public IP on the router management page System Status -> WAN -> More details -> Status. If the public IP displayed is consistent with the IP address of the router's WAN port, it means that the router has a public IP. Please follow the steps below to set up an OpenVPN connection.

**STEP 1. Configure the OpenVPN Server on Router A:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_openvpn_server.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Router A's management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select OpenVPN Server as Protocol. 
3. Select the Client Access (Internet and Local Network / Internet / Local Network).
4. Configure the OpenVPN Server.
    - OpenVPN Protocol: Select UDP or TCP as desired.
    - Service Port: 1194 by default, keep it or change it as needed.
    - VPN Subnet: Set up a VPN subnet segment.
    - Subnet Mask: Select or customize as needed.

5. Click *Save & Apply*.
6. Click EXPORT to export the configuration file, for the OpenVPN Client to upload.

**STEP 2. Configure OpenVPN Client on Router B:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_openvpn_client.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Router A's management web page https://cudy.net (or 192.168.10.1). 
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

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_wireguard_server.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**STEP 1. Configure the WireGuard Server on Router A:**

1. Log into the Router A's management web page https://cudy.net (or 192.168.10.1).
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
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/client-export.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**STEP 2. Configure WireGuard Client on Router B:**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_wireguard_client.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Router A's management web page https://cudy.net (or 192.168.10.1).
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
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

2. Click Network - > Create A Network. 
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier2.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

3. Zerotier will create a new network and assign a NETWORK ID for you. Then click on the assigned NETWORK ID, and its setting page will display.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier3.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

4. Set Access Control to be Public for later convenient settings, and note down the Network ID.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier4.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

!!! Note
    Private Access Control requires authorization for the terminal or router to access the network, which is more secure but inconvenient. While Public Access Control allows for a direct the network access with authentication rather than authorization. You may choose either one accordingly.

**STEP 2. Configure ZeroTier Master on Router A.**
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_zerotier_master.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Log into the Router A's management web page https://cudy.net (or 192.168.10.1). 
2. Go to General Settings ->VPN. Enable VPN, and select ZeroTier Master as Protocol. 
3. Select Client Access (Internet and Local Network/Internet/Local Network).
4. Enter the ZeroTier Network ID noted down previously.
5. Click *Save & Apply*. Then it will display the Device ID.
6. Back to the ZeroTier web page, you will see One device has joined this network.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier5.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />


**STEP 3. Join ZeroTier Network on your device.**

1. Download and Install ZeroTier Software from https://www.zerotier.com/download/.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier6.webp" alt="" width="400px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

2. Click the ZeroTier icon and then Join New Network..., enter the Network ID and click Join.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier7.webp" alt="" width="400px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

3. Back to the ZeroTier web page, you will see this new device and its Managed IP.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier8.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**STEP 4. Configure the Static Route.**

Go to Settings -> Advanced on the ZeroTier web page. Under Add Routes, enter Router's LAN IP segment 192.168.10.0/24 in Destination field and its Managed IP in Via field, and then click Submit.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/zerotier9.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

Now your client devices can directly access the router's management web page via 192.168.10.1 as well as the server via its IP address.

### IPSec (site-to-site) VPN

**IPSec (site-to-site) VPN** is a secure tunneling protocol used to connect two different networks, typically a corporate network and a remote branch office network, over the Internet. It allows multiple users at the remote site to access resources on the main office network as if they were directly connected to it. Please follow the steps below to set up an IPSec (site-to-site) VPN connection.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/vpn_ipsec.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**STEP 1. Get both Routers in the Headquarter and Branch Office ready.**

1. Make sure both Routers are connected to the Internet, but two network can not be in the same LAN segment. 
For example, if the headquarter is in the LAN segment 192.168.10.0/24, then the branches should be in a different LAN segment, say, 192.168.20.0/24.
2. Check and note down the WAN and LAN IP addresses of the Headquarter Router and Branch Office Router on their management Status page. WAN IP of the headquarters router is the remote gateway of the branch offices, and its LAN IP is the remote subnet of the branch offices; and vice versa.

**STEP 2: Configure the IPSec VPN on the Router in the Headquarter.**

1. Log into the  Router A's management web page https://cudy.net (or 192.168.10.1). 
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

1. Log into the  Router A's management web page https://cudy.net (or 192.168.10.1). 
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

