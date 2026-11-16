## General Settings - WAN Mode

This is only available in *Main Router and AP Controller* mode.

It defines how the AP controller (working in *Main Router and AP Controller* mode) connects to the Internet or an external network. Proper setup ensures seamless integration with the main router and ISP requirements. Select an appropriate type of Internet connection and configure the required parameters.

### DHCP
Automatically obtains IP address, subnet, and DNS from ISP's DHCP server (plug-and-play).
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/general-wan1.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- Hostname: Customize the device's network identifier, used for management and DNS resolution. 
- MAC Clone: Spoof a custom MAC address on the WAN interface.
- MTU: Maximum Transmission Unit (bytes) for WAN packets. Keep it default or adjust max packet size to avoid fragmentation.

Click *Save & Apply* to save and activate the settings or changes.

### PPPoE
Requires username/password to authenticate with ISP (common for DSL/cable), encapsulating data in PPP frames.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/general-wan2.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- Username: Enter the ISP-provided login ID for PPPoE authentication.
- Password: Enter the ISP-provided secret key paired with the username to establish a PPPoE connection.
- Secondary Connection: Optional backup Static/DHCP link for failover (if primary fails).
- Access Concentrator: Leave it empty for auto-detection, or manually enter the ISP's PPPoE server name.
- Service Name: Leave it empty for auto-detection, or manually enter the ISP-specific PPPoE service identifier.
- MAC Clone: Spoof a WAN MAC address to match ISP-registered devices.
- MTU: Maximum Transmission Unit (bytes) for WAN packets. Keep it default or adjust max packet size to avoid fragmentation.

Click *Save & Apply* to save and activate the settings or changes.

### Static (Fixed IP)
Manually configure IP, gateway, and DNS (for servers/VoIP needing consistent addressing).

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/general-wan3.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- IP Address: Enter the unique public or private IPv4 address assigned to your AP's WAN interface.
- Subnet Mask: Defines the network segment, e.g., 255.255.255.0 for a /24 range.
- Default Gateway: Enter the AP's IP where traffic exits to the wider network.
- Preferred DNS: Enter a primary DNS server for domain resolution.
- Alternate DNS: (Optional but recommended) Enter a backup DNS server if the primary fails.
- MAC Clone: Spoof a custom MAC address on the WAN interface.
- MTU: Maximum Transmission Unit (bytes) for WAN packets. Keep it default or adjust max packet size to avoid fragmentation.

Click *Save & Apply* to save and activate the settings or changes.

### L2TP / PPTP
VPN tunneling protocol (often paired with IPsec) for secure remote site connections over public networks.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/general-wan4.webp" alt="" width="800px" style="border: 1px solid #eee;" />

- Server Address: Enter the IP/hostname of your L2TP VPN server.
- Username/Password: Enter the credentials for L2TP authentication (often paired with IPsec pre-shared keys).
- Addressing Type: Choose between Dynamic IP (DHCP-assigned) or Static IP (manual WAN IP for VPN).
- MAC Clone: Override the WAN interface MAC address.
- MTU: Maximum Transmission Unit (bytes) for WAN packets. Keep it default or adjust the packet size to avoid fragmentation.

Click *Save & Apply* to save and activate the settings or changes.