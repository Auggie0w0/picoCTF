def find_a(g, b, A, B, s, p):
    """
    Find the value of a given:
    - g^a mod p = A
    - g^b mod p = B
    - A^b mod p = B^a mod p = s
    """
    for a in range(1, p):
        # Check if g^a mod p = A
        if pow(g, a, p) == A:
            # Verify B^a mod p = s
            if pow(B, a, p) == s:
                return a
    return None

def main():
    # Known values
    p = 2347702307
    b = 1225407059
    A = 1747990017
    B = 1218107839
    s = 640301648
    g = 185

    # Find a
    a = find_a(g, b, A, B, s, p)
    
    if a:
        print(f"Found a = {a}")
        print("\nVerification:")
        print(f"1. g^a mod p = {pow(g, a, p)} (should be {A})")
        print(f"2. B^a mod p = {pow(B, a, p)} (should be {s})")
    else:
        print("No valid value of 'a' found")

if __name__ == "__main__":
    main()