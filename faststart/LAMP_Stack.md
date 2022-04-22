LAMP Stack with WordPress Fast Start Guide
==========================================

Overview
--------

The [LAMP stack](https://www.ibm.com/cloud/learn/lamp-stack-explained), traditionally made up of Linux, Apache, MySQL, and PHP, powered explosive growth of web 2.0. Today it's still a powerful stack, with latest innovations being replacing various components, with Linux remaining the only constant.

In this tutorial, we'll set up a basic LAMP stack using the traditional components, with the new MariaDB in place of MySQL, and deploy the popular blogging software, [WordPress](https://wordpress.org), all on a free virtual machine (VM) on the IBM LinuxONE Community Cloud.

Steps
-----

1. Deploy a Red Hat Enterprise Linux (RHEL) 8 VM

2. Install the components of the LAMP stack using the RHEL package manager

3. Install WordPress

Step 1: Deploy a RHEL 8 VM
--------------------------

If you're not yet familiar with launching a VM in the LinuxONE Community Cloud, refer to our [Virtual Server Deployment Guide](https://github.com/linuxone-community-cloud/technical-resources/blob/master/faststart/deploy-virtual-server.md).

You will have multiple options for which Linux distribution to deploy. For this tutorial, you will want to use the available version of RHEL 8.

Step 2: Install the LAMP stack
------------------------------

Apache on RHEL is installed with a package called "httpd" and referred to it as that throughout use on the system. First, you'll use yum to install it, and then you'll instruct systemctl to start the server, and enable it when you next boot up. Finally, to see if it's running, you can use the status command.

```
sudo yum install httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo systemctl status httpd
```

(hit q to quit)

Now open port 80 in the firewall, so it can be accessed externally:

```
sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
```

Next we'll install the rest of the LAMP stack, a simple text editor (nano), and the packages required for WordPress:

```
sudo yum install php-mysqlnd php-fpm php-json php-gd mariadb-server unzip nano
```

Finally, just like we did with Apache, you'll want to start, enable, and confirm the running status of MariaDB:

```
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo systemctl status mariadb
```

Step 3: Install WordPress
-------------------------

Now that you have your LAMP stack configured, we can start installing WordPress.

Begin by creating a database user and database:


```
mysql -u root
create user 'wordpress'@'localhost' identified by 'YOUR-PASSWORD-CHANGE-ME';
create database wordpress;
grant all on wordpress.* to 'wordpress'@'localhost';
quit
```

Now download and install the latest version of WordPress:

```
curl -O https://wordpress.org/latest.zip
unzip latest.zip
sudo mv wordpress/ /var/www/html/linuxone
sudo chown -R apache:apache /var/www/html/linuxone
```

Restart your httpd server to enable PHP and MariaDB support:

```
sudo systemctl restart httpd
```

Navigate to http://YOUR-IP-ADDRESS/linuxone to begin the installation process.

Complete the installation wizard using the user, database, and password you created above. You will also create a user and password for logging into WordPress, which you should save.

Once the installation is complete, you can log in and start learning how to use WordPress to create your very own blog! Congratulations!
