# Diagnostic Tools

## Diagnosis
Automatically checks AP health and generates troubleshooting reports, thus to help optimize network by analyzing real-time metrics.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/diagnosis.webp" alt="" width="800px" style="border: 1px solid #eee;" />
Click *GO* to make a diagnosis. It may take some while to process. Please wait patiently. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/diagnosis2.webp" alt="" width="800px" style="border: 1px solid #eee;" />

The diagnosis result will indicate the status of Internet, Devices, Services and System. 

You can click *Download* to reserve the diagnosis *.bin* file, which may be decoded with vendor tools (e.g., Huawei eSight/Ubiquiti UNMS) and converted into readable logs/reports or be submitted to official support if analysis fails – include error details and timestamps.

----
## PING
To test the connectivity between the AP controller and the tested host, and measure the round-trip time. 

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/PING.webp" alt="" width="800px" style="border: 1px solid #eee;" />

*To use PING for diagnosis, please follow the steps below.*

1. Select the tested Interface.
    - WAN: Tests internet connectivity (e.g., pinging 8.8.8.8 via ISP gateway).
    - LAN: Checks local network health (e.g., pinging AP controller 192.168.1.1).
    - VPN: Validates tunnel stability by pinging remote VPN endpoints (e.g., 10.8.0.1).
2. Enter the IP Address or Hostname of the tested host.
3. Click *PING* to start the diagnosis.

The PING result as below indicates the proper connection between the AP controller and the Bing server (www.bing.com) being tested.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/PING3.webp" alt="" width="800px" style="border: 1px solid #eee;" />

-----
## TRACEROUTE
To test the route (path) your AP controller has passed to reach the tested host, and measure transit delays of packets across an Internet Protocol network.
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/TRACEROUTE.webp" alt="" width="800px" style="border: 1px solid #eee;" />

*To use TRACEROUTE for diagnosis, please follow the steps below.*

1. Select the tested Interface.
    - WAN: Traces the public internet path (e.g., ISP hops to google.com), revealing external routing issues.
    - VPN: Maps the encrypted tunnel path (e.g., corporate VPN gateways), exposing latency spikes or breaks in private networks.
2. Enter the IP Address or Hostname of the tested host.
3. Click *TRACEROUTE* to start the diagnosis.

There will be several types of TRACEROUTE result for your reference.

- Normal Path: Shows all hops with stable latency, confirming reachability.
- Timeouts (*): Indicates firewalls blocking ICMP or node failures.
- Loops: Repeated IPs reveal routing misconfiguration.
- Destination Unreachable (!N/!X): Target/server actively rejects traffic.
- Latency Spikes: Sudden delay increases point to congested ISP links.


-----
## NSLOOKUP
To query DNS servers to resolve domain names into IP addresses, helping troubleshoot network connectivity or configuration issues.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/NSLOOKUP.webp" alt="" width="800px" style="border: 1px solid #eee;" />

*To use NSLOOKUP for diagnosis, please follow the steps below.*

1. Enter the Lookup Hostname of tested host. 
2. Click *NSLOOKUP* to start the diagnosis. Then a result will show the resolved IP address(es) of a domain or confirms if DNS resolution is successful or fails.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/NSLOOKUP2.webp" alt="" width="800px" style="border: 1px solid #eee;" />

-----
## System Log
Tracks all the AP controller behaviors. When the AP controller does not work normally, download the system log and send it to our [Technical Support](mailto:support@cudy.com) for troubleshooting. 
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/system-log.webp" alt="" width="800px" style="border: 1px solid #eee;" />    

- *Update*: Click to refresh the system log.
- *Clear*: Click to erase all the system log up till now.
- *Download*: Click to download the system log for technical support.