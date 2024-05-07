Virtual Server Deployment Guide
===============================

Overview
--------

This document will take you through the steps to get access to the LinuxONE
community cloud, deploy a virtual server and start using it in your project or
in one of the Fast Start Guides.

Steps
-----

1.  Request access to LinuxONE Community Cloud

2.  First time setup

3.  Deploy your LinuxONE virtual server

4.  Log in to your LinuxONE virtual server

Step 1. Request access to LinuxONE Community Cloud.
---------------------------------------------------

1.  In a browser, go to the [LinuxONE Community Cloud
    website](https://community.ibm.com/zsystems/l1cc/).

    ![alt text](images-deploy/dev-homeNEW.png)

2.  Click **Try Virtual Machines on the LinuxONE Community Cloud**.

3.  Complete the required fields on the registration form. **Note:** If you were
    given en **Event Code** please enter it, if not leave it blank)

    ![alt text](images-deploy/registration-form.png)

4.  Complete your registration by clicking **Request your trial**.

    ![alt text](images-deploy/request-your-trial.png)

5.  Check your email for a registration confirmation similar to the following
    shown. You will need your User ID and Password from this email to sign in to
    the self service portal.

    ![alt text](images-deploy/welcome-email.png)

First time setup
----------------

1.  After activating your account, log in at
    https://linuxone.cloud.marist.edu/#/login

-   Enter your **user ID** and the **password** created during registration.

-   Click **Sign in**.

    ![alt text](images-deploy/ssp-login.png)

1.  Now is also a good time to create or import an SSH key. An SSH public key is
    required to deploy Linux instance. The instance can only be accessed with
    your private key that matches the public key. You can generate one now or
    wait until you deploy your first instance.

-   Click **Virtual Servers** in the upper left corner of the page.

-   Next click your **username** from the upper right corner of the Home page.

-   Select **Manage SSH Key Pairs**.

    ![alt text](images-deploy/manage-key.png)

1.  If you already have a public SSH key you wish to use with this cloud:

    -   Click **Import**.

    -   Enter a **Key Name** for this key.

    -   Browse your local file system to select the **public key path**.

    -   Click **Upload your public key**.

        ![alt text](images-deploy/upload-key.png)

2.  If you want to create a new SSH key pair:  
    

-   Click **Create**.

-   Enter a **Key Name** for this key.

-   Click **Create a new key pair**.  
    

-   A pop-up window will appear asking you to save **yourkey. pem** file. This
    is your private key. Please save it to a secure location. Once this
    operation is complete, there is no way to retrieve this key. Click **OK** to
    save the file.

![alt text](images-deploy/create-key.png)

![alt text](images-deploy/pem-file.png)

Deploy your LinuxONE virtual server
-----------------------------------

1.  Go to the **Home** page, **Service Catalog** section and **Virtual Servers**
    service.

-   Click **Manage Instances**.

    ![alt text](images-deploy/manage-instances.png)

-   Click **Create**.

    ![alt text](images-deploy/create-server.png)

1.  Your Virtual Server type will automatically be "General purpose VM".

2.  Provide details information for this instance.

-   An **Instance Name**, without any spaces or special characters.

1.  Select the desired Linux image.

    ![alt text](images-deploy/create-server-image.png)

2.  Select the Flavor (There is only one at this time).

    ![alt text](images-deploy/select-flavor.png)

3.  Select the SSH key to use.

    ![alt text](images-deploy/create-server-select-key.png)

4.  Verify that all the information is correct and click **Create**.

    ![alt text](images-deploy/create-server-submit.png)

5.  Watch the status of your newly deployed instance go through the following
    phases of start up: *NETWORKING*, *SPAWNING*, *ACTIVE*. When your instance
    status changes to *ACTIVE*, it is ready for use.

    ![alt text](images-deploy/create-server-status.png)

    Write down the IP address of your instance. You will need it to log in.

Log in to your LinuxONE virtual server
--------------------------------------

### From Mac OS X or Linux using Terminal

1.  Open a Terminal application.

2.  Ensure that you have the SSH private key used to deploy the server.

3.  If you have not done so already, change the permission bits of this key to
    600.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # chmod 600 /path/to/key/keyname.pem  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4.  Use SSH to access the Linux guest.

-   UserID: linux1

-   `-i` lets SSH know which identity file to use access the Linux guest.

-   Serveripaddress: This was written down from the *Manage Instances* page of
    the LinuxONE Community Cloud.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ssh –i /path/to/key/keyname.pem linux1@serveripaddress 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### From Windows using PuTTY

1.  Set up PuTTY to use the SSH key for your server. Refer to the [Setting up
    PUTTY on Windows to use ssh private key](PUTTY_Set_up.pdf) tutorial.

2.  Log in to the linux1 user ID.

Important notes about your server:
----------------------------------

1.  You must log in with the user ‘linux1’ with your SSH private key. No
    modification (use of password authentication, for example) is allowed.

2.  The user ‘root’ login is disabled for security reasons. No modification is
    allowed.

3.  You can use ‘sudo’ to execute commands that require root authority.
  
4.  There is no backup for your virtual server. It is the end user’s
    responsibility to back up any critical data.

5.  Firewall is enabled via iptables rules. Only the SSH port is open by default. Modify the firewall rules
    with iptables if you need other ports opened. To check your current enabled iptables rules, issue this command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sudo iptables -L
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


For SLES:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sudo iptables -I INPUT -p tcp --dport <port#> -j ACCEPT 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to make your changes permanently, issue this command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sudo bash -c "iptables-save > /etc/linuxone/iptables.save"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: If you want to use firewall management tool like firewalld, you need to delete the saved iptables file.


For RHEL:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sudo iptables -I INPUT -p tcp --dport <port#> -j ACCEPT 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to make your changes permanently, issue this command:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sudo bash -c "iptables-save > /etc/sysconfig/iptables.save"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: If you want to use firewall management tool like firewalld, you need to delete the saved iptables file.


For Ubuntu:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sudo iptables -I INPUT -p tcp --dport <port#> -j ACCEPT 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to make your changes permanently, issue this command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sudo bash -c "iptables-save > /etc/iptables/rules.v4" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: If you want to use firewall management tool like ufw, you need to delete the saved iptables file.


