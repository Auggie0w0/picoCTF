# Application Security Settings Guide

## Critical Service Settings

### Apache Configuration
- [ ] Secure Apache if installed
sudo nano /etc/apache2/apache2.conf

ServerTokens Prod
ServerSignature Off
TraceEnable Off

sudo a2enmod security2
sudo nano /etc/apache2/conf-available/security.conf

Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-XSS-Protection "1; mode=block"

### MySQL/MariaDB Security
- Secure MySQL installation
sudo mysql_secure_installation

sudo nano /etc/mysql/my.cnf
[mysqld]
bind-address = 127.0.0.1
local-infile=0

### PHP Security
- Configure PHP settings
sudo nano /etc/php/*/apache2/php.ini

expose_php = Off
display_errors = Off
log_errors = On
allow_url_fopen = Off
allow_url_include = Off
max_execution_time = 30
max_input_time = 30
memory_limit = 128M

### Mail Server Security
sudo nano /etc/postfix/main.cf

disable_vrfy_command = yes
smtpd_banner = $myhostname ESMTP

## Required Application Settings
### Browser Security

sudo mkdir -p /usr/lib/firefox/distribution
sudo nano /usr/lib/firefox/distribution/policies.json

{
  "policies": {
    "BlockAboutAddons": true,
    "BlockAboutConfig": true,
    "DisableFirefoxStudies": true,
    "DisableTelemetry": true,
    "ExtensionSettings": {
      "*": {
        "installation_mode": "blocked"
      }
    }
  }
}

### Application Firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable

### Application Logging
sudo nano /etc/rsyslog.conf

*.info;mail.none;authpriv.none;cron.none   /var/log/messages
authpriv.*                                  /var/log/secure

## Application Permissions
### SUID/SGID Review
sudo find / -type f -perm /4000 -ls
sudo find / -type f -perm /2000 -ls

### File Permissions
sudo chmod 644 /etc/passwd
sudo chmod 640 /etc/shadow
sudo chmod 644 /etc/group
sudo chmod 640 /etc/gshadow

### AppArmor Configuration
sudo aa-enforce /etc/apparmor.d/*
sudo systemctl enable apparmor
sudo systemctl start apparmor

### Polkit Rules
sudo nano /etc/polkit-1/localauthority.conf.d/51-ubuntu-admin.conf

### Repository Management
sudo nano /etc/apt/sources.list

- Remove unnecessary repositories
sudo rm -f /etc/apt/sources.list.d/*

### Version Check
dpkg -l | grep apache2
dpkg -l | grep mysql
dpkg -l | grep php

### Clean Up
sudo apt autoremove
sudo apt clean

**verify**

sudo aa-status
sudo ufw status
sudo systemctl status apparmor

**logs**
sudo tail -f /var/log/auth.log
sudo tail -f /var/log/syslog