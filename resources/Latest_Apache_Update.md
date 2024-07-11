# Latest Apache manual install Instructions to address latest CVE Vulnerability

### Date: 2024/07

## Description
- The version of Apache httpd installed on the remote host is prior to 2.4.59. It is, therefore, affected by multiple vulnerabilities as referenced in the 2.4.59 advisory.
- Apache HTTP Server: HTTP Response Splitting in multiple modules: HTTP Response splitting in multiple modules in Apache HTTP Server allows an attacker that can inject malicious response headers into backend applications to cause an HTTP desynchronization attack. Users are recommended to upgrade to version 2.4.59, which fixes this issue. Acknowledgements: (CVE-2024-24795)
- Apache HTTP Server: HTTP/2 DoS by memory exhaustion on endless continuation frames: HTTP/2 incoming headers exceeding the limit are temporarily buffered in nghttp2 in order to generate an informative HTTP 413 response. If a client does not stop sending headers, this leads to memory exhaustion.
Acknowledgements: finder: Bartek Nowotarski (https://nowotarski.info/) (CVE-2024-27316)

## Temporary Fix Instructions
If Apache httpd 2.4.59 is not yet available from the Linux distros officially, you can use these instructions to get the appropriate level of Apache httpd installe.  We have compiled the package from source code. You can follow below instructions to get the Apache httpd binary code and run it on your LinuxONE VM in the LinuxONE Community Cloud. 

1. Delete your current Apache http server from your VM.
2. For RHEL8, RHEL9, SLES15, and Ubuntu, get the Apache 2.4.59
```
wget http://148.100.42.7/packages/apache2_2.4.59_s390x.tar.gz
```
3. Note: for RHEL 8/9 you need to install "wget" package
```
sudo dnf install wget
```
4. Unpack the package
```
tar xvfz apache2_2.4.59_s390x.tar.gz
```
5. After unpack, you will see the files like below. 
```
$ ls
apache2  apache2.service
```
6. Copy `apache2` to `/usr/local/`

7. Note: RHEL 7 packages do not support Apache version 2.4.58

8. Note: For RHEL 9
   
   - You must install libxcrypt-compat.
   ```
   sudo dnf install libxcrypt-compat
   ```
   - You need to add SELinux rule for the apache2 server or disable the SELinux. 

9. If you want to use the systemd to manage the httpd service, copy the file `apache2.service` to your distro's systemd library directory. The directory location varies in different distros. Below is the directory location of each distro:
   - RHEL and SLES: `/usr/lib/systemd/system`
   - Ubuntu: `/lib/systemd/system` 

10. Enable the service and start the http server
   ```
   sudo systemctl enable apache2.service
   ```
   ```
   sudo systemctl start apache2.service
   ```



