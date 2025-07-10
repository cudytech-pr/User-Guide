# Overview
## Package Content
<img src="../../../images/gs1024e/package.jpg" width="500" alt="">

---

## Appearance

<img src="../../../images/gs1024e/frontpanel.png" width="500" alt="">

## LED & DIP
<table>
    <tr>
        <th>LED</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>PWR</td>
        <td>
        <p>On: Power is on.</p>
        <p>Off: Power is off.</p>
        </td>
    </tr>
    <tr>
        <td>
        <p>Link/Act</p>
        <p>(1-24)</p>
        </td>
        <td>
        <p>On: Link but no data.</p>
        <p>Flash: Link and data transmission. </p>
        <p>Off: No link or no data.</p>
        </td>
    </tr>
    <tr>
        <td><b>DIP</b></td>
        <td><b>Description</b></td>
    </tr>
    <tr>
        <td>Managed</td>
        <td>(Default) Light-managed Mode. Allow to manage the swicth on the web-based GUI.</td>
    </tr>
    <tr>
        <td>VLAN</td>
        <td>Non-managed Mode. The designated Downlink Port 1-22 are isolated from each other, and only transmit data with the Uplink Port 23-24.</td>
    </tr>
    <tr>
        <td>Extend</td>
        <td>Non-managed Mode. The data speed of Port 1-22 will be capped at 10 Mbps and the maximum transmission distance be 250 meters.</td>
    </tr>
    <tr>
        <td>RESET</td>
        <td>Toggle the switch from left to right and back within 2 seconds to restore the factory defaults.</td>
    </tr>
</table>
---

## Topology
<img src="../../../images/gs1024e/topology-vlan.jpg" width="500" alt="">

<img src="../../../images/gs1024e/topology-qos.jpg" width="500" alt="">
