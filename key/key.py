import hashlib

username_trial = b"GOUGH"
hash_result = hashlib.sha256(username_trial).hexdigest()

dynamic_part = hash_result[4] + hash_result[5] + hash_result[3] + hash_result[6] + \
               hash_result[2] + hash_result[7] + hash_result[1] + hash_result[8]

key = "picoCTF{1n_7h3_|<3y_of_" + dynamic_part + "}"
print(key)