# Advanced Settings - Network

Network section allows you to manage and configure a series of network features for the Router. 

## LAN

The router is preset with a default LAN IP 192.168.10.1, which you can use to log in to its web management page. The LAN IP address together with the Subnet Mask also defines the subnet that the connected devices are on. If the IP address conflicts with another device on your local network or your network requires a specific IP subnet, you can change it.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/lan2.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

1. Enter a new IP Address appropriate to your need. 

2. Set the Subnet Mask or keep it as default. 

3. Enable IP Routed Subnet as needed. If it is enabled, you need to enter the IP Address and Subnet Mask as well.

4. Click *Save & Apply*.
  
!!! Note
    - If you have set the Port Forwarding, DMZ or DHCP address reservation, and the new LAN IP address is not in the same subnet with the old one, then you should reconfigure these features.
    - If in conflict with the WAN IP address, the LAN IP will automatically change into 10.1.1.1.

## DHCP Server

DHCP Server is enabled by default and dynamically assigns TCP/lP parameters to client devices from the IP Address Pool. DO NOT disable DHCP server unless you have another DHCP server, or you want to manually assign the TCP/P parameters to every clients on the network. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/dhcp.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

*To specify the IP address that the router assigns, please take the steps below.*

1. Enable *DHCP Server*.

2. Enter the starting IP address and the Limit number to create the IP address pool.

3. (Optional) Enter the Preferred and Alternate DNS if your ISP provides.

4. Set the *Lease time*.

5. Click *Save & Apply*.

!!! Note
    If you want to reserve for a specified client device an IP address, which is assigned by the router as a DHCP server, you may use the [IP/MAC binding](security.md#ipmac-binding) function.

## IPv6

The router supports the next-generation Internet Protocol IPv6, providing a vastly expanded IP address space, improved network efficiency, and enhanced connectivity for modern devices.

!!! Note
    - If the current version of the firewall (or VPN, block list, and etc.) does not support IPv6, you may enable and configure the IPv6 function on this page.
    - If you use VPN and IPv6 functions at the same time, it's likely to cause IPv6 data leakage.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/ipv6.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

1. Enable IPv6.
2. Select your Interface (WAN port) to be configured.
3. Select your connection type from the drop-down list accordingly and configure the required parameters provided by the ISP.

### Relay

Typically used for IPv6 transition mechanisms. The router will act as a relay between your local IPv6 network and an IPv4-based upstream network provided by your ISP. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/ipv6_relay.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Select *Relay* and just click *Save & Apply* without any additional configuration.

### Dynamic IP(SLAAC/DHCPv6)

Automatically assigns IPv6 addresses via router advertisements (SLAAC) or DHCPv6 servers, ideal for plug-and-play deployments with changing network topologies.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/ipv6_dhcp.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Select *Dynamic IP(SLAAC/DHCPv6)*, and configure MAC Clone and MTU as needed.Then click *Save & Apply*.

- MAC Clone: (Optional) Enter the MAC address of the device that is allowed by your ISP. You can usually find this in the device's network settings or on a label on the device.
- MTU: Enter the appropriate MTU size (commonly 1500 bytes for compatibility with IPv4). 

### Static(Fixed lP)

Manually configured IPv6 addresses for critical devices (e.g., PLCs), ensuring stable remote access and firewall rule consistency.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/ipv6_static.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Select *Static (Fixed IP)* and enter the fixed *IPv6 address*, *gateway*, *prefix* and *DNS* server address provided by your ISP. Configure MAC Clone and MTU as needed. Then click *Save & Apply*.

- IPv6-Address: The fixed IPv6 address assigned to the Router (e.g., 2001:db8::1).
- IPv6-Gateway: The default gateway for IPv6 traffic (e.g., 2001:db8::ff).
- IPv6 prefix: The network prefix length (e.g., /64) defining the subnet scope.
- Preferred DNS: Primary DNS server for IPv6 resolution (e.g., 2001:4860:4860::8888).
- Alternate DNS: Backup DNS server if the primary fails (e.g., 2001:4860:4860::8844).
- MAC Clone: (Optional) Enter the MAC address of the device if the ISP requires a specific MAC address for the static IP assignment. You can usually find this in the device's network settings or on a label on the device.
- MTU: Enter the appropriate MTU size based on the network's physical layer, typically 1500 bytes for Ethernet.

### Passthrough

Allows an IPv6-enabled device to manage its own IP settings directly from the ISP, bypassing the router's DHCP server. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/ipv6_passthrough.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Select *Passthrough* and just click *Save & Apply* without any additional configuration.

### MAP-E

Namely, Mapping of Address and Port with Encapsulation, is a method for translating IPv6 addresses to IPv4 addresses. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/ipv6_mape.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Select *MAP-E*, and configure MAC Clone and MTU as needed. Then click *Save & Apply*.

- MAC Clone: (Optional) MAP-E usually does not involve MAC address restrictions, so MAC Clone is not typically necessary.
- MTU: Enter the appropriate MTU size according to the maximum IPv4 packet size, which is typically 1500 bytes minus the headers.

### DS-Lite

A technology that allows ISPs to provide IPv4 service over an IPv6 network. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/ipv6_dslite.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

Select *DS-Lite*, and configure MAC Clone and MTU as needed. Then click *Save & Apply*.

- MAC Clone: (Optional) DS-Lite usually does not involve MAC address restrictions, so MAC Clone is not typically necessary.
- MTU: Enter the MTU value based on your network's requirements. The value should be within the range of 1280 to 1582 bytes. The MTU setting is important to ensure that the encapsulated IPv4 packets can be transmitted over the IPv6 network without fragmentation. 

## QoS

QoS (Quality of Service) allows you to prioritize connection of specific devices for a set duration. Devices set as high priority will be allocated more bandwidth and so continue to run smoothly even when there is heavy traffic on the network. You can set the download and upload speed for each client device here. The value can be used to calculate WAN usage. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/qos_wan1.webp" alt="" width="800px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

1. Select the Interface to be configured.
2. Click *Enable*.
3. Set a speed for the *Download* and *Upload*.
4. Click *Save & Apply*.

## Custom DNS

If you set custom DNS servers, any DNS name will be resolved through the DNS Servers set here instead of the one obtained from WAN.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/custom-dns.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

- **Rebind protection**: This function may cause private DNS lookup failure. Do not enable it if your network has a captive portal.

- **Override All Clients' DNS**: If Enabled, your Router will bypass hard-coded DNS settings on all clients, such as Chrome cast, TV boxes, etc.

- **DNS Settings**: Select a type of DNS settings.
    - Default: Uses ISP-provided DNS. Fast but lacks privacy.
    -  DNS over TLS: Encrypts queries via TLS. Secure but may add 5-10ms latency.
        - Cloudflare: Provides fast, globally distributed DNS resolution via Anycast (1.1.1.1), with TLS 1.3 support for secure, low-latency connections.
        - Google: Provides reliable DNS resolution via Google Public DNS (8.8.8.8).
        - NextDNS: Connects to your NextDNS configuration using your NextDNS ID (available on the Setup page of your NextDNS account), providing ad blocking, tracker protection, and parental controls.
    - Manual: Customize DNS, entering the *preferred/alternate DNS*.

## DDNS

Dynamic Domain Name Service (Dynamic DNS or DDNS) is a service used to map a domain name to the dynamic IP address of a network device. Most ISPs assign a dynamic IP address to the Router and you can use this IP address to access your Router remotely. However, the IP address can change from time to time and you don't know when it changes. In this case, you might apply the DDNS feature on the Router to allow you to access your Router and local servers (FTP, HTTP, etc.) using a domain name without checking and remembering the IP address.

!!! Note
    DDNS would not work if the ISP assigns a private WAN IP address (e.g. 192.168.1.x) to the Router.  

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/ddns.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

*To set up DDNS, please follow the steps below.*

1. *Enable* DDNS.
2. Select a DDNS Service Provider. It is recommended to select *no-ip.com* or *dyn.com*. If you don't have a DDNS account, you have to register first.
3. Enter the Domain / Username / Password of your account.
    - Domain: Custom hostname (e.g., yourname.ddns.net).
    - Username/Password: Authentication for provider API.
4. Set the Check Interval and Force Interval.
    - Check Interval: Time between IP checks (default 10min).
    - Force Interval: Mandatory update cycle (even if IP unchanged).
    - Last Update: Displays timestamp of most recent successful sync.
5. Click *Save & Apply*.

## Static Routing

It is a form of routing that is configured manually by a network administrator or a user by adding entries into a routing table. The manually-configured routing information guides the Router in forwarding data packets to the specific destination. 

For example, I want my PC to surf the Internet through Router and visit my company's local network at the same time. Now I have a switch and Router B. I connect the devices as shown in the following figure so that the physical connection between my PC and my company's server is established. 

To configure the static routing so that you can surf the Internet and visit my company's network at the same time, please follow the steps below.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/static_routing.webp" alt="" width="700px" style="display:block; margin:0 auto;" />

1. Disable Router B's DHCP function. Change the Routers' LAN IP addresses to two different IP addresses on the same subnet. 
2. Log in to Router's management web page [http://Cudyac.net](http://Cudyac.net), and go to *Advanced Settings -> Network -> Static Routing*.
3. Click *Add* and then enter the parameters as required.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/static-routing2.webp" alt="" width="800px" style="border: 1px solid #eee;display:block; margin:0 auto;" />
    - Interface: Select the type of interface that sends out data packets to the gateway.
        - WAN: Connect to external networks (ISP/MPLS) with NAT/firewall.
        - LAN: Local device switching (VLAN-aware for OT segmentation).
        - WISP: Wireless ISP client mode (bridge/route to upstream AP).
        - 4G: Cellular failover/Primary WAN (AT&T FirstNet certified for critical infra).
    - Target: Enter the Host-IP or Network IP address you want to assign to a static route. This IP address cannot be on the same subnet with the WAN IP or LAN IP of Router.
    - Subnet Mask: It is required if the Target is a network. It determines the destination network with the destination IP address. If the destination is a single IP address, enter 255.255.255.255; otherwise, enter the subnet mask of the corresponding network IP. 
    - Gateway: Enter the IP address of the gateway device which the data packets will be sent to. This IP address must be on the same subnet with the Router's IP which sends out data. 

4. Click *Save & Apply*.

 Now you can open a web browser on your PC, enter the company server's IP address to visit the company network.

## Port Forwards

Port Forwards can be used to set up public services on your local network (such as HTTP, FTP, DNS,  POP3/SMTP and Telnet), while keeping the local network safe from the other services that are still invisible on the Internet. 

Different services use different service ports. Port 80 is used in HTTP service, port 21 in FTP service, port 25 in SMTP service and port 110 in POP3 service. Do verify the service port number before the configuration.

For example, I want to share my personal website I've built on the local network to my friends on the Internet. Say, my personal PC IP address is 192.168.10.100, connecting to the Router with WAN IP address 218.18.232.154. Please follow the step-by-step instructions to configure it.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/port-forwards.webp" alt="" width="800px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

1. Assign a static IP address to your PC, for example 192.168.10.100.
2. Log in to [http://Cudyac.net](http://Cudyac.net), and go to *Advanced Settings -> Network -> Port Forwards*.
3. Click *Add* and then enter the required parameters.
    - Name: Give a name for the entry.
    - Protocol: Select *TCP+UDP* if you are unsure of which protocol you are using. 
        - TCP: Usually used for web browsing, file transfers, and most client-server applications.
        - UDP: Used for streaming services, online gaming, and other applications that require fast transmission of data.
    - Interface: Select *WAN* or *VPN* according to the source of traffic you want to forward.
    - External Port: Specify the port number that will receive traffic on the WAN or VPN interface.
    - Internal IP Address: Enter the IP address of the device on your local network that should receive the forwarded traffic.
    - Internal Port: Specify the port number on the internal device that will receive the forwarded traffic.
    - Delete: Delete the entry as needed.

4. Click *Save & Apply*. 

Now users on the Internet can enter *http://WAN IP* (in this example: *http://218.18.232.154*) to visit your personal website.

If you want to provide several services in a Router, please add multiple port forwarding rules.

!!! Note
    - The WAN IP should be a public IP address. For the WAN IP is assigned dynamically by the ISP, it is recommended to apply and register a domain name for the WAN ([How to set up a Dynamic DNS service account](#ddns)). Then users on the Internet can use *http://domain name* to visit the website.
    - If you have changed the default External Port, you should use *http://WAN IP:external port* or *http://domain name:external port* to visit the website.

## Port Trigger

Port Trigger can specify a triggering port and its corresponding external ports. When a host on the local network initiates a connection to the triggering port, all the external ports will be opened for subsequent connections. 

The Router can record the IP address of the host. When the data from the Internet return to the external ports, the Router can forward them to the corresponding host. 

Port Triggering is mainly applied to online games, VoIPs, video players and common applications including MSN Gaming Zone, Dialpad and QuickTime 4 players, etc.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/port-trigger.webp" alt="" width="800px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

*To configure the Port Trigger rules, please follow the steps below.*

1. Click *Add* and then enter the required parameters.
    - Name: Set a name for the entry.
    - Trigger Protocol: Select *TCP* or *UDP* based on the application's requirements, or *TCP+UDP* if you are unsure of which protocol you are using .This is the protocol that will be used for the trigger port. 
    - Trigger Port: Enter the trigger port range that the application uses to initiate connections. The trigger ports can not be overlapped.
    - External Protocol: Select the identical protocol as trigger port to ensure that the traffic is forwarded correctly. 
    - External Port: Enter the external port identical with the inbound port that the application expects to receive traffic and forward it to the internal device. You should verify the external ports the application uses first and enter them into this field in the format of xx or xx-xx. 
    - Delete: To delete the entries as needed.

2. Click *Save & Apply*. 

You can add multiple port trigger entries as needed.

## DMZ

A DMZ (Demilitarized Zone) host on the local network will become a virtual server with all ports opened and totally exposed to the Internet, causing the unlimited bi-directional communication between internal and external hosts. 

The DMZ host becomes a virtual server with all ports opened. When you are not clear about which ports to open in some special applications, such as IP camera and database software, you can set the PC to be a DMZ host.

!!! Note
    Due to the total exposure of DMZ host to the Internet, it will bring about certain potential safety hazards. So remember to dis-enable DMZ when not in use.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/dmz.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

For example, you want to get the home PC to join an online game without port restriction. You can set your PC as a DMZ host with all ports open. Please follow the steps below to configure it.

1. Assign a static IP address to your PC, for example 192.168.10.100.
2. Log in to [http://Cudyac.net](http://Cudyac.net), and go to *Advanced Settings -> Network -> DMZ*.
3. Enable *DMZ*, and enter the PC's IP address 192.168.10.100 manually in the (DMZ Host) *IP Address* field.
4. Click *Save & Apply*.

Now you've set your PC to a DMZ host and now you can make a team to game with other players.

## TTL

TTL (Time To Live) sets the maximum time for packets to survive in the network, and is filled in according to the requirements of the operator. By default, the Router forwards the TTL of the incoming client device minus one. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/ttl.webp" alt="" width="500px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

- Disabled: No TTL values for any specific reason.
- Extend the TTL Value: To increase the TTL of incoming packets.
- Spoof LAN TTL Value: To override outgoing packets' TTL to the Router's default value.
- Custom: Required to enter a specific IPv4 TTL value.

## Wake on LAN

Wake-on-LAN (WoL) is an Ethernet or Token ring computer network standard that allows a computer to be turned on or awakened by a network message. The message is usually sent by a program executed on other devices. It is also possible to initiate the message from another network by using subnet directed broadcasts or a WOL gateway service.

To use this function requires the main board and wired network adapter must support Wake-on-LAN feature. Please follow the steps below to configure it.

*STEP 1: Finish your computer settings before configuring the WoL function on the Router.*

1. Enter BIOS when starting up the computer. Then enable Resume by PCI Device and Resume by PCI-E Device. Usually this option is in power management menu.
2. Turn on the computer and go to *Control Panel -> Network and Internet -> Network and Sharing Center -> Local area connection -> Properties -> Configure -> Advanced*. Then enable Shutdown Wake-On-Lan, Wake on Magic Packet and Wake on pattern match.
3. Check MAC address of the computer that applies Wake-on-LAN. 

*STEP 2: Go to configure the Router.*

1. Login in to [http://Cudyac.net](http://Cudyac.net) and go to *Advanced Settings -> Network -> Wake on LAN*.
2. Click *Add*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/wake-on-lan.webp" alt="" width="800px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

3. Enter the MAC-Address you have checked previously in STEP 1.3, give a description for the device, and determine the time duration (Mins and Hour) and day frequency (Week Day).
4. Click *Save & Apply*.

## UPnP

UPnP  (Universal  Plug  and  Play)  protocol  allows  applications  or  host  devices to automatically find the front-end NAT device and send request to it to open the corresponding ports. With UPnP enabled, the applications or host devices on the local network and the Internet can freely communicate with each other thus realizing the seamless connection of the network. 

Enable UPnP if you want to use applications for multi-player gaming, peer-to-peer connections, real-time communication (such as VoIP or telephone conference) or remote assistance, etc. 

For example, when you connect your Xbox to the Router which has connected to the Internet to play online games, UPnP will send request to the Router to open the corresponding  ports allowing the following data penetrating the NAT to transmit. Therefore, you can play Xbox online games without a hitch.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/upnp.webp" alt="" width="800px" style="border: 1px solid #eee;display:block; margin:0 auto;" />

!!! Note
    - UPnP is enabled by default in this Router.
    - Only the application supporting UPnP protocol can use this feature.
    - UPnP feature needs the support of operating system. Some operating systems need to install the UPnP components.