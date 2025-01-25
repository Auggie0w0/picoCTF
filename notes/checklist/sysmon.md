# System Monitoring Guide

## System Logs Review

### Critical Log Files
tail -f /var/log/syslog
tail -f /var/log/messages

tail -f /var/log/auth.log
grep "Failed password" /var/log/auth.log

### Log Analysis
sudo apt install logwatch

sudo logwatch --detail High --range Today

## Network Monitoring
### Connection Tracking
netstat -tunap
ss -tunap

sudo iftop
sudo nethogs

### Network Analysis
sudo tcpdump -i any -n

sudo apt install vnstat
vnstat -l

## File System Monitoring
### File Changes
sudo apt install inotify-tools
inotifywait -m -r /path/to/monitor

sudo auditctl -w /etc -p wa
sudo auditctl -w /bin -p wa

### Integrity Checking
sudo apt install aide
sudo aideinit

sudo aide --check

## SSH Key Audit
### Key Management
find /home -name "authorized_keys" -ls
find /root -name "authorized_keys" -ls

find /home -name ".ssh" -exec ls -la {} \;

### SSH Configuration
grep "Accepted" /var/log/auth.log

grep "publickey" /var/log/auth.log

## Authentication Monitoring
### Login Attempts
grep "Failed password" /var/log/auth.log
lastb

last
who -a

### Access Control
grep sudo /var/log/auth.log

ausearch -m USER_CMD -sv no

## Unusual Activity Detection
### Process Monitoring

top
ps aux --sort=-%cpu

vmstat 1
iostat 1

### Anomaly Detection
sudo apt install sysstat
sudo nano /etc/default/sysstat

ENABLED="true"

sudo systemctl enable sysstat
sudo systemctl start sysstat

sar -u 1 3
sar -r 1 3

sudo tail -f /var/log/syslog | grep -i "error\|warning\|fail"