#!/usr/bin/env python3
"""
Optimized RSA Decryption Script
For CTF challenges with small factors
"""

import math

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi_n):
    """Find modular inverse of e mod phi_n"""
    gcd, x, y = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("Modular inverse doesn't exist")
    return x % phi_n

def rsa_decrypt(ciphertext, d, n):
    """Decrypt RSA ciphertext"""
    return pow(ciphertext, d, n)

def int_to_text(integer):
    """Convert integer to text"""
    hex_str = hex(integer)[2:]
    if len(hex_str) % 2:
        hex_str = '0' + hex_str
    
    try:
        return bytes.fromhex(hex_str).decode('utf-8')
    except:
        try:
            return bytes.fromhex(hex_str).decode('ascii')
        except:
            return hex_str

def main():
    # RSA parameters
    N = 16305505449518174308916550396856392393287622129492300155512204366452048013564513271957730402062006892984875770905913256741632163444511648244660586819941922
    e = 65537
    ciphertext = 1836730548241977180586657133402209126922765124594635934201333667039935371121635917891127312377046212022858892604604994368142746554214309226282752562812109
    
    print("RSA Decryption")
    print("=" * 30)
    
    # Factorize N (check for small factors first)
    print("Factorizing N...")
    p = 2  # Found that N is even
    q = N // p
    
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"Verification: p * q = N? {p * q == N}")
    
    # Calculate phi(N) and private key
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    
    print(f"phi(N) = {phi_n}")
    print(f"Private key d = {d}")
    
    # Decrypt
    plaintext_int = rsa_decrypt(ciphertext, d, N)
    plaintext = int_to_text(plaintext_int)
    
    print(f"\nDecrypted message: {plaintext}")
    print(f"Flag: {plaintext}")

if __name__ == "__main__":
    main()
