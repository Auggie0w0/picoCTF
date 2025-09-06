def caesar_decode(ciphertext, shift):
    """
    Decode a Caesar cipher by shifting each letter by the specified amount.
    
    Args:
        ciphertext (str): The encoded message
        shift (int): The number of positions to shift each letter
        
    Returns:
        str: The decoded message
    """
    result = ""
    
    for char in ciphertext:
        if char.isalpha():
            # Determine ASCII offset (97 for lowercase, 65 for uppercase)
            ascii_offset = 97 if char.islower() else 65
            
            # Convert to 0-25, shift, and wrap around with modulo
            shifted = (ord(char) - ascii_offset - shift) % 26
            
            # Convert back to ASCII and add to result
            result += chr(shifted + ascii_offset)
        else:
            # Keep non-alphabetic characters as they are
            result += char
            
    return result

def main():
    # Prompt the user to input the encoded message
    ciphertext = input("Enter the encoded message (ciphertext): ")
    print("Trying all 26 possible Caesar cipher shifts:")
    print("-" * 50)
    
    # Try all possible shifts (0-25)
    for shift in range(26):
        decoded = caesar_decode(ciphertext, shift)
        print(f"Shift {shift}: {decoded}")
    
if __name__ == "__main__":
    main()
