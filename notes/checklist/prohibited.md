# Prohibited Files Detection and Removal Guide

## Unauthorized Software Archives

### Archive Detection

sudo find / -type f -name "*.tar.gz" -o -name "*.zip" -o -name "*.rar" -o -name "*.7z"

find /home -type f -name "*.deb" -o -name "*.rpm" -o -name "*.bin"

### Cleanup Process
sudo rm /path/to/unauthorized.zip

echo "$(date) - Removed: [filename]" >> /var/log/file_removal.log


## Prohibited Media Files
### Media File Search
sudo find / -type f -name "*.mp3" -o -name "*.mp4" -o -name "*.avi" -o -name "*.mkv"

sudo find / -type f -name "*.jpg" -o -name "*.png" -o -name "*.gif" -o -name "*.bmp"

### Size-based Detection
sudo find / -type f -size +100M

du -sh /home/*/Downloads
du -sh /home/*/Desktop

## File Type Verification
### File Type Analysis
sudo apt install file
find /home -type f -exec file {} \;

find /home -type f -executable

### Extension Verification
for f in $(find /home -type f); do
    echo "=== $f ==="
    file "$f" | grep -v "$(basename "$f")"
done

### System Analysis
find /tmp -type f
find /var/tmp -type f

find /home -name "*.txt" -o -name "*.doc" -o -name "*.pdf"


## Hidden Directories
### Hidden File Search
sudo find / -name ".*" -ls

ls -la /home/*/.* 2>/dev/null

### Suspicious Locations
find /dev -type f
find /proc -name "*.sh"

find /etc -name ".*" -type f
find /var -name ".*" -type f

echo "=== File Scan Report $(date) ===" >> /var/log/file_scan.log

sudo auditctl -w /home -p wa -k file_changes

sudo ausearch -k file_changes

