# User Auditing Guide

## Authorized Users Review

### List Users
cat /etc/passwd

last
lastlog

### User Account Status
passwd -S -a

chage -l username

## Group Audit
### Group Membership
cat /etc/group
getent group

groups username
id username

### Group Permissions
ls -l /etc/group
ls -l /etc/gshadow

find / -group groupname

## Sudo Privileges
### Sudo Configuration
sudo cat /etc/sudoers
ls -l /etc/sudoers.d/

getent group sudo
getent group wheel

### Sudo Usage Audit
grep sudo /var/log/auth.log

echo 'Defaults logfile="/var/log/sudo.log"' | sudo tee /etc/sudoers.d/99-logging

## Login Configuration
### Login Settings
cat /etc/login.defs

cat /etc/pam.d/common-auth
cat /etc/pam.d/common-account

### Login Restrictions
sudo nano /etc/security/time.conf

- Set up access time limits
*;*;user;Al0800-1700

## User Activity Monitoring
### Activity Logging
sudo apt install acct
sudo accton on

sudo apt install snoopy

### Log Review
sa
lastcomm username

grep "session opened" /var/log/auth.log

## User Restriction
### Shell Restrictions
usermod -s /bin/rbash username

echo "username:rbash" | sudo tee -a /etc/shells

### Directory Restrictions
chmod 750 /home/username

setfacl -m u:username:rx /path/to/directory

tail -f /var/log/auth.log

find /home -name ".*history" -exec ls -la {} \;

who
w