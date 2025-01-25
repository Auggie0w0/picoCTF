# types of practice

* Web Exploitation
* Cryptography
* Reverse Engineering
* **Forensics**
* General Skills
* Binary Exploitation

# Forensics
## Images
When facing a file with any suffix, CHECK the file type first
* if it is not at risk of damaging the file alter the file suffix to the correct suffix and view (in case of .txt to .png), if risky, make a copy then rename 
* use wireshark or **exiftool** to check details 
* EMBEDED FILES?! --> use **binwalk**
* CHECK THE HEX : xxd filename | less

# Essential notes

## Cipher
**to watch out**
 - MULTIPLE layers of cipher!!! try to check through all the layers! 
    - it was base first, then caesar! 

It's not even funny but for Ceasar Cipher, you have to use this website: [decode.fr](https://www.dcode.fr/caesar-cipher)

## Website
Look for txt files in the html header url 
* Play around with url 
Check CSS or javascript files for clues too

## overflow
| example: 
    python3 -c "print('A' * 100)" | nc saturn.
    picoctf.net 60420 (this was the connection)
    Input: **picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}**
