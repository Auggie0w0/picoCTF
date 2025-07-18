def mod_calc(base, exponent, modulus):
    """
    Calculate (base^exponent) mod modulus efficiently using Python's built-in pow function
    
    Args:
        base (int): The base number
        exponent (int): The exponent
        modulus (int): The modulus
    
    Returns:
        int: Result of (base^exponent) mod modulus
    """
    return pow(base, exponent, modulus)

def main():
    # Example usage
    base = int(input("Enter base: "))
    exponent = int(input("Enter exponent: "))
    modulus = int(input("Enter modulus: "))
    
    result = mod_calc(base, exponent, modulus)
    print(f"{base}^{exponent} mod {modulus} = {result}")

if __name__ == "__main__":
    main()