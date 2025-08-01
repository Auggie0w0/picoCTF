# Service Auditing Guide

## Service Status Check

### List Running Services
systemctl list-units --type=service --state=active

systemctl list-unit-files --type=service --state=enabled

### Document Services
systemctl list-units --type=service --all > /var/log/service_inventory.log

sudo ss -tulpn > /var/log/open_ports.log

## Disable Unnecessary Services
### Apache Web Server
systemctl status apache2

sudo systemctl stop apache2
sudo systemctl disable apache2
sudo apt purge apache2*

### SMTP Server
systemctl status postfix

sudo systemctl stop postfix
sudo systemctl disable postfix
sudo apt purge postfix*

### SSH Server
systemctl status ssh

sudo systemctl stop ssh
sudo systemctl disable ssh
sudo apt purge openssh-server

### Other Services
systemctl list-units --type=service | grep -E "cups|bluetooth|avahi|nfs|samba"

sudo systemctl stop service-name
sudo systemctl disable service-name

## Essential Services Configuration
### System Logging
sudo systemctl status rsyslog

sudo nano /etc/rsyslog.conf

### Time Synchronization
sudo systemctl status systemd-timesyncd

sudo systemctl enable systemd-timesyncd
sudo systemctl start systemd-timesyncd

## Service Monitoring
### Real-time Monitoring
sudo journalctl -f

top

### Service Alerts
sudo apt install monit

sudo nano /etc/monit/monitrc

systemctl list-units --type=service --state=failed

systemctl list-unit-files --type=service --state=enabled

tail -f /var/log/syslog

