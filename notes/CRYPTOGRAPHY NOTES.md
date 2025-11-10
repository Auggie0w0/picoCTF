# CRYPTOGRAPHY NOTES

## ￼￼RSA
https://hereket.com/posts/rsa-algorithm/
![](https://hereket.com/posts/rsa-algorithm/rsa-formula.png)
| **Name** | **Role**                                                                                                                      |
| -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| e        | public key (n,e)                                                                                                              |
| n        | a key which is the result of p*q                                                                                              |
| d        | priccate key (n,d); stands for the decryption exponents is also known as the modular multiplicative inverse of **e **mod Φ(n) |
| C        | Encryption: C is the cipher text and e and n are parts of public key                                                          |
| M        | Decription: M is the message and d and n are parts of private key                                                             |

### Without private key 
1. N needs to be factored into p, q
		a) factors smaller numbers one by one (using code)
		b)  _[Pollard's rho algorithm](_https://www.geeksforgeeks.org/dsa/pollards-rho-algorithm-prime-factorization/_) - for larger numbers_
		c) _[Fermat's factorization](_https://www.geeksforgeeks.org/dsa/fermats-factorization-method/_) - for close to perfect squres_

2. Euler’s Totient Function φ(N)
		a) it represents the number between 1 and N

3. Calculate the Private Key d
		a) mod_inverse() function
		b) extended_gcd() function

4. Decrypt the Ciphertext
		a) **plaintext = ciphertextᵈ mod N**

