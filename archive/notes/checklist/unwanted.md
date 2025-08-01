# Unwanted Software Removal Guide

## Game Detection and Removal

### Find Gaming Software
find /usr -type d -name "games"
find /home -type d -name "Steam"

dpkg -l | grep -i "game"
dpkg -l | grep -i "steam"

### Remove Gaming Software
sudo apt purge steam* games-*
sudo apt autoremove

sudo rm -rf /home/*/.steam
sudo rm -rf /home/*/.local/share/Steam

## Unnecessary Servers
### Server Detection
dpkg -l | grep -E "apache2|nginx|mysql|postgresql|samba|ftp"

sudo netstat -tulpn | grep LISTEN
sudo ss -tulpn

### Server Removal
sudo systemctl stop apache2 nginx mysql postgresql vsftpd
sudo systemctl disable apache2 nginx mysql postgresql vsftpd

sudo apt purge apache2* nginx* mysql* postgresql* samba* vsftpd*
sudo apt autoremove


## Scareware/Adware Removal
### Detect Suspicious Software
ls -la /etc/xdg/autostart/
ls -la ~/.config/autostart/

dpkg -l | grep -i "toolbar\|addon\|extension"

### Browser Cleanup
rm -rf ~/.mozilla/firefox/*/extensions/*
rm -rf ~/.config/google-chrome/Default/Extensions/*

rm -rf ~/.cache/mozilla/firefox/
rm -rf ~/.cache/google-chrome/

## PUP (Potentially Unwanted Programs)
### PUP Detection
find /opt -type f -exec file {} \;
find /usr/local -type f -exec file {} \;

dpkg -l | grep -i "toolbar\|optimizer\|cleaner"


### PUP Removal
sudo apt purge package-name*

sudo rm -rf /opt/unwanted_program/
sudo rm -rf /usr/local/unwanted_program/

## Hacking Tools
### Tool Detection
dpkg -l | grep -E "nmap|wireshark|ophcrack|metasploit|aircrack"

dpkg -l | grep -E "nmap|wireshark|ophcrack|metasploit|aircrack"


### Tool Removal
sudo apt purge nmap wireshark* ophcrack* aircrack-ng* metasploit*

sudo rm -rf /usr/share/nmap
sudo rm -rf /usr/share/wireshark
sudo rm -rf /usr/share/metasploit*

dpkg -l | grep -i removed

sudo apt clean
sudo apt autoremove

echo "=== Software Removal Report $(date) ===" >> /var/log/software_removal.log
dpkg -l | grep ^rc >> /var/log/software_removal.log