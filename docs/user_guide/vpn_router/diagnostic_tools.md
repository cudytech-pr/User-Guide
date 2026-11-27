# Diagnostic Tools

## Diagnosis

Automatically checks connected device health and generates troubleshooting reports, thus to help optimize network by analyzing real-time metrics.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/diagnosis.webp" alt="" width="800px" style="border: 1px solid #eee;" />

Click *GO* to make a diagnosis. It may take some while to process. Please wait patiently. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/diagnosis2.webp" alt="" width="800px" style="border: 1px solid #eee;" />

The diagnosis result will indicate the status of Internet, Load Balancing, Devices, Services and System. 

## PING

Tests the connectivity between the Router and the tested host, and measure the round-trip time. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/PING.webp" alt="" width="800px" style="border: 1px solid #eee;" />

*To use PING for diagnosis, please follow the steps below.*

1. Select the tested Interface (WAN1/2/3/4).
    - WAN: Tests internet connectivity (e.g., pinging 8.8.8.8 via ISP gateway).

2. Enter the IP Address or Hostname of the tested host.
3. Click *PING* to start the diagnosis.

The PING result as below indicates the proper connection between the Router and the Bing server (www.bing.com) being tested.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/PING2.webp" alt="" width="800px" style="border: 1px solid #eee;" />

## TRACEROUTE

Tests the route (path) your Router has passed to reach the tested host, and measure transit delays of packets across an Internet Protocol network.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/traceroute.webp" alt="" width="800px" style="border: 1px solid #eee;" />

*To use TRACEROUTE for diagnosis, please follow the steps below.*

1. Select the tested Interface (WAN1/2/3/4).
    - WAN: Traces the public internet path (e.g., ISP hops to google.com), revealing external routing issues.

2. Enter the IP Address or Hostname of the tested host.
3. Click *TRACEROUTE* to start the diagnosis.

There will be several types of TRACEROUTE result for your reference.

- Normal Path: Shows all hops with stable latency, confirming reachability.
- Timeouts (*): Indicates firewalls blocking ICMP or node failures.
- Loops: Repeated IPs reveal routing misconfiguration.
- Destination Unreachable (!N/!X): Target/server actively rejects traffic.
- Latency Spikes: Sudden delay increases point to congested ISP links.

## NSLOOKUP

Query DNS servers to resolve domain names into IP addresses, helping troubleshoot network connectivity or configuration issues.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/nslookup.webp" alt="" width="800px" style="border: 1px solid #eee;" />

*To use NSLOOKUP for diagnosis, please follow the steps below.*

1. Enter the Lookup Hostname of tested host. 
2. Click *NSLOOKUP* to start the diagnosis. Then a result will show the resolved IP address(es) of a domain or confirms if DNS resolution is successful or fails.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/nslookup2.webp" alt="" width="800px" style="border: 1px solid #eee;" />

## System Log

Tracks all the Router behaviors. When the Router does not work normally, download the system log and send it to our [Technical Support](mailto:support@cudy.com) for troubleshooting. 
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/vpn_router/system_log.png" alt="" width="800px" style="border: 1px solid #eee;" />    

- *Download*: Click to download the system log for technical support.