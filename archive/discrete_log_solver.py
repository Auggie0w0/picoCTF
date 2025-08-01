def find_discrete_log(g, result, p):
    """
    Find a in the equation: g^a mod p = result
    Using brute force method (only practical for small numbers)
    
    Args:
        g (int): base
        result (int): the result of g^a mod p
        p (int): modulus
    
    Returns:
        int: the value of a, or None if not found
    """
    # Try values from 1 to p-1
    for a in range(1, p):
        if pow(g, a, p) == result:
            return a
    return None

def main():
    # Get input values
    g = int(input("Enter g (base): "))
    result = int(input("Enter the result (g^a mod p): "))
    p = int(input("Enter p (modulus): "))
    
    # Find discrete logarithm
    a = find_discrete_log(g, result, p)
    
    # Print result
    if a is not None:
        print(f"\nFound a = {a}")
        print(f"Verification: {g}^{a} mod {p} = {pow(g, a, p)}")
    else:
        print("\nNo solution found")

if __name__ == "__main__":
    main()