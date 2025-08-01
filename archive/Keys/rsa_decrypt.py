from Crypto.Util.number import inverse, long_to_bytes

# Given values
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537

def factorize_n(n):
    p = 1955175890537890492055221842734816092141
    q = 670577792467509699665091201633524389157003
    return p, q

try:
    # Step 1: Factor n to find p and q
    p, q = factorize_n(n)
    
    # Step 2: Calculate phi(n)
    phi = (p - 1) * (q - 1)
    
    # Step 3: Find private key d
    d = inverse(e, phi)
    
    # Step 4: Decrypt the message
    m = pow(c, d, n)
    
    # Step 5: Convert to text
    decrypted = long_to_bytes(m)
    print(f"Decrypted message: {decrypted}")

except Exception as e:
    print(f"Error: {e}")
    print("Try using factordb.com to factor n")