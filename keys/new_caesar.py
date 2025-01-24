import string

LOWERCASE_OFFSET = ord("a")
# this determins the alphabet's ending (in this case p = :16)
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def b16_decode(enc):
    dec = ""
    for i in range(0, len(enc), 2):
        binary = "{0:04b}".format(ALPHABET.index(enc[i])) + "{0:04b}".format(ALPHABET.index(enc[i+1]))
        dec += chr(int(binary, 2))
    return dec

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def decode_all(encoded_text):
    print("Attempting all possible keys...")
    print("-" * 50)
    
    for possible_key in ALPHABET:
        # First unshift
        unshifted = ""
        for i, c in enumerate(encoded_text):
            unshifted += unshift(c, possible_key)
        
        # Then try to decode base16
        try:
            decoded = b16_decode(unshifted)
            if all(32 <= ord(c) <= 126 for c in decoded):  # Check if printable ASCII
                print(f"Key '{possible_key}': picoCTF{{{decoded}}}")
        except:
            continue

# Your encoded text
encoded_flag = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"
decode_all(encoded_flag)
