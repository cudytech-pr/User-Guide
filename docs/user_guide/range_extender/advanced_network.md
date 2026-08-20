# Network

## LAN

By default, the Range Extender automatically obtains an IP address from the main router. It is recommended to keep this setting unless you need to assign a fixed IP address for network management. Incorrect settings may prevent the Range Extender from accessing the network or being reachable for management.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/range_extender/network-lan.webp" alt="" width="400px" style="border: 1px solid #eee; display: block; margin: 0 auto;" />

If you do need to assign a fixed IP address, please follow the steps below.

1. Enable *Static address*. 
2. Set an unused *IP address* in the same subnet as the main router. For example, if the main router is 192.168.1.1, you can use 192.168.1.250.
3. Select a *subnet mask* from the drop-down list or customize it. Usually the same as the main router's subnet mask, such as 255.255.255.0.
4. Enter the IP address of the main router in the *Default Gateway* field, such as 192.168.1.1.
5. Enter a *preferred DNS server*, such as the main router's IP address or a public DNS server.
6. Enter an *alternate DNS server* as backup if needed.
7. It is recommended to keep the default *MTU* value unless your ISP or network administrator specifies otherwise.
8. Click *Save & Apply*.

!!! example "Example"

    If the main router's network settings are:

    - *Router IP:* `192.168.1.1`
    - *Subnet Mask:* `255.255.255.0`

    You can configure the Range Extender as:

    ```text
    IP Address:        192.168.1.250
    Subnet Mask:       255.255.255.0
    Default Gateway:   192.168.1.1
    Preferred DNS:     192.168.1.1
    Alternate DNS:     Optional
    MTU:               Keep the default value
    ```
  
!!! Note
    - If you have configured Port Forwarding, DMZ, or DHCP Address Reservation, and the new LAN IP address is in a different subnet from the old one, you need to reconfigure these settings.
    - If the new LAN IP address conflicts with the WAN IP address, the LAN IP address will automatically be changed to 10.1.1.1.