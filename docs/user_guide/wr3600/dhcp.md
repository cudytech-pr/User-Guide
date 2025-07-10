# DHCP Server

Router acts as a DHCP (Dynamic Host Configuration Protocol) server, which is enabled by default. It dynamically assigns TCP/IP parameters to client devices from the IP Address Pool. DO NOT disable DHCP server unless you have another DHCP server, or you want to manually assign the TCP/IP parameters to every client device on the network. 

## DHCP Status

<img src="../../../images/wr3600/wr3600 (36).png" alt="" width="800px" style="border: 1px solid #eee;" />

Go to *System Status -> DHCP Server* to see it is *Enabled* or *Disabled* as welll as its IP address and subnet mask. Click *More Details* to know more information about it or make changes on Settings page. 

## DHCP Leases

<img src="../../../images/wr3600/wr3600 (64).png" alt="" width="800px" style="border: 1px solid #eee;" />

The DHCP Leases will show a list of clients which the Router being a DHCP server has allocated an IP address to, including such information as IP address, MAC address and Host name.

## DHCP Settings

<img src="../../../images/wr3600/wr3600 (133).png" alt="" width="800px" style="border: 1px solid #eee;" />

**To specify the IP address that the Router assigns, please follow the steps below.**

1.Enable the DHCP Server.

2.Enter the starting IP addresses and the Limit number to create the IP Address Pool.

3.(Optional) Enter the DNS if the ISP offers. 

4.Enter the Leasetime.

5.Click *Save & Apply*.

<img src="../../../images/noteicon.png"> If you want to reserve for a specified client device an IP address, which is assigned by the router as a DHCP server, you may use the [IP/MAC binding](security.md#ipmac-binding) function.