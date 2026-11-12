# Diagnostics

## Ping

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/pon_router/image-56.webp" alt="" width="1000px" style="border: 1px solid #eee;" />

**Ping** is a network tool that sends ICMP echo requests to test if a device (e.g., server, router) is reachable and measure response time. It's used to verify connectivity, detect latency, or troubleshoot network failures.

- Host Address: Enter the target IP/domain you want to test (e.g., 8.8.8.8 or google.com).
- WAN Interface: Keep the default *Any* and the router will automatically use its primary WAN IP (or all available WAN interfaces) as the source for the ping test.
- Start: Click to run the diagnostics.

---

## Ping6

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/pon_router/image-57.webp" alt="" width="800px" style="border: 1px solid #eee;"/>  

**Ping6** is an IPv6 version of the ping tool that sends ICMPv6 Echo Requests to test connectivity and measure latency between devices in an IPv6 network. It's primarily used to verify IPv6 reachability, troubleshoot network issues, and assess path performance.

- Host Address: Enter the target IPv6 address (e.g., 2001:db8::1) or domain name to test connectivity.
- WAN Interface: The router's IPv6-enabled public-facing interface (or "Any" for auto-selection), determining the source of Ping6 packets.
- WAN Interface: Keep the default *Any* and the router will automatically select an active IPv6-enabled WAN interface as the Ping6 source.
- Start: Click to run the diagnostics.

---

## Tracert

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/pon_router/image-58.webp" alt="" width="1000px" style="border: 1px solid #eee;" />

**Tracert (Traceroute)** is a network diagnostic tool that maps the path (hops) between your router and a target IP/domain, measuring latency at each node. It's used to identify routing failures, congestion points, or connectivity issues across networks.

- Protocol: Select a proper protocol for the traceroute test.

    - ICMP (Internet Control Message Protocol) is a Layer-3 protocol used for diagnostics (e.g., ping, traceroute) and error reporting (e.g., "Destination Unreachable").
    - UDP (User Datagram Protocol) is a Layer-4 protocol for fast, non-connection data transmission (e.g., video streaming, DNS queries).

- Host Address: Enter the target IP or domain name to trace the network path to.
- Number Of Tries: Sets how many probe packets are sent per hop (default 3).
- Time out: Defines how long (seconds) to wait for a hop's response before marking it as failed.
- Data Size: Adjusts the probe packet size (bytes) to test MTU/fragmentation issues.
- DSCP: Marks packets with a QoS priority value (0-63) for traffic prioritization testing.
- Max Hop Count: Limits the maximum hops traced (default 30) before stopping.
- WAN Interface: Keep the default *Any* and the router will automatically choose the optimal WAN interface (based on routing tables) as the source for outgoing traceroute packets.
- Start: Click to run the diagnostics.

---

## Tracert6

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/pon_router/image-59.webp" alt="" width="1000px" style="border: 1px solid #eee;" />

**Tracert6** is the IPv6 version of traceroute, mapping the network path (hops) to a target IPv6 address using ICMPv6 probes. It's used to diagnose routing issues, latency problems, or connectivity failures in IPv6 networks.

- Host Address: Enter the target IPv6 address (e.g., 2001:db8::1) or domain name to trace the network path to.
- Number Of Tries: Sets how many ICMPv6 probe packets are sent per hop (default typically 3).
- Time out: Defines the wait time (in seconds) for each hop's response before marking it as failed.
- Data Size: Adjusts the ICMPv6 probe packet size (bytes) to test path MTU or fragmentation.
- Max Hop Count: Limits the maximum number of hops traced (default 30) before stopping.
- WAN Interface: Keep the default *Any* and the router will automatically select an active IPv6-enabled WAN interface as the source for outgoing traceroute probes, following the system's default IPv6 routing table.
- Start: Click to run the diagnostics.
---