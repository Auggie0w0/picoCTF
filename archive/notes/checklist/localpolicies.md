# Local Policies Configuration Guide

## Audit Policy

### System Auditing

sudo apt install auditd
sudo systemctl enable auditd
sudo systemctl start auditd

### Audit Rules Configuration
sudo nano /etc/audit/rules.d/audit.rules

-w /etc/passwd -p wa -k user_changes
-w /etc/group -p wa -k group_changes
-w /etc/shadow -p wa -k shadow_changes
-w /etc/sudoers -p wa -k sudoers_changes
-w /var/log/auth.log -p wa -k auth_log
-w /etc/ssh/sshd_config -p wa -k sshd_config

### Log Rotation
sudo nano /etc/logrotate.d/audit

/var/log/audit/audit.log {
    rotate 7
    daily
    missingok
    notifempty
    compress
    delaycompress
    copytruncate
}

### Critical File Monitoring
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
sudo auditctl -w /etc/shadow -p wa -k shadow_changes
sudo auditctl -w /var/log/auth.log -p wa -k auth_log_changes

## User Rights Assignment
### Sudo Configuration
sudo visudo

Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

### Group Permissions
sudo groupadd admin_users
sudo groupadd restricted_users

sudo nano /etc/login.defs

UMASK           027
USERGROUPS_ENAB yes

### Access Control Lists
sudo apt install acl

sudo setfacl -m g:admin_users:rwx /path/to/admin/directory
sudo setfacl -m g:restricted_users:rx /path/to/restricted/directory

### User Privileges Review
for user in $(cut -f1 -d: /etc/passwd); do
    echo "---[$user]---"
    groups $user
    sudo -l -U $user
done


## Security Options
### Network Security
sudo nano /etc/sysctl.conf

net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.all.log_martians = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.tcp_syncookies = 1

### Privilege Elevation
sudo nano /etc/sudoers.d/privilege_limits

Defaults        requiretty
Defaults        !visiblepw
Defaults        use_pty

### System-wide Security
sudo nano /etc/security/limits.conf

*               hard    core            0
*               hard    maxlogins       10
*               hard    nproc           100

### Kernel Parameters
sudo nano /etc/sysctl.d/10-security-hardening.conf

kernel.randomize_va_space = 2
kernel.dmesg_restrict = 1
kernel.kptr_restrict = 2
fs.suid_dumpable = 0

sudo sysctl -p
sudo service auditd restart

sudo auditctl -l
sudo sysctl -a | grep security
sudo getfacl /path/to/directory

sudo ausearch -k auth_log
sudo aureport --summary

sudo sestatus
sudo apparmor_status