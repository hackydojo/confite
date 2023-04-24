# ![](https://i.ibb.co/JKWYP5X/Group-1.png)
### Easly manage configurations with tiny library

This a a work in progress. We will be updating it soon with more information and documentation on how to use and extend **Confite**

## Installing confite

```bash
pip install confite
```

## Application Level AES Secret Encryption

### What is AES?

Advanced Encryption Standard (AES) very popular block cipher 
that is commonly used to encrypt electronic data. AES is very fast and secure. 
AES has three different block ciphers: `AES-128 (128 bit)`, `AES-192 (192 bit)` and
`AES-256 (256 bit)` - each cipher is named after the key length they use for 
encryption and decryption. Each of these ciphers encrypt and decrypt the data 
in 128-bit blocks, but they use different sizes of cryptographic keys.

### Why Confite uses GCM AES Mode?

GCM is a mode of AES that uses the CTR (counter) mode to encrypt data and uses Galois 
mode for authentication. Aside from the CTR mode which is used to encrypt the data, 
Galois mode authentication allows us to check at the end of decryption that the message 
has not been tampered with. GCM is well known for its speed and that it's a mode that 
it's patent-free.

### Password-based Encryption

AES requires an encryption key of 128, 192 or 256 bits in size (for AES-128, AWS-192 and 
AES-256 respectively). Confite currently only supports using key derivation in order to 
produce an encryption key of the appropriate size byte. `Crypto.Protocols.KDF.scrypt` is
used as the implementation of key derivation since it allows creating a key of any length 
in bytes using a password and a salt. 

Confite also uses scrypt instead of SHA family (ie. SHA-256 and SHA-512) because it also 
takes a salt and a work factor. Providing a salt that will mean that the same hash does 
not map to the same password every time, thus preventing rainbow table lookups. A work 
factor is also specified to make the transformation more computationally difficult which 
means the key is harder to brute force.



