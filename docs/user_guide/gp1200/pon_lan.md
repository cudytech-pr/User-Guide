# LAN

<img src="../../../images/gp1200/image-6.png" alt="" width=1000px style="border: 1px solid #eee;" />

**• IP Address:** Unique identifier for a device on the network (e.g.,192.168.1.1 or 2001:db8::1).

**• Subnet Mask:** Defines the network segment (e.g., 255.255.255.0 splits IP into network/host parts).

**• IPv6 Link-Local Address Mode:** Select the method to obtain an addresses for local communication without DHCP.

<blockquote>
<p>- Auto: Automatically generate an IPv6 Link - Local Address for local communication.</p>
<p>- Static: Manually enter an IPv6 Link - Local Address for local communication.</p>
</blockquote>
**• IPv6 DNS Mode:** Select the method to assign the DNS servers.
<blockquote>   
<p>- HGW Proxy: Select it if your ISP requires centralized DNS management or when you need IPv4 compatibility in an IPv6-only network. Avoid it if you prioritize direct DNS queries for privacy or per-device customization.</p>
<p>- WAN Connection: Select it if you want devices to bypass the router's proxy and directly use ISP-assigned or custom DNS servers (e.g.,for privacy or granular control). IPv6 DNS address(es) will be automatically assigned.</p>  
<p>- Static: Select it if you need to manually specify custom DNS servers for enhanced privacy or performance. Then manually enter the provided IPv6 DNS1 (preferred) and IPv6 DNS2 (alternate) addresses.</p>
</blockquote>

**• Prefix Mode :** Select the method how the Router gets its IPv6 network address range. 
<blockquote>   
<p>- WAN Connection: Automatic ISP assignment, common for home use.</p>
<p>- Static: Manually set a fixed prefix, usually for business/lab networks.</p>
</blockquote>   

**• IGMP Snooping:** Optimizes multicast traffic for LAN ports (reduces unnecessary flooding).

**• LAN1~ LAN4:** Toggle per-port multicast filtering.

• Apply Changes: Click to save and activate configuration. It may briefly disconnect services.

<p><img src="../../../images/noteicon.png"> For enterprise networks, IPv6 settings often require ISP compatibility checks.</p>
