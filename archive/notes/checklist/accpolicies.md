# Account Policies Configuration Guide

## Password Policy

### Minimum Password Length
- [ ] Set minimum password length to 12 characters

sudo nano /etc/security/pwquality.conf
minlen = 12

### Password Complexity Requirements
sudo nano /etc/security/pwquality.conf
minclass = 4
ucredit = -1
lcredit = -1
dcredit = -1
ocredit = -1

### Password Expiration
sudo nano /etc/login.defs
PASS_MAX_DAYS   90
PASS_MIN_DAYS   7
PASS_WARN_AGE   14

### Password History
sudo nano /etc/pam.d/common-password
password required pam_pwhistory.so remember=5 enforce_for_root

### PAM Settings Configuration
sudo nano /etc/pam.d/common-password
password requisite pam_pwquality.so retry=3
password required pam_pwhistory.so remember=5 enforce_for_root
password [success=1 default=ignore] pam_unix.so obscure sha512 shadow remember=5

### Prevent Password Reuse
sudo chmod 0640 /etc/shadow
sudo chown root:shadow /etc/shadow

## Lockout Policy

### Maximum Login Attempts
sudo nano /etc/pam.d/common-auth
auth required pam_tally2.so deny=5 unlock_time=1800 onerr=fail audit

### Account Lockout Duration
**- To manually unlock an account:**
sudo pam_tally2 --user=USERNAME --reset

### Lockout Counter Reset
sudo nano /etc/pam.d/common-auth
auth required pam_tally2.so deny=5 unlock_time=1800 onerr=fail audit even_deny_root root_unlock_time=1800

### Failed Login Delay
sudo nano /etc/pam.d/login
auth optional pam_faildelay.so delay=4000000

### Additional Security Measures
sudo chmod 644 /etc/pam.d/*
sudo chown root:root /etc/pam.d/*

sudo nano /etc/audit/rules.d/audit.rules

-w /var/log/auth.log -p wa -k auth_log
-w /etc/pam.d/ -p wa -k pam_config


*restart after making changes*
sudo systemctl restart systemd-logind

*verify*
sudo chage -l USERNAME
sudo pam_tally2 --user=USERNAME