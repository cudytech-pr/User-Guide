# Log in / Log out

???+ Note
    Images of GS1024E are for reference only; details may vary by model.

## Log in

The switch supports further management on the GUI web page. Log into it and start management.

???+ Tip
    If your model has a DIP switch, make sure it is set to **Managed**.
        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/switch/login-0.webp" alt="" width="400px" style="border: 1px solid #eee; display:block; margin:0 auto;" />

1. Connect your computer to the switch with an Ethernet cable, and set its IP address to *192.168.2.x* (x ranges from 2 to254) and subnet mask to *255.255.255.0*.
   
2. Open a web browser, enter 192.168.2.1 in the address bar and press Enter. 

3. Create and confirm a new password, and enable *Cloud Management*, *Dynamic IP* and *Auto DNS* to allow cloud management via the Cudy App.

    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/login.webp" alt="" width="300px" style="border: 1px solid #eee; display:block; margin:0 auto;" />

    ???+ Note
        - Firmware upgrade may be required for earlier versions.
        - Keep your password secure. If forgotten, press the Reset button to restore factory settings.

4. Scan the QR code to download Cudy App on your smart device for remote management. You can also manage the switch via the web interface locally.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/downloadapp.svg" alt="" width="300px" style="border: 1px solid #eee; display:block; margin:0 auto;" />

---

## Log out
To securely end the current management and ensure that no unauthorized access can occur until a new login is performed. This feature helps protect the switch configuration and management settings from potential security breaches.

<img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/switch/logout.webp" alt="" width="800px" style="border: 1px solid #eee; display:block; margin:0 auto;" />