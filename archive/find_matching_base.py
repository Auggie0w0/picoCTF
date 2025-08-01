def verify_equality(A, B, a, b, p, expected_s):
    """
    Verify if B^a mod p = A^b mod p = expected_s
    """
    left_side = pow(B, a, p)
    right_side = pow(A, b, p)
    return left_side == right_side == expected_s

def find_possible_exponents(g, A, B, s, p):
    """
    Find possible values of a and b that satisfy:
    g^a mod p = A
    g^b mod p = B
    B^a mod p = A^b mod p = s
    """
    possible_results = []
    
    # Try reasonable ranges for a and b
    for a in range(1, p):
        if pow(g, a, p) == A:
            for b in range(1, p):
                if pow(g, b, p) == B:
                    if verify_equality(A, B, a, b, p, s):
                        possible_results.append((a, b))
    
    return possible_results

def main():
    # Get input values
    p = int(input("Enter p (modulus): "))
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    s = int(input("Enter s (shared secret): "))
    
    print("\nSearching for valid values of g and corresponding a, b pairs...")
    
    found = False
    # Try all possible values of g
    for g in range(2, p):
        results = find_possible_exponents(g, A, B, s, p)
        if results:
            found = True
            print(f"\nFound valid g = {g}")
            for a, b in results:
                print(f"With a = {a}, b = {b}")
                print(f"Verification:")
                print(f"g^a mod p = {pow(g, a, p)} (should be {A})")
                print(f"g^b mod p = {pow(g, b, p)} (should be {B})")
                print(f"B^a mod p = {pow(B, a, p)} (should be {s})")
                print(f"A^b mod p = {pow(A, b, p)} (should be {s})")
                print()
    
    if not found:
        print("\nNo valid values found")

if __name__ == "__main__":
    main()