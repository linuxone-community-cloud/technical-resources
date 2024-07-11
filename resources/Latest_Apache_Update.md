# Latest Apache manual install Instructions to address latest CVE Vulnerability

### Date: 2024/07

## Description
- The version of Apache httpd installed on the remote host is prior to 2.4.58. It is, therefore, affected by multiple vulnerabilities as referenced in the 2.4.58 advisory.
- mod_macro buffer over-read: Out-of-bounds Read vulnerability in mod_macro of Apache HTTP Server.This issue affects Apache HTTP Server: through 2.4.57. Acknowledgements: finder: David Shoon (github/davidshoon) (CVE-2023-31122)
- Apache HTTP Server: DoS in HTTP/2 with initial windows size 0: An attacker, opening a HTTP/2 connection with an initial window size of 0, was able to block handling of that connection indefinitely in Apache HTTP Server. This could be used to exhaust worker resources in the server, similar to the well known slow loris attack pattern. This has been fixed in version 2.4.58, so that such connection are terminated properly after the configured connection timeout. This issue affects Apache HTTP Server: from 2.4.55 through 2.4.57. Users are recommended to upgrade to version 2.4.58, which fixes the issue.
Acknowledgements: (CVE-2023-43622)
- Apache HTTP Server: HTTP/2 stream memory not reclaimed right away on RST: When a HTTP/2 stream was reset (RST frame) by a client, there was a time window were the request's memory resources were not reclaimed immediately. Instead, de-allocation was deferred to connection close. A client could send new requests and resets, keeping the connection busy and open and causing the memory footprint to keep
on growing. On connection close, all resources were reclaimed, but the process might run out of memory before that. This was found by the reporter during testing of CVE-2023-44487 (HTTP/2 Rapid Reset Exploit) with their own test client. During normal HTTP/2 use, the probability to hit this bug is very low. The kept memory would not become noticeable before the connection closes or times out. Users are recommended to upgrade to version 2.4.58, which fixes the issue. Acknowledgements: (CVE-2023-45802)

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



