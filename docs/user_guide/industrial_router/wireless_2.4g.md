# Wireless 2.4G

!!!Note
    IR04 is used as an example in this guide. Refer to your actual product for more details.
    
<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/industrial_router/wireless2.4g.webp" alt="" width="800px" style="border:1px solid #eee; display:block; margin:0 auto;" />

On the **General Settings >> Wireless 2.4G** page, you can customize the wireless 2.4G network. Please follow the steps below.

1. Click to enable *Wireless 2.4G*.
2. Customize *SSID*(a visible name) for your 2.4GHz Wi-Fi network, or keep it as default.
3. Select an *Encryption* (a security protocol) to prevent unauthorized access.
    - WPA-PSK: Legacy TKIP encryption, vulnerable to attacks, deprecated.
    - WPA2-PSK: AES-based standard, secure but susceptible to brute-force.
    - WPA-PSK/WPA2-PSK: Mixed mode for backward compatibility, weakest link dictates security.
    - WPA2-PSK/WPA3-SAE: Transitional mode, AES+SAE for future-proofing.
    - WPA3-SAE: Quantum-resistant, SAE protocol, ideal for critical infrastructure.

4. Set a *Password* (a pre-shared key with 8-63 characters or 64 hexadecimal number) for the network authentication.

5. Select a *Mode* (a Wi-Fi standard 802.11n balances range/speed).
    - 802.11b+g+n: Combines legacy (b/g) with modern (n) for maximum compatibility and speed up to 300Mbps.
    - 802.11b+g: Legacy mode for older devices, limited to 54Mbps which avoids in high-density areas.
    - 802.11b: Obsolete 11Mbps, only for vintage equipment. Not recommended.

6. Select *Transmit Power* for the signal strength control.
    - Maximum: 100% power extends coverage to long-range outdoor areas but may increase interference.Suitable for large facilities with sparse device density.
    - Middle: ~50-70% power balances coverage and interference for indoor industrial spaces. Suitable for Medium-sized factories with metal obstructions.
    - Minimum: ≤30% power limits range to small, controlled zones. Suitable for high-density IoT deployments or EMI-sensitive areas.

7. (Optional) Set *Max Stations* for device connection limit based on router capacity.

8. (Optional) Enable *Hidden Network* to avoid SSID broadcast and hide the network from casual scans but offers minimal security. Use only with WPA3 for industrial IoT.

9. (Optional) Enable *Separate Clients* to isolate connected devices and block their communication, critical for IoT security in shared networks.  