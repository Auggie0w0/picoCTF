# CyberPatriot Linux (Mint 21) Security Checklist

## Account Policies
### Password Policy
- [ ] Set minimum password length (12+ characters)
- [ ] Configure password complexity requirements
- [ ] Set password expiration periods
- [ ] Enable password history
- [ ] Configure PAM settings for password policies
- [ ] Prevent password reuse

### Lockout Policy
- [ ] Set maximum login attempts
- [ ] Configure account lockout duration
- [ ] Set account lockout counter reset time
- [ ] Implement failed login delay

## Application Security Settings
### Critical Service Settings
- [ ] Review and secure Apache configurations (if needed)
- [ ] Secure MySQL/MariaDB settings (if installed)
- [ ] Configure PHP security settings (if installed)
- [ ] Review and secure mail server settings (if present)

### Required Application Settings
- [ ] Configure browser security settings
  - [ ] Block dangerous downloads
  - [ ] Restrict content settings
  - [ ] Disable unnecessary plugins
- [ ] Set up application firewalls
- [ ] Configure application logging

### Application Permissions
- [ ] Review SUID/SGID permissions
- [ ] Set appropriate file permissions
- [ ] Configure AppArmor profiles
- [ ] Review and modify polkit rules

## Application Updates
- [ ] Update all installed applications
- [ ] Configure automatic updates
- [ ] Remove unnecessary applications
- [ ] Verify repository sources
- [ ] Check for vulnerable software versions

## Defensive Countermeasures
### Firewall
- [ ] Enable and configure UFW/iptables
- [ ] Set default deny policies
- [ ] Allow only necessary ports
- [ ] Configure logging for blocked attempts

### Anti-virus
- [ ] Install and update ClamAV
- [ ] Configure real-time scanning
- [ ] Schedule regular system scans
- [ ] Set up malware quarantine

### Encryption
- [ ] Enable disk encryption (if required)
- [ ] Configure SSL/TLS settings
- [ ] Secure SSH configurations
  - [ ] Change default port
  - [ ] Disable root login
  - [ ] Use key-based authentication
- [ ] Implement encrypted communications

### Additional Security Measures
- [ ] Configure network monitoring
- [ ] Prevent executable file execution
- [ ] Disable USB ports if not needed
- [ ] Implement noexec mount options

## Local Policies
### Audit Policy
- [ ] Enable system auditing
- [ ] Configure audit rules
- [ ] Set up log rotation
- [ ] Monitor critical file access

### User Rights Assignment
- [ ] Review sudo configurations
- [ ] Set up proper group permissions
- [ ] Configure access control lists
- [ ] Review user privileges

### Security Options
- [ ] Configure network security options
- [ ] Set up privilege elevation controls
- [ ] Configure system-wide security settings
- [ ] Review and modify kernel parameters

## Operating System Updates
- [ ] Update system packages
- [ ] Install security patches
- [ ] Configure automatic system updates
- [ ] Verify update sources
- [ ] Document installed updates

## Policy Violation: Malware
- [ ] Scan for and remove:
  - [ ] Backdoors
  - [ ] Remote Administration Tools
  - [ ] Keyloggers
  - [ ] Password Sniffers
- [ ] Install and run RKHunter
- [ ] Monitor suspicious processes
- [ ] Check startup applications

## Policy Violation: Prohibited Files
- [ ] Remove unauthorized software archives
- [ ] Check for prohibited media files
- [ ] Verify allowed file types
- [ ] Remove forensics question-related files
- [ ] Check hidden directories

## Policy Violation: Unwanted Software
- [ ] Remove:
  - [ ] Games
  - [ ] Unnecessary servers
  - [ ] Scareware/Adware
  - [ ] PUPs (Potentially Unwanted Programs)
  - [ ] Hacking tools (Ophcrack, Nmap, Wireshark)
- [ ] Document removed software

## Service Auditing
- [ ] Disable unnecessary services:
  - [ ] Apache (if not required)
  - [ ] SMTP (if not required)
  - [ ] OpenSSH (if not required)
  - [ ] Other unused services
- [ ] Configure essential services
- [ ] Document running services
- [ ] Monitor service status

## Miscellaneous
- [ ] Configure remote access settings
- [ ] Set up file sharing restrictions
- [ ] Enable screen locking
- [ ] Configure group policies
- [ ] Set operating system permissions
- [ ] Install OSSEC monitoring system
- [ ] Take system snapshots at key points
- [ ] Configure DNS settings

## User Auditing
- [ ] Review authorized users
- [ ] Audit user groups
- [ ] Check sudo privileges
- [ ] Review login configurations
- [ ] Monitor user activities
- [ ] Set up user-specific restrictions

## System Monitoring
- [ ] Review system logs
- [ ] Monitor network connections
- [ ] Track file system changes
- [ ] Audit SSH keys
- [ ] Monitor authentication attempts
- [ ] Check for unusual activities

## Documentation
- [ ] Document all changes made
- [ ] Keep track of removed software
- [ ] Record configuration changes
- [ ] Note security implementations
- [ ] Document user modifications