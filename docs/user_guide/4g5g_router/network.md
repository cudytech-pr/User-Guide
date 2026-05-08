# Network

Network section allows you to manage and configure a series of network features for the router. In Wireless Router mode, it includes LAN, guest network, DHCP server, IPv6, IGMP, IPTV/VLAN, QoS, Custom DNS, DDNS, Static Routing, Port Forwards, Port Trigger, DMZ, Online detection, TTL, Wake on LAN, and UPnP; while in Wireless Access Point mode, it consists of LAN, DHCP server, IGMP and Wake on LAN. 

!!! Note
    P2 is used as an example in this guide. Refer to your actual product for more details.
    
---

## LAN/WAN Switch
Converts the LAN/WAN port between local network switching (LAN mode) and wide-area routing (WAN mode), enabling flexible topology adaptation in the networks.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/lan-wan-switch.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

- *Current Status*: Displays the current working mode of the WAN/LAN port.
- *LAN/WAN Switch*: Click *Switch to LAN* to change working mode from WAN to LAN; or click *Switch to WAN* to change it from LAN to WAN.

!!! Note
    This feature is not available for all models. Please refer to your model and management page.

---

## LAN
The router is preset with a default LAN IP 192.168.10.1, which you can use to log in to its web management page. The LAN IP address together with the Subnet Mask also defines the subnet that the connected devices are on. If the IP address conflicts with another device on your local network or your network requires a specific IP subnet, you can change it.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-lan.webp" alt="" width="400px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Enter a new IP Address appropriate to your need. 
2. Set the Subnet Mask or keep it as default. 
3. Enable IP Routed Subnet as needed. If it is enabled, you need to enter the IP Address and Subnet Mask as well.
4. Click *Save & Apply*.
  
!!! Note
    - If you have set the Port Forwarding, DMZ or DHCP address reservation, and the new LAN IP address is not in the same subnet with the old one, then you should reconfigure these features.
    - If in conflicts with the WAN IP address, the LAN IP will automatically change into 10.1.1.1.

---
## Guest Network
Guest Network allows you to provide Wi-Fi access for guests without disclosing your main network. When you have guests in your house, apartment, or workplace, you can create a guest network for them. In addition, you can customize guest network options to ensure network security and privacy. Please follow the steps below to set up a guest network.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-2.4g.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**To set up a guest network, please follow the steps below.**

1. Enable 2.4G/5G Guest Network.
2. Customize the SSID. Don’t enable Hidden Network unless you want your guests to manually input the SSID for guest network access.
3. Select your Encryption type and customize your own Password.
4. Enable Access Filter. If enabled, the firewall-related functions (such as MAC filter, IP filter, and domain filter, parental control, etc.) will take effect on clients connected to the guest network.
5. Click *Save & Apply*. 

Now your guests can access your guest network using the SSID and password you set.

---
## DHCP Server

Router acts as a DHCP (Dynamic Host Configuration Protocol) server, which is enabled by default. It dynamically assigns TCP/IP parameters to client devices from the IP Address Pool. DO NOT disable DHCP server unless you have another DHCP server, or you want to manually assign the TCP/IP parameters to every client device on the network. 

- Go to *Advanced Settings -> Network -> DHCP Server* or *System Status -> DHCP Server -> More Details -> Settings*, and follow the steps below to specify the IP address that the Router assigns.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/dhcp-settings.webp" alt="" width="800px" style="border: 1px solid #eee;" />

    1. Enable the DHCP Server.
    2. Enter the starting IP addresses and the Limit number to create the IP Address Pool.
    3. (Optional) Enter the DNS if the ISP offers. 
    4. Enter the Lease time.
    5. Click *Save & Apply*.

    !!! Note
        If you want to reserve for a specified client device an IP address, which is assigned by the router as a DHCP server, you may use the [IP/MAC binding](security.md#ipmac-binding) function.

- Go to *System Status -> DHCP Server -> More Details -> Status* to see it is *Enabled* or *Disabled* as well as its IP address and subnet mask. Click *More Details* to know more information about it or make changes on Settings page. 
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/dhcp-status.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- Go to *System Status -> DHCP Server -> More Details -> DHCP Leases* to view the list of clients which the Router being a DHCP server has allocated an IP address to, including such information as IP address, MAC address and Host name.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/dhcp-lease.webp" alt="" width="800px" style="border: 1px solid #eee;" />

---
## IPv6
IPv6 may not be supported in the current version of the firewall, VPN, block list, etc.Therefore, the IPv6 function can only be used for configuration on this interface. There are 7 types of  IPv6 Internet connection, including Relay, Dynamic IP(SLAAC/DHCPv6), Static (Fixed lP), Passthrough, 464XLAT, MAP-E, and DS-Lite. Please choose the appropriate one and configure the parameters according to your ISP.

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

### Static(Fixed lP): 
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

---
## IGMP
is useful in home network to manage and optimize multicast traffic, reduce network load, and enhance network security and efficiency, for instance, you would like to enjoy streaming video content or using IPTV services.

If your ISP provides the networking service based on IGMP technology (e.g.British Telecom(BT) and Talk Talk in UK), please enable IGMP Snooping and IGMP Proxy, then select the IGMP Version (No enforcement / Enforce IGMPv1 / Enforce IGMPv2 / Enforce IGMPv3. as required by your ISP. Then click *Save & Apply*. 

With IGMP proxy configured, IPTV can work under your router now. Then connect your set-top box to any of the router’s Ethernet port, and configure it. All these done, you may enjoy IPTV now.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-igmp.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

- No enforcement: It supports all three IGMP version: Enforce IGMPv1/v2/v3. You can select this option if not sure about the exact one.
- Enforce IGMPv1: In this version, the router provides basic multicast group membership reporting, sufficient for simple home networks where multicast traffic is not heavily utilized .
- Enforce IGMPv2: In this version, the router offers an improvement over IGMPv1 by allowing hosts to send 'leave' messages, thus to improve the efficiency of multicast traffic management in home networks with dynamic multicast group memberships .
- Enforce IGMPv3: In this most advanced version, the router supports source-specific multicast (SSM), allowing for more granular control over multicast traffic. This can be beneficial in home networks where users may want to receive multicast streams from specific sources only .

---
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

---
## QoS
QoS (Quality of Service) allows you to prioritize connection of specific devices for a set duration. Devices set as high priority will be allocated more bandwidth and so continue to run smoothly even when there is heavy traffic on the network. You can set the download and upload speed for each client device here. The value can be used to calculate WAN usage. 

**To set up QoS, please follow the steps below.**

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-qos.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

1. Click Add to add entries.
2. Select the MAC-Address and make a comment to specify the devices, and set its Download/Upload rate.
3. Click *Save & Apply*.

----
## Custom DNS
If you set custom DNS servers, any DNS name will be resolved through the DNS Servers set here instead of the one obtained from WAN.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-custom-dns.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

- Rebind protection: This function may cause private DNS lookup failure. Do not enable it if your network has a captive portal.
- Override All Clients' DNS: If Enabled, your router will bypass hard-coded DNS settings on all clients, such as Chrome cast, TV boxes, etc.
- DNS Settings: Select Default to use the gateway of the parent router, or Manual to set the DNS server manually with Preferred/Alternate DNS.

---
## DDNS
Dynamic Domain Name Service (Dynamic DNS or DDNS) is a service used to map a domain name to the dynamic IP address of a network device. Most ISPs assign a dynamic IP address to the router and you can use this IP address to access your router remotely. However, the IP address can change from time to time and you don’t know when it changes. In this case, you might apply the DDNS (Dynamic Domain Name Server) feature on the router to allow you to access your router and local servers (FTP, HTTP, etc.) using a domain name without checking and remembering the IP address.

!!! Note
    DDNS would not work if the ISP assigns a private WAN IP address (e.g. 192.168.1.x) to the router.  

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-ddns.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**To set up DDNS, please follow the steps below.**

1. Enable DDNS.
2. Select the DDNS Service Provider. It is recommended to select no-ip.com or dyn.com. If you don’t have a DDNS account, you have to register first.
3. Enter the Domain / Username / Password of your account.
4. Set the Check Interval and Force Interval.
5. Click *Save & Apply*.

---
## Static Routing
is a form of routing that is configured manually by a network administrator or a user by adding entries into a routing table. The manually-configured routing information guides the router in forwarding data packets to the specific destination. 

For example, I want my PC to surf the Internet through router A and visit my company’s local network at the same time. Now I have a switch and Router B. I connect the devices as shown in the following figure so that the physical connection between my PC and my company’s server is established. 

To configure the static routing so that you can surf the Internet and visit my company’s network at the same time, please follow the steps below.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/4g5g_router/static-routing.webp" alt="" width="800px"/>

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

---
## Port Forwards
Port Forwards can be used to set up public services on your local network (such as HTTP, FTP, DNS,  POP3/SMTP and Telnet), while keeping the local network safe from the other services that are still invisible on the Internet. 

Different services use different service ports. Port 80 is used in HTTP service, port 21 in FTP service, port 25 in SMTP service and port 110 in POP3 service. Do verify the service port number before the configuration.

For example, I want to share my personal website I’ve built on the local network to my friends on the Internet. Say, my personal PC IP address is 192.168.10.100, connecting to the router with WAN IP address 218.18.232.154. Please follow the step-by-step instructions to configure it.

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

----
## Port Trigger
Port Trigger can specify a triggering port and its corresponding external ports. When a host on the local network initiates a connection to the triggering port, all the external ports will be opened for subsequent connections. 

The router can record the IP address of the host. When the data from the Internet return to the external ports, the router can forward them to the corresponding host. 

Port Triggering is mainly applied to online games, VoIPs, video players and common applications including MSN Gaming Zone, Dialpad and QuickTime 4 players, etc.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-port-trigger.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**To configure the Port Trigger rules, please follow the steps below.**

1. Click Add, and enter the required parameters.You can add multiple port trigger entries as needed.

    - Name: Set a name for the entry.
    - Trigger Protocol: Select TCP or UDP based on the application's requirements, or TCP+UDP if you are unsure of which protocol you are using .This is the protocol that will be used for the trigger port. 
    - Trigger Port: Enter the trigger port range that the application uses to initiate connections. The trigger ports can not be overlapped.
    - External Protocol: Select the identical protocol as trigger port to ensure that the traffic is forwarded correctly. 
    - External Port: Enter the external port identical with the inbound port that the application expects to receive traffic and forward it to the internal device. You should verify the external ports the application uses first and enter them into External Port field in the format required. 
    - Delete: To delete the entries as needed.

2. Click *Save & Apply*. 

---
## DMZ
A DMZ (Demilitarized Zone) host on the local network will become a virtual server with all ports opened and totally exposed to the Internet, causing the unlimited bi-directional communication between internal and external hosts. 

The DMZ host becomes a virtual server with all ports opened. When you are not clear about which ports to open in some special applications, such as IP camera and database software, you can set the PC to be a DMZ host.

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

----
## Online Detection
is essential for ensuring that your network remains online and operational even if there are issues with the primary WAN connection. It allows for automatic failover to a backup connection, which can be critical for businesses and homes that require continuous Internet access.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-online-detection.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

**To configure the online detection, please follow the steps below.**

1. Enable Online Detection.
2. Select the Target Host, either Default or Manual as needed.
3. Enter the Host, either a public DNS server like Google's 8.8.8.8 or any other reliable server that is expected to be always online, in order to check the online status of the WAN port. 
4. Enter the Period, that is the timeout seconds when no Ping replies received and network restarted.
5. Enter the Ping Period, that is the interval between which the Ping is sent in seconds.
6. Select the Protocol, either TCP or ICMP as needed. If TCP is selected, you also need to enter the Port value.
7. Click *Save & Apply*.

----
## TTL
TTL (Time To Live) sets the maximum time for packets to survive in the network, and is filled in according to the requirements of the operator. By default, the router forwards the TTL of the incoming client device minus one. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-ttl.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

- Disabled: Select it if you do not need to modify TTL values for any specific reason.
- Extend the TTL Value: Select it if you need to increase the TTL of incoming packets.
- Spoof LAN TTL Value: Select it if you want to override outgoing packets' TTL to the router's default value.
- Custom: Select Custom, and enter the specific IPv4 TTL value as needed (e.g., 65).

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-ttl2.webp" alt="" width="500px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

----
## Wake on LAN
Wake-on-LAN (WoL) is an Ethernet or Token ring computer network standard that allows a computer to be turned on or awakened by a network message. The message is usually sent by a program executed on other devices. It is also possible to initiate the message from another network by using subnet directed broadcasts or a WOL gateway service.

To use this function requires the main board and wired network adapter must support Wake-on-LAN feature. Please follow the steps below to configure it.

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

----
## UPnP
UPnP  (Universal  Plug  and  Play)  protocol  allows  applications  or  host  devices to automatically find the front-end NAT device and send request to it to open the corresponding ports. With UPnP enabled, the applications or host devices on the local network and the Internet can freely communicate with each other thus realizing the seamless connection of the network. 

Enable UPnP if you want to use applications for multi-player gaming, peer-to-peer connections, real-time communication (such as VoIP or telephone conference) or remote assistance, etc. 

For example, when you connect your Xbox to the router which has connected to the Internet to play online games, UPnP will send request to the router to open the corresponding  ports allowing the following data penetrating the NAT to transmit. Therefore, you can play Xbox online games without a hitch.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/wireless_router/network-upnp.webp" alt="" width="800px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

!!! Note
    - UPnP is enabled by default in this router.
    - Only the application supporting UPnP protocol can use this feature.
    - UPnP feature needs the support of operating system (e.g.Windows Vista/ Windows 7/Windows 8, and etc. Some operating systems need to install the UPnP components).