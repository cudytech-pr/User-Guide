
# How to manage Cudy AP controller remotely? 

???+ Note
    - C200P is used as an example below. Refer to your actual product for more details.

### Step 1. Connect the AP controller.

Make sure you have [connected your AP controller](../user_guide/ap_controller/connection.md) and powered it on.

### Step 2. Enable *Cloud Management* on [cudyac.net](http://cudyac.net).

- If this is your first login to [cudyac.net](http://cudyac.net), just follow the [Quick Setup](../user_guide/ap_controller/quick_setup.md) and enable *Cloud Management* in the *System* step.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/qs5.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;">   
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/qsa4.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;">       

- If you have already completed Quick Setup before, just log in to [cudyac.net](http://cudyac.net) with your password, and go to *Advanced Settings >> System >> Cloud Management* to enable *Cloud Management* and click *Save & Apply*. 
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/advanced_cloud.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;" >   

???+ Note
    - Before proceeding, ensure that the *Cloud Status* is **Ready to Bind**. If it is *Offline*, check your Internet connection.
    - Note down the *Serial Number* for later use. It is also available on the product label.

### Step 3. Bind the AP controller with your Cudy account.

- Go to [Cudy Cloud](http://cloud.cudy.com) at [cloud.cudy.com](http://cloud.cudy.com), log in your Cudy account. *Create account* first if you don't have one.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/cloud_log.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;" >   

- Click *Add* or *Add Device*.
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/cloud_add.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;" >


- Enter the AP controller's *Serial Number* and its web login *Password*. Click *Confirm* to bind it. 
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/sn_pw.webp" width="400px" style="border:  2px solid #eee;display: block; margin: 0 auto;" >

- Once bound successfully, you can remotely manage the AP in [Cudy Cloud](http://cloud.cudy.com) by clicking its device name or the operation icon <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/config.webp" width="25px">. 
    <img src="https://cdn.jsdelivr.net/gh/Cudytech-pr/User-Guide/docs/images/ap_controller/bond.webp" width="700px" style="border:  2px solid #eee;display: block; margin: 0 auto;" >   

    ???+ Tips
        You can check the binding status on [cudyac.net](http://cudyac.net), either in the upper-right corner or under *Advanced Settings >> System >> Cloud Management*, as well as in the [Cudy Cloud](http://cloud.cudy.com) Device List. You can also unbind the device or switch to another Cudy account there.
