#!/usr/bin/env python3
"""
RSA Decryption Script
Given N, e, and ciphertext, decrypt the message
"""

import math
import sys

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find gcd and coefficients"""
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

def pollard_rho(n):
    """Pollard's rho algorithm for factorization"""
    if n % 2 == 0:
        return 2
    
    x = 2
    y = 2
    d = 1
    
    def f(x):
        return (x * x + 1) % n
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)
    
    return d if d != n else None

def factorize(n):
    """Factorize n into p and q"""
    print(f"Attempting to factorize N = {n}")
    
    # Try small factors first
    for i in range(2, 1000):
        if n % i == 0:
            return i, n // i
    
    # Use Pollard's rho algorithm
    p = pollard_rho(n)
    if p and p != n:
        q = n // p
        return p, q
    
    return None, None

def rsa_decrypt(ciphertext, d, n):
    """Decrypt RSA ciphertext"""
    return pow(ciphertext, d, n)

def int_to_text(integer):
    """Convert integer to text"""
    # Convert to bytes and then to string
    hex_str = hex(integer)[2:]  # Remove '0x' prefix
    if len(hex_str) % 2:
        hex_str = '0' + hex_str
    
    try:
        # Try to decode as UTF-8
        return bytes.fromhex(hex_str).decode('utf-8')
    except:
        # If UTF-8 fails, try ASCII
        try:
            return bytes.fromhex(hex_str).decode('ascii')
        except:
            # If both fail, return as hex
            return hex_str

def main():
    # RSA parameters from the server
    N = 16305505449518174308916550396856392393287622129492300155512204366452048013564513271957730402062006892984875770905913256741632163444511648244660586819941922
    e = 65537
    ciphertext = 1836730548241977180586657133402209126922765124594635934201333667039935371121635917891127312377046212022858892604604994368142746554214309226282752562812109
    
    print("RSA Decryption Challenge")
    print("=" * 50)
    print(f"N = {N}")
    print(f"e = {e}")
    print(f"Ciphertext = {ciphertext}")
    print()
    
    # Step 1: Factorize N to find p and q
    print("Step 1: Factorizing N...")
    p, q = factorize(N)
    
    if p is None or q is None:
        print("Failed to factorize N. This might be a very large number.")
        print("Trying alternative factorization methods...")
        
        # Try Fermat's factorization method for numbers close to perfect squares
        a = int(math.sqrt(N)) + 1
        while a < N:
            b_squared = a * a - N
            b = int(math.sqrt(b_squared))
            if b * b == b_squared:
                p = a - b
                q = a + b
                if p * q == N:
                    break
            a += 1
        else:
            print("Factorization failed. The number might be too large for these methods.")
            return
    
    print(f"Found factors: p = {p}, q = {q}")
    print(f"Verification: p * q = {p * q}")
    print(f"Matches N: {p * q == N}")
    print()
    
    # Step 2: Calculate phi(N) = (p-1)(q-1)
    phi_n = (p - 1) * (q - 1)
    print(f"Step 2: phi(N) = (p-1)(q-1) = {phi_n}")
    print()
    
    # Step 3: Calculate private key d
    print("Step 3: Calculating private key d...")
    try:
        d = mod_inverse(e, phi_n)
        print(f"Private key d = {d}")
        print(f"Verification: (e * d) mod phi(N) = {(e * d) % phi_n}")
        print()
    except ValueError as e:
        print(f"Error calculating private key: {e}")
        return
    
    # Step 4: Decrypt the ciphertext
    print("Step 4: Decrypting ciphertext...")
    plaintext_int = rsa_decrypt(ciphertext, d, N)
    print(f"Decrypted integer: {plaintext_int}")
    print()
    
    # Step 5: Convert to text
    print("Step 5: Converting to text...")
    plaintext = int_to_text(plaintext_int)
    print(f"Decrypted message: {plaintext}")
    print()
    
    # Try different interpretations
    print("Alternative interpretations:")
    print(f"As hex: {hex(plaintext_int)}")
    print(f"As bytes: {plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big')}")

if __name__ == "__main__":
    main()
