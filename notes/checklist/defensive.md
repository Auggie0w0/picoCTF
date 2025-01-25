# Defensive Countermeasures Guide

## Firewall Configuration

### Enable UFW/iptables
sudo apt install ufw
sudo ufw enable

### Default Policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

### Port Configuration
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp

### Logging Configuration
sudo ufw logging on
sudo ufw logging medium

sudo tail -f /var/log/ufw.log

## Anti-virus Setup
### ClamAV Installation
sudo apt install clamav clamav-daemon

- Configure on-access scanning
sudo nano /etc/clamav/clamd.conf

OnAccessIncludePath /home
OnAccessPrevention yes
OnAccessExcludeUname clamav

### Scheduled Scans
sudo nano /etc/cron.daily/clamav-scan

#!/bin/bash
clamscan -r / --exclude-dir="^/sys|^/proc|^/dev" -l /var/log/clamav/daily.log

sudo chmod +x /etc/cron.daily/clamav-scan

### Quarantine Setup
sudo mkdir -p /var/lib/clamav/quarantine
sudo chown clamav:clamav /var/lib/clamav/quarantine
sudo chmod 750 /var/lib/clamav/quarantine

## Encryption Settings

### SSH Security
sudo nano /etc/ssh/sshd_config

Port 2222
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
Protocol 2

### Disk Encryption
sudo apt install cryptsetup

sudo cryptsetup luksFormat /dev/sdX
sudo cryptsetup luksOpen /dev/sdX secure_volume

### SSL/TLS Configuration
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/server.key -out /etc/ssl/certs/server.crt

### Key-based Authentication
ssh-keygen -t ed25519 -a 100

sudo nano /etc/ssh/sshd_config.d/security.conf

AuthenticationMethods publickey

## Additional Security Measures
### Network Monitoring
sudo apt install net-tools iftop nethogs
sudo nano /etc/cron.hourly/netstat-log

#!/bin/bash
netstat -tuln >> /var/log/netstat.log


### Executable Prevention
sudo nano /etc/fstab
tmpfs   /tmp    tmpfs   defaults,noexec,nosuid,nodev   0   0


### USB Port Control
sudo nano /etc/modprobe.d/block_usb.conf
install usb-storage /bin/true

### Noexec Mount Options
sudo nano /etc/fstab
/dev/sdaX /home ext4 defaults,noexec,nosuid,nodev 0 2

sudo systemctl restart ssh
sudo mount -a

sudo ufw status verbose
sudo freshclam
sudo systemctl status clamav-daemon
sudo sshd -T

sudo tail -f /var/log/auth.log
sudo tail -f /var/log/clamav/freshclam.log