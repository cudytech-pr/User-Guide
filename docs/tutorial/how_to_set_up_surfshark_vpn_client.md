# How to set up Surfshark VPN clients?

???+ Info
    - Cudy routers provide a dedicated Surfshark VPN client interface. You can configure your Surfshark VPN account directly on the router to establish a secure VPN connection for all devices connected to the network.
    - This feature is available for Cudy routers with firmware version 2.5.0+ and Cudy App version 1.5.5+. 
    - TR3000 is shown as an example in this tutorial.

## Using Cudy App

1. Connect your phone to the router's Wi-Fi network. 

2. Open the Cudy App on your phone. Tick *I agree with ...* and select *Local Management*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/cudy1.webp" width="300px" style="display: block; margin: 0 auto;">   

    ???+ Tip
        Scan the QR code to download it first if needed.

        <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/faq/10007/1_Cudy_APP_QR.webp" width="200px" style="display: block; margin: 0 auto;">   

3. Select *Wi-Fi Device*. 
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/select_device_type.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

    ???+ Tip
        If you have before managed other type of devices on Cudy App, you may need to tap the menu icon (☰) on the left of Dashboard to switch to *Wi-Fi Device*.

4. Tap the router. 
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/tap_on_tr3000.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

5. Enter the router's administrator password. (Create one for an initial login to the management page either via web interface or Cudy App.)
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/password.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">  

6. Scroll down and tap *More*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/more.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

7. Find and tap *VPN*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/vpn.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

8. Tap *VPN Client*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/vpn_client.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

9. Tap *Add*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/add_vc.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

10. Tap *Surfshark*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/add_surfshark.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

11. Enter your Surfshark account *Username* and *Password*, and click *Continue*. 
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/surfshark_account.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   
    
    ???+ Tip
        - Don't have an account yet? Click *Get Started* to create one. Visit our partner link [https://surfshark.com/](https://get.surfshark.net/aff_c?offer_id=1941&aff_id=46950) to learn more about available offers.
        - You may be required to enter a 2FA code, if 2FA is enabled on your Surfshark account. Find it in your email or authenticator app.

12. Select a *Default Rule* and *VPN Policy*. Search and select a server. Tap the ✔ icon at the top right to save and apply.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/surfshark_config.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

    ???+ Explanation
        - *Allow All Devices*: by default allows all devices to use the VPN connection unless a policy rule specifies otherwise. 
        - *Ban All Devices*: by default prevents all devices from using the VPN connection unless a policy rule explicitly allows them to use it.
        - *Disable*: disables the VPN policy rule, then traffic matching this rule is not affected by the policy. 
        - *VPN Kill Switch*: blocks internet access if the VPN connection is lost, preventing traffic from being sent outside the VPN tunnel. 
        - *Domain*: applies the VPN policy to specific domain names, and you need to enter one or more domains, such as `example.com`. 
        - *Remote Subnet*: applies the VPN policy to a specific destination network, and you need to enter the subnet in CIDR notation, such as `192.168.10.0/24`.

13. Toggle on to activate this VPN client profile. You can view, edit, or delete this profile as needed.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/surfshark_connected.webp" width="300px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   


## Using Web Interface

1. Log in your router's web interface at [cudy.net](http://cudy.net) (or [192.168.10.1](http://192.168.10.1)).

2. Go to *General Settings > VPN > VPN Client*. Click *Add*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/vpn1.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

3. Click *Surfshark* in the VPN Client pop-up window.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/vpn2.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

4. Enter your Surfshark account *Username* and *Password*, and click *Continue*. 
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/vpn3.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

    ???+ Tip
        - Don't have an account yet? Click *Get Started* to create one. Visit our partner link [https://surfshark.com/](https://get.surfshark.net/aff_c?offer_id=1941&aff_id=46950) to learn more about available offers.

        - You may be required to enter a 2FA code, if 2FA is enabled on your Surfshark account. Find it in your email or authenticator app.

5. Create a *Description*, select a *Default Rule* and *VPN Policy*. Search and select a server. Click *Save & Apply*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/vpn5.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   

    ???+ Explanation
        - *Allow All Devices*: by default allows all devices to use the VPN connection unless a policy rule specifies otherwise. 
        - *Ban All Devices*: by default prevents all devices from using the VPN connection unless a policy rule explicitly allows them to use it.
        - *Disable*: disables the VPN policy rule, then traffic matching this rule is not affected by the policy. 
        - *VPN Kill Switch*: blocks internet access if the VPN connection is lost, preventing traffic from being sent outside the VPN tunnel. 
        - *Domain*: applies the VPN policy to specific domain names, and you need to enter one or more domains, such as `example.com`. 
        - *Remote Subnet*: applies the VPN policy to a specific destination network, and you need to enter the subnet in CIDR notation, such as `192.168.10.0/24`.

6. Toggle *Enable* to activate this VPN client profile. You can view, edit, or delete this profile as needed.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/tutorial/vpn7.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   