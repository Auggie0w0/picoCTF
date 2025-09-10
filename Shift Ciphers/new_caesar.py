import string

ALPHABET = string.ascii_lowercase[:16]  # 'abcdefghijklmnop'
A2I = {c:i for i,c in enumerate(ALPHABET)}

def unshift(c, k):
    return ALPHABET[(A2I[c] - A2I[k]) % 16]

def b16_decode(s):
    assert len(s) % 2 == 0
    out = bytearray()
    for i in range(0, len(s), 2):
        hi = A2I[s[i]]
        lo = A2I[s[i+1]]
        out.append((hi << 4) | lo)
    return out.decode(errors="replace")

def decrypt(enc, key):
    # inverse of shift()
    un = ''.join(unshift(c, key) for c in enc)
    return b16_decode(un)

# ---- usage ----
enc = "PUT_CIPHERTEXT_HERE"  # the printed 'enc' from the script

# Try all 16 possible one-letter keys
cands = [(k, decrypt(enc, k)) for k in ALPHABET]

# If you expect a picoCTF flag, filter:
for k, pt in cands:
    if pt.startswith("picoCTF{"):
        print(f"[key={k}] {pt}")

# Otherwise, just inspect all:
# for k, pt in cands: print(f"[key={k}] {pt}")
