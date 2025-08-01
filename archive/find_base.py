def verify_base(g, a, b, A, B, s, p):
    """
    Verify if a base g satisfies all the Diffie-Hellman conditions:
    - A = g^a mod p
    - B = g^b mod p
    - s = A^b mod p = B^a mod p
    """
    if A is not None and a is not None:
        if pow(g, a, p) != A:
            return False
    
    if B is not None and b is not None:
        if pow(g, b, p) != B:
            return False
    
    if s is not None and a is not None and B is not None:
        if pow(B, a, p) != s:
            return False
    
    if s is not None and b is not None and A is not None:
        if pow(A, b, p) != s:
            return False
            
    return True

def find_base(a, b, A, B, s, p):
    """
    Find possible values of g that satisfy the Diffie-Hellman conditions
    """
    valid_bases = []
    
    # Try all possible values of g from 2 to p-1
    for g in range(2, p):
        if verify_base(g, a, b, A, B, s, p):
            valid_bases.append(g)
    
    return valid_bases

def find_exponents(A, B, s, p):
    """
    Find possible values of a and b that satisfy:
    A = g^a mod p
    B = g^b mod p
    s = A^b mod p = B^a mod p
    """
    possible_pairs = []
    
    # Try values for a
    for a in range(1, p):
        # Check if B^a mod p equals s
        if pow(B, a, p) == s:
            # Try values for b
            for b in range(1, p):
                # Check if A^b mod p equals s
                if pow(A, b, p) == s:
                    possible_pairs.append((a, b))
                    break
            break
    
    return possible_pairs

def find_a(g, b, A, B, s, p):
    """
    Find the value of a given g, b, A, B, s, and p
    """
    for a in range(1, p):
        if pow(g, a, p) == A and pow(B, a, p) == s:
            return a
    return None

def main():
    # Get input values
    p = int(input("Enter p (modulus): "))
    a = input("Enter a (or press Enter if unknown): ")
    b = input("Enter b (or press Enter if unknown): ")
    A = input("Enter A (or press Enter if unknown): ")
    B = input("Enter B (or press Enter if unknown): ")
    s = input("Enter s (or press Enter if unknown): ")
    
    # Convert inputs to integers or None
    a = int(a) if a else None
    b = int(b) if b else None
    A = int(A) if A else None
    B = int(B) if B else None
    s = int(s) if s else None
    
    # Find possible exponents if we have A, B, s, and p
    if all(x is not None for x in [A, B, s, p]):
        possible_pairs = find_exponents(A, B, s, p)
        if possible_pairs:
            print("\nFound possible values for a and b:")
            for a, b in possible_pairs:
                print(f"a = {a}, b = {b}")
                print(f"Verification: B^a mod p = {pow(B, a, p)} (should be {s})")
                print(f"Verification: A^b mod p = {pow(A, b, p)} (should be {s})")
                print()
    
    # Find possible bases
    valid_bases = find_base(a, b, A, B, s, p)
    
    # If g is known, try to find a
    g = 185  # Known g value
    if b is not None and A is not None and B is not None and s is not None:
        found_a = find_a(g, b, A, B, s, p)
        if found_a is not None:
            print(f"\nFound value for a: {found_a}")
            print(f"Verification g^a mod p = {pow(g, found_a, p)} (should be {A})")
            print(f"Verification B^a mod p = {pow(B, found_a, p)} (should be {s})")
    
    # Print results
    if valid_bases:
        print("\nFound possible values for g:")
        for g in valid_bases:
            print(f"g = {g}")
            if a is not None:
                print(f"Verification: {g}^{a} mod {p} = {pow(g, a, p)}")
            if b is not None:
                print(f"Verification: {g}^{b} mod {p} = {pow(g, b, p)}")
            print()
    else:
        print("\nNo valid base g found")

if __name__ == "__main__":
    main()