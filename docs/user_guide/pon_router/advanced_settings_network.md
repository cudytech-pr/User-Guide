# Advanced Settings - Network

The Network section allows you to configure various network features. Available options vary by operating mode. Wireless Router mode includes LAN, Guest Network, DHCP Server, IPv6, IGMP, IPTV/VLAN, QoS, Custom DNS, DDNS, Static Routing, Port Forwarding, Port Triggering, DMZ, Online Detection, TTL, Wake-on-LAN, and UPnP. Wireless Access Point mode includes LAN, DHCP Server, IGMP, and Wake-on-LAN.

## LAN

The router's default LAN IP address is 192.168.10.1, which you can use to access its web management page. The LAN IP address and subnet mask define the local network. You can change them to avoid IP conflicts or meet your network requirements.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-lan.webp" alt="" width="400px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Enter a new IP Address appropriate to your need. 
2. Set the Subnet Mask or keep it as default. 
3. Enable IP Routed Subnet as needed. If it is enabled, you need to enter the IP Address and Subnet Mask as well.
4. Click *Save & Apply*.
  
!!! Note
    - If you have set the Port Forwarding, DMZ or DHCP address reservation, and the new LAN IP address is not in the same subnet with the old one, then you should reconfigure these features.
    - If in conflicts with the WAN IP address, the LAN IP will automatically change into 10.1.1.1.

## DHCP Server

DHCP server is enabled by default and automatically assigns IP addresses and other network settings to connected devices. Do not disable it unless another DHCP server is available or you plan to configure network settings manually for each device.

### DHCP Settings

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/dhcp-settings.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- To specify the IP address that the Router assigns, you may configure settings here or go to *System Status > DHCP Server > More Details > DHCP Settings*. Please follow the steps below.
    1. Enable the DHCP Server.
    2. Enter the starting IP addresses and the Limit number to create the IP Address Pool.
    3. (Optional) Enter the DNS if the ISP offers. 
    4. Enter the Lease time.
    5. Click *Save & Apply*.

    !!! Note
        If you want to reserve for a specified client device an IP address, which is assigned by the router as a DHCP server, you may use the [IP/MAC binding](advanced_settings_security.md#ipmac-binding) function.

- To check the DHCP status —— if DHCP Server being *Enabled* or *Disabled*, its IP address and subnet mask, please go to *System Status > DHCP Server > More Details > Status*.
- To check the DHCP leases —— a list of clients which the Router being a DHCP server has allocated an IP address to, including such information as IP address, MAC address and Host name, please go to *System Status > DHCP Server > More Details > DHCP Leases*.

## IPv6

IPv6 support may be limited in some features, such as Firewall, VPN, and Block List. This page allows you to configure IPv6 Internet connections. Seven connection types are available: Relay, Dynamic IP (SLAAC/DHCPv6), Static IP, Passthrough, 464XLAT, MAP-E, and DS-Lite. Select the type supported by your ISP and configure the required settings.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/ipv6.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

!!! Note
    - If the current version of the firewall (or VPN, block list, and etc.) does not support IPv6, you may enable and configure the IPv6 function on this page.
    - If you use VPN and IPv6 functions at the same time, it's likely to cause IPv6 data leakage.

### Relay
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/ipv6-relay.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

Relay is typically used for IPv6 transition mechanisms. The router will act as a relay between your local IPv6 network and an IPv4-based upstream network provided by your ISP. 

Select *Relay* and just click *Save & Apply* without any additional configuration.

### Dynamic IP(SLAAC/DHCPv6) 
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/ipv6-dhcp.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

Select *Dynamic IP(SLAAC/DHCPv6)*, and configure MAC Clone and MTU as needed.Then click *Save & Apply*.

- MAC Clone: (Optional) Enter the MAC address of the device that is allowed by your ISP. You can usually find this in the device's network settings or on a label on the device.
- MTU: Enter the appropriate MTU size (commonly 1500 bytes for compatibility with IPv4). 

### Static(Fixed lP)
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/ipv6-static.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

Select *Static (Fixed IP)* and enter the fixed IPv6 address, gateway, prefix and DNS server address provided by your ISP. Then click *Save & Apply*.

- MAC Clone: (Optional) Enter the MAC address of the device if the ISP requires a specific MAC address for the static IP assignment. You can usually find this in the device's network settings or on a label on the device.
- MTU: Enter the appropriate MTU size based on the network's physical layer, typically 1500 bytes for Ethernet.

### Passthrough
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/ipv6-passthrough.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

Passthrough allows an IPv6-enabled device to manage its own IP settings directly from the ISP, bypassing the router's DHCP server. 

Select *Passthrough* and just click *Save & Apply* without any additional configuration.

### 464XLAT
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/ipv6-464xlat.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

464XLAT is a stateless translation mechanism that allows IPv4-only devices to communicate over an IPv6 network. 

Select *464XLAT* and just click *Save & Apply* without any additional configuration.

### MAP-E
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/ipv6-mape.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

MAP-E (Mapping of Address and Port with Encapsulation) is a method for translating IPv6 addresses to IPv4 addresses. 

Select *MAP-E*, and configure MAC Clone and MTU as needed. Then click *Save & Apply*.

- MAC Clone: (Optional) MAP-E usually does not involve MAC address restrictions, so MAC Clone is not typically necessary.
- MTU: Enter the appropriate MTU size according to the maximum IPv4 packet size, which is typically 1500 bytes minus the headers.

### DS-Lite
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/ipv6-dslite.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

DS-Lite (Dual-Stack Lite) is a technology that allows ISPs to provide IPv4 service over an IPv6 network. 

Select *DS-Lite*, and configure MAC Clone and MTU as needed. Then click *Save & Apply*.

- MAC Clone: (Optional) DS-Lite usually does not involve MAC address restrictions, so MAC Clone is not typically necessary.
- MTU: Enter the MTU value based on your network's requirements. The value should be within the range of 1280 to 1582 bytes. The MTU setting is important to ensure that the encapsulated IPv4 packets can be transmitted over the IPv6 network without fragmentation. 

## IGMP

Useful in home network to manage and optimize multicast traffic, reduce network load, and enhance network security and efficiency, for instance, you would like to enjoy streaming video content or using IPTV services.

If your ISP provides the networking service based on IGMP technology (e.g.British Telecom(BT) and Talk Talk in UK), please enable IGMP Snooping and IGMP Proxy, then select the IGMP Version (No enforcement / Enforce IGMPv1 / Enforce IGMPv2 / Enforce IGMPv3. as required by your ISP. Then click *Save & Apply*. 

With IGMP proxy configured, IPTV can work under your router now. Then connect your set-top box to any of the router’s Ethernet port, and configure it. All these done, you may enjoy IPTV now.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-igmp.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

- No enforcement: It supports all three IGMP version: Enforce IGMPv1/v2/v3. You can select this option if not sure about the exact one.
- Enforce IGMPv1: In this version, the router provides basic multicast group membership reporting, sufficient for simple home networks where multicast traffic is not heavily utilized .
- Enforce IGMPv2: In this version, the router offers an improvement over IGMPv1 by allowing hosts to send 'leave' messages, thus to improve the efficiency of multicast traffic management in home networks with dynamic multicast group memberships .
- Enforce IGMPv3: In this most advanced version, the router supports source-specific multicast (SSM), allowing for more granular control over multicast traffic. This can be beneficial in home networks where users may want to receive multicast streams from specific sources only .

## Custom DNS
If you set custom DNS servers, any DNS name will be resolved through the DNS Servers set here instead of the one obtained from WAN.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-custom-dns.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

- Rebind protection: This function may cause private DNS lookup failure. Do not enable it if your network has a captive portal.
- Override All Clients' DNS: If Enabled, your router will bypass hard-coded DNS settings on all clients, such as Chrome cast, TV boxes, etc.
- DNS Settings: Select Default to use the gateway of the parent router, or Manual to set the DNS server manually with Preferred/Alternate DNS.

## DDNS
Dynamic DNS (DDNS) maps a domain name to your router's changing public IP address, allowing you to remotely access your router and local servers (such as FTP and HTTP servers) without having to track its IP address.

!!! Note
    DDNS would not work if the ISP assigns a private WAN IP address (e.g. 192.168.1.x) to the router.  

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-ddns.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**To set up DDNS, please follow the steps below.**

1. Enable DDNS.
2. Select the DDNS Service Provider. It is recommended to select no-ip.com or dyn.com. If you don’t have a DDNS account, you have to register first.
3. Enter the Domain / Username / Password of your account.
4. Set the Check Interval and Force Interval.
5. Click *Save & Apply*.

## Static Routing

Allows you to manually add routing entries to the router's routing table, specifying how data packets are forwarded to their destination networks.

For example, if you want your PC to access the Internet through Router A while also accessing your company's local network through Router B, you can configure static routing as shown in the following network diagram. Follow the steps below to configure static routing.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/static-routing.webp" alt="" width="800px"/>

1. Disable Router B’s DHCP function. Change the routers’ LAN IP addresses to two different IP addresses on the same subnet. 
2. Log in to Router A’s management web page *http://cudy.net*, and go to Advanced Settings -> Network -> Static Routing.
3. Click Add, and enter the parameters as required.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/static-routing2.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

    - Interface: Select the type of port (WAN or LAN)  that sends out data packets to the gateway.
    - Target: Enter the Host-IP or Network IP address you want to assign to a static route. This IP address cannot be on the same subnet with the WAN IP or LAN IP of Router A.
    - Subnet Mask: If the destination is a single IP address, enter 255.255.255.255; otherwise, enter the subnet mask of the corresponding network IP. (It is required if the Target is a network. It determines the destination network with the destination IP address. ) 
    - Gateway: The IP address of the gateway device which the data packets will be sent to. This IP address must be on the same subnet with the router’s IP which sends out data. 

4. Click *Save & Apply*.

!!! Success
    Congratulations! Now you can open a web browser on your PC, enter the company server’s  IP address to visit the company network.

## Port Forwards

Allows Internet users to access specific services on devices in your local network, such as web (HTTP), FTP, and email servers, while keeping other services inaccessible from the Internet.

Each service uses a specific port number. For example, HTTP uses port 80, FTP uses port 21, SMTP uses port 25, and POP3 uses port 110. Make sure you know the correct port number before configuring port forwarding.

For example, to allow your friends to access a website hosted on your PC (192.168.10.100) through your router's WAN IP address (218.18.232.154), follow the steps below.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-port-forwards.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Assign a static IP address to your PC, for example 192.168.10.100.

2. Log in to *http://cudy.net*, and go to Advanced Settings -> Network -> Port Forwards.

3. Click Add, and enter the required parameters.
    - Name: Give a name for the entry.
    - Protocol: Select TCP or UDP, or TCP+UDP if you are unsure of which protocol you are using. TCP is usually used for web browsing, file transfers, and most client-server applications, while UDP for streaming services, online gaming, and other applications that require fast transmission of data.
    - Interface: Select WAN or VPN according to the source of traffic you want to forward.
    - External Port: Specify the port number that will receive traffic on the WAN or VPN interface.
    - Internal IP Address: Enter the IP address of the device on your local network that should receive the forwarded traffic.
    - Internal Port: Specify the port number on the internal device that will receive the forwarded traffic.
    - Delete: Delete the entry as needed.
    
    If you want to provide several services in a router, please add multiple port forwarding rules.

4. Click *Save & Apply*. 

!!! Success
    Users on the Internet can enter *http://WAN IP* (in this example: *http://218.18.232.154*) to visit your personal website.

!!! Note
    - The WAN IP should be a public IP address. For the WAN IP is assigned dynamically by the ISP, it is recommended to apply and register a domain name for the WAN. Then users on the Internet can use *http://domain name* to visit the website.
    - If you have changed the default External Port, you should use *http://WAN IP:external port* or *http://domain name:external port* to visit the website.

## Port Trigger

Dynamically opens specified external ports when a device on your local network initiates a connection through a designated triggering port. The router records the device's IP address and forwards incoming traffic on the opened ports to that device. This feature is commonly used by online games, VoIP applications, and multimedia applications.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-port-trigger.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**To configure the Port Trigger rules, please follow the steps below.**

1. Click *Add*, and enter the required parameters.You can add multiple port trigger entries as needed.

    - Name: Set a name for the entry.
    - Trigger Protocol: Select TCP or UDP based on the application's requirements, or TCP+UDP if you are unsure of which protocol you are using .This is the protocol that will be used for the trigger port. 
    - Trigger Port: Enter the trigger port range that the application uses to initiate connections. The trigger ports can not be overlapped.
    - External Protocol: Select the identical protocol as trigger port to ensure that the traffic is forwarded correctly. 
    - External Port: Enter the external port identical with the inbound port that the application expects to receive traffic and forward it to the internal device. You should verify the external ports the application uses first and enter them into External Port field in the format required. 
    - Delete: To delete the entries as needed.

2. Click *Save & Apply*. 

## DMZ

A DMZ host is a device on your local network with all ports exposed to the Internet, allowing unrestricted communication with external devices. You can use this feature when an application, such as an IP camera or database software, requires multiple ports that are difficult to configure individually.

!!! Note
    Due to the total exposure of DMZ host to the Internet, it will bring about certain potential safety hazards. So remember to dis-enable DMZ when not in use.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-dmz.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

For example, you want to get the home PC to join an online game without port restriction.You can set your PC as a DMZ host with all ports open. Please follow the steps below to configure it.

1. Assign a static IP address to your PC, for example 192.168.10.100.
2. Log in to *http://cudy.net*, and go to Advanced Settings -> Network -> DMZ.
3. Enable DMZ, and enter the PC’s IP address 192.168.10.100 manually in the (DMZ Host) IP 	Address field.
4. Click *Save & Apply*.

!!! Success
    Congratulations! You’ve set your PC to a DMZ host and now you can make a team to game with other players.

## Online Detection

Essential for ensuring that your network remains online and operational even if there are issues with the primary WAN connection. It allows for automatic failover to a backup connection, which can be critical for businesses and homes that require continuous Internet access.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-online-detection.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**To configure the online detection, please follow the steps below.**

1. Enable Online Detection.
2. Select the Target Host, either Default or Manual as needed.
3. Enter the Host, either a public DNS server like Google's 8.8.8.8 or any other reliable server that is expected to be always online, in order to check the online status of the WAN port. 
4. Enter the Period, that is the timeout seconds when no Ping replies received and network restarted.
5. Enter the Ping Period, that is the interval between which the Ping is sent in seconds.
6. Select the Protocol, either TCP or ICMP as needed. If TCP is selected, you also need to enter the Port value.
7. Click *Save & Apply*.

## TTL
TTL (Time To Live) sets the maximum time for packets to survive in the network, and is filled in according to the requirements of the operator. By default, the router forwards the TTL of the incoming client device minus one. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-ttl.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

- Disabled: Select it if you do not need to modify TTL values for any specific reason.
- Extend the TTL Value: Select it if you need to increase the TTL of incoming packets.
- Spoof LAN TTL Value: Select it if you want to override outgoing packets' TTL to the router's default value.
- Custom: Select Custom, and enter the specific IPv4 TTL value as needed (e.g., 65).

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-ttl2.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

## Wake on LAN

Wake-on-LAN (WoL) allows you to remotely wake up a computer by sending a network message to it.

To use this feature, both the computer's motherboard and wired network adapter must support WoL. Follow the steps below to configure it.

**STEP 1: Finish your computer settings before configuring the WoL function on the router.**

1. Enter BIOS when starting up the computer. Then enable Resume by PCI Device and Resume by PCI-E Device. Usually this option is in power management menu.
2. Turn on the computer and go to Control Panel -> Network and Internet -> Network and Sharing Center -> Local area connection -> Properties -> Configure -> Advanced. Then enable Shutdown Wake-On-Lan, Wake on Magic Packet and Wake on pattern match.
3. Check MAC address of the computer that applies Wake-on-LAN. 

**STEP 2: Go to configure the router then.**

1. Login in to *http://cudy.net* with the password you’ve created and go to Advanced Settings -> Network -> Wake on LAN.
2. Click *Add*.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-wol.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

3. Enter the MAC-Address you have checked previously in STEP 1.3, give a description for the device, and determine the time duration (Min and Hour) and day frequency (Week Day).
Delete the entries if needed.
4. Click *Save & Apply*.

## UPnP

Universal Plug and Play (UPnP) allows applications and devices on your local network to automatically open the ports they need on the router for communication over the Internet.

Enable UPnP for applications that require incoming connections, such as online games, peer-to-peer applications, VoIP, and remote assistance. For example, UPnP allows an Xbox to automatically open the required ports for online gaming.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-upnp.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

!!! Note
    - UPnP is enabled by default in this router.
    - Only the application supporting UPnP protocol can use this feature.
    - UPnP feature needs the support of operating system (e.g.Windows Vista/ Windows 7/Windows 8, and etc. Some operating systems need to install the UPnP components).

## USB Sharing

The router supports to share files and data via USB storage device. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/pon_router/usb_sharing.webp" alt="" width="600px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Toggle on *Enable*.
2. Note down the access link appropriate for your operating system.
3. Keep note of the default username *admin* and your newly-set password for the access to the USB storage.
4. Toggle on *Read-only* if necessary. When enabled, users can only view or download files from the USB storage. Uploading, deleting, or modifying files is not allowed.

## VoIP Basic Settings 

*VoIP Basic Settings* allows you to configure SIP server information, proxy settings, and telephone line accounts to enable VoIP services through your router.

1. Select the Region where the VoIP service is used.
2. Enter the SIP server and proxy information provided by your VoIP service provider.
3. Specify the number of VoIP lines and enable the required line(s).
4. Enter the telephone number and SIP account information for each enabled line.
5. Click *Save & Apply* to save and apply the settings.

!!! Note 
    Obtain the SIP server addresses, port numbers, telephone number, and account credentials from your VoIP service provider. Available settings may vary depending on your provider.

## VoIP Advanced Settings 

*VoIP Advanced Settings* provides additional options for customizing SIP communication, voice transmission, and call behavior. These settings are generally intended for advanced users or specific VoIP service requirements. In most cases, the default settings are sufficient. Modify them only when required by your VoIP service provider or when troubleshooting VoIP issues.

1. Modify the required parameters according to your VoIP service provider's instructions.
2. Click *Save & Apply* to save and apply the settings.

!!! Note
    Incorrect advanced settings may affect VoIP registration or call quality. If you are unsure about a parameter, keep its default value or contact your VoIP service provider.

## WAN Mode

*WAN Mode* allows you to select the network access technology used by the router. Choose GPON or EPON for fiber-optic PON connections, or ETH for Ethernet WAN connections, according to your ISP's service.

1. Select the required mode: GPON, EPON, or ETH.
2. Click *Save & Apply* to apply the settings.
3. Configure the corresponding WAN settings according to your ISP's requirements.
    - GPON Mode: Configure PON authentication credentials if required by your ISP. Configure PON WAN parameters according to your ISP's requirements.
    - EPON Mode: Configure the authentication parameters if required by your ISP. Configure WAN parameters according to your ISP's requirements.
    - ETH Mode: Connect the upstream Ethernet cable to the designated Ethernet WAN port. Configure the WAN connection type (DHCP, Static IP, or PPPoE) according to your ISP's requirements.

!!! Note
    Changing the WAN mode may interrupt your Internet connection. Make sure the selected mode matches your ISP's network and the router's hardware configuration before applying the change.

## Captive Portal

*Captive Portal* allows you to design a portal page for network access verification. Customers are directed to view an advertisement or accept set terms before being granted Internet access. In this way, it offers unique marketing opportunities for small businesses to improve brand awareness and deliver marketing messages. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/pon_router/captive_portal.webp" alt="" width="1000px" style="border: 1px solid #eee;" />

1. Enable *Captive Portal*. 
2. Select *Interface* for portal authentication. Recommend to select both.
3. Enter your *Local Network* address. Recommend to keep it as default.
4. (Optional) Enter the *Captive Portal URL*. Newly connected clients will be redirected to this specified URL. This could be a welcome page, terms of use, or any other relevant information you want them to see.
5. Select the *<span class="tooltip-term" data-tooltip="Cudy Router comes embedded with six captive portal providers (HotspotSystem, Iron Wi-Fi, ObiFi, VulaCoin, WorldSpot.net, WiFiMAX). The setup process is quite simple. After creating an account with the listed providers, users can input the configuration value to enable the captive portal. Please follow the steps to configure it.">Profile</span>* and enter the corresponding parameters. 
    - For Profile HotspotSystem/Iron Wi-Fi/WorldSpot.net/ObiFi/VulaCoin, Lease time is required. It is an authentication timeout when a client has to reconnect to the network.
    - For Profile WiFiMAX, UAM Server address or hostname and Lease time are required.
    - For Profile Manual, UAM Server address, Preferred DNS, and Lease time are required.
6. Click *Save & Apply*.

!!! Note
    The third-party Captive Portal solutions may have varying levels of compatibility and security risks, which may require additional configuration and troubleshooting.