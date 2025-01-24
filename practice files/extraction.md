# disk images

## tools

### srch_strings
| srch_strings dds1-alpine.flag.img | grep -i "picoCTF"
Short for Search Strings

### fls or icat to explore or extract data
| fls -r -p -o 2048 dds2-alpine.flag.img | grep down-at-the-bottom.txt
| icat -o 2048 dds2-alpine.flag.img 18291 > down-at-the-bottom.txt

**How to use fls**
fls [-adDFlhpruvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-m dir/] [-o imgoffset] [-z ZONE] [-s seconds] image [images] [inode] If [inode] is not given, the root directory is used

## usage: Sleuthkit Apprentice
1. analyze the mmls, look at the START: 002 & 003 & 004
    002048
    206848
    360448
    * it is supposed to show what kind of file system is used on the image: 

2. inspect with fsstat
    fsstat -o 2048 disk.flag.img
    fsstat -o 306848 disk.flag.img // cannot determine file type!?  
    fsstat -o 360448 disk.flag.img

    * OPTIONAL: If you suspect the file system is EXT, attempt to mount the partitions directly with Mount

3. use fls to list the file and directory names in each partition [-i is the image type, -f is the file system type, and -r is to recursively display directories]

    * raw indicates that the disk image is in raw format (a byte-for-byte copy of a disk, often with extensions like .img, .dd, etc.).

    * -f ext specifies the file system type used within the partition.
	    * ext stands for the family of Linux file systems (e.g., EXT2, EXT3, EXT4).
	    * You must specify this if the file system is not automatically detected.
    
    * -o 2048 the offset in sectors where the partition starts.
	•	This tells fls where to begin analyzing the disk image.

    | grep "flag" --> 2082 (realloc) - flag.txt  & 2371 - flag.uni.txt

4. use **icat** to print the contents of these files to the terminal
    icat -i raw -f ext -o 360448 disk.flag.img 2082

    *2082 is the number indicated for the flag file*



### mml
| mmls dds2-alpine.flag.img

"
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors
"

### DOS Partition Table

| Slot      | Start       | End         | Length      | Description                      |
|-----------|-------------|-------------|-------------|----------------------------------|
| 000: Meta | 0000000000  | 0000000000  | 0000000001  | Primary Table (#0)              |
| 001: -----| 0000000000  | 0000002047  | 0000002048  | Unallocated                     |
| 002: 000:000 | 0000002048 | 0000206847 | 0000204800 | Linux (0x83)                   |
| 003: 000:001 | 0000206848 | 0000360447 | 0000153600 | Linux Swap / Solaris x86 (0x82) |
| 004: 000:002 | 0000360448 | 0000614399 | 0000253952 | Linux (0x83)                   |

**HOW TO READ**
1.	Offset and Sectors:
    * The offset is the starting sector where a partition begins. It’s critical when analyzing or extracting data using tools like dd or Sleuthkit.
    * Each sector is 512 bytes by default (common for most disks).

2.	Partition Types:
    * Linux (0x83): Standard Linux file system partition.
    * Linux Swap / Solaris x86 (0x82): Swap space used for memory management by the OS.
	* Unallocated: Free space on the disk, not assigned to any partition.

3.	Primary Table (#0):
	* Contains metadata about the disk layout. It doesn’t hold user data but describes the structure.

### qemu
to boot a disk image
| qemu-system-x86_64 -drive file= <file>,format=raw -m 512M