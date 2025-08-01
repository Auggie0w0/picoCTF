# Operating System Updates Guide

## System Package Updates

### Update System Packages

sudo apt update
sudo apt upgrade

sudo apt dist-upgrade

### Security Patches
sudo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades

sudo nano /etc/apt/sources.list.d/security.list

deb http://security.ubuntu.com/ubuntu focal-security main restricted
deb http://security.ubuntu.com/ubuntu focal-security universe
deb http://security.ubuntu.com/ubuntu focal-security multiverse


## Automatic Updates Configuration
### Configure Unattended Upgrades
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades

Unattended-Upgrade::Allowed-Origins {
    "${distro_id}:${distro_codename}-security";
    "${distro_id}:${distro_codename}-updates";
};

Unattended-Upgrade::Package-Blacklist {
};

Unattended-Upgrade::AutoFixInterruptedDpkg "true";
Unattended-Upgrade::MinimalSteps "true";
Unattended-Upgrade::InstallOnShutdown "false";

### Enable Automatic Updates
sudo nano /etc/apt/apt.conf.d/20auto-upgrades

APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "7";
APT::Periodic::Unattended-Upgrade "1";


## Update Source Verification
### Repository Management
sudo nano /etc/apt/sources.list

ls -l /etc/apt/sources.list.d/

### GPG Key Verification
sudo apt-key update
sudo apt-key list

## Update Documentation

### Track Updates
sudo nano /var/log/system-updates.log

dpkg -l > /var/log/installed-packages.log

### Monitor Update Status
cat /var/log/apt/history.log

cat /var/log/unattended-upgrades/unattended-upgrades.log

sudo systemctl status unattended-upgrades
sudo unattended-upgrade --dry-run

apt list --upgradable

tail -f /var/log/apt/term.log
tail -f /var/log/unattended-upgrades/unattended-upgrades.log

