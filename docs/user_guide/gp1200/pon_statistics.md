# Statistics

## Interface

<img src="../../../images/gp1200/image-73.png" alt="" width="800px" style="border: 1px solid #eee;" />
    
<p><strong>Interface Statistics</strong> monitors real-time traffic data (e.g., speed, packets, errors) on router interfaces (WAN/LAN) and thus help to troubleshoot network performance or congestion.</p>
    
<p><strong>• Interface:</strong> The network port name (e.g., WAN/LAN) being monitored.</p>
<p><strong>• Rx pkt:</strong> Total packets received (inbound traffic).</p>
<p><strong>• Rx err:</strong> Corrupted/error packets received (CRC/alignment issues).</p>
<p><strong>• Rx drop:</strong> Packets dropped due to buffer/bandwidth limits.</p>
<p><strong>• Tx pkt:</strong> Total packets transmitted (outbound traffic).</p>
<p><strong>• Tx err:</strong> Failed transmissions (collisions/queue errors).</p>
<p><strong>• Tx drop:</strong> Packets discarded before sending (congestion/QoS rules).</p>
<p>• Refresh: Click to update the Interface Statistics.</p>

----

## PON_Statistics

<img src="../../../images/gp1200/image-74.png" alt="" width="800px" style="border: 1px solid #eee;" />

<p><strong>PON Statistics</strong> tracks optical signal metrics (e.g., power levels, uptime) for fiber connections (GPON/EPON), and thus to ensure stable ISP link quality. Only visible on fiber-optic routers with PON ports.</p>

<p><strong>• Bytes Sent/Received:</strong> Total data volume (in bytes) sent or received over the PON interface.</p>

<p><strong>• Packets Sent/Received:</strong> Count of all packets (including unicast/multicast/broadcast) sent or received.</p>

<p><strong>• Unicast Packets Sent/Received:</strong> Point-to-point traffic (single destination) sent or received.</p>

<p><strong>• Multicast Packets Sent/Received:</strong> Traffic sent to or received from a specific group of devices.</p>

<p><strong>• Broadcast Packets Sent/Received:</strong> Traffic sent to or received from all devices in the network.</p>

<p><strong>• FEC Errors:</strong> Forward Error Correction errors, indicating signal quality issues.</p>

<p><strong>• HEC Errors:</strong> Header Error Control errors, indicating signal quality issues.</p>

<p><strong>• Packets Dropped:</strong> Packets discarded due to congestion/buffer limits.</p>

<p><strong>• Pause Packets Sent/Received:</strong> Flow control frames sent or received to temporarily halt data transmission during network congestion, preventing packet loss.</p>