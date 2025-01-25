# Miscellaneous Security Settings Guide

## Remote Access Configuration

### SSH Settings
sudo nano /etc/ssh/sshd_config

PermitRootLogin no
AllowUsers [specific_user]
Protocol 2
MaxAuthTries 3

### VNC Settings
sudo systemctl stop vino
sudo systemctl disable vino

## File Sharing Controls
### Samba Configuration
sudo nano /etc/samba/smb.conf

[global]
    restrict anonymous = 2
    map to guest = never

### NFS Restrictions
sudo nano /etc/exports

/shared *(ro,no_root_squash)

## Screen Lock Settings
### Configure Screen Lock
gsettings set org.gnome.desktop.screensaver lock-enabled true
gsettings set org.gnome.desktop.screensaver lock-delay 300

### Lock Screen Security
gsettings set org.gnome.desktop.screensaver user-switch-enabled false

## Group Policy Settings
### User Group Policies
sudo groupadd restricted_users
sudo groupadd power_users

### Policy Configuration
sudo nano /etc/security/access.conf

+:power_users:ALL
-:restricted_users:ALL EXCEPT LOCAL

## Operating System Permissions
### File System Permissions
sudo chmod 644 /etc/passwd
sudo chmod 640 /etc/shadow
sudo chmod 644 /etc/group

### Directory Permissions
sudo chmod 755 /home
sudo chmod 700 /home/*

## OSSEC Installation
### Install OSSEC

sudo apt install ossec-hids

### Configure OSSEC
sudo nano /var/ossec/etc/ossec.conf

<ossec_config>
  <global>
    <email_notification>no</email_notification>
  </global>
  <syscheck>
    <frequency>7200</frequency>
  </syscheck>
</ossec_config>


## DNS Configuration
### DNS Settings
sudo nano /etc/systemd/resolved.conf

[Resolve]
DNS=1.1.1.1 1.0.0.1
DNSStubListener=no

### DNS Security
sudo nano /etc/systemd/resolved.conf
[Resolve]
DNSSEC=true

sudo systemctl restart systemd-resolved

sudo systemctl status systemd-resolved

sudo tail -f /var/log/syslog
sudo tail -f /var/ossec/logs/alerts/alerts.log