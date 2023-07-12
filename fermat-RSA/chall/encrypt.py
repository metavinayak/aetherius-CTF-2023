# Imports, uses pycryptodome: pip install pycryptodome
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

# Setup
# p       = ***REDACTED***
# q       = ***REDACTED***
n       = p*q                 # Compute PUBLIC  value n from PRIVATE primes p and q
totient = (p-1)*(q-1)         # Compute PRIVATE totient function of n from PRIVATE primes p and q
e       = 65537               # Choose  PUBLIC  key e such that 1 < e < totient and gcd(e, totient) == 1, common value is 65537
d       = pow(e, -1, totient) # Compute PRIVATE key d as the inverse of e given the PRIVATE totient

# Prepare message
message = b"***REDACTED***"   # Message bytes to encrypt
message = bytes_to_long(message) # Transform bytes to a number (long) so that we can apply RSA

# Encryption
ciphertext = pow(message, e, n) # Encrypt message using PUBLIC values e and n

# Decryption
plaintext = pow(ciphertext, d, n)    # Decrypt ciphertext using PRIVATE key d
plaintext = long_to_bytes(plaintext) # Transform number back to bytes

with open('cipher.txt','w') as file:
    file.write('n= '+str(n)+'\n')
    file.write('ciphertext= '+str(ciphertext)+'\n')
    file.write('e= '+str(e)+'\n')
print('\n')
print(ciphertext,'\n')
print(plaintext)