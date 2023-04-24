import os
import base64
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt


def main():
    salt = get_random_bytes(32)
    print(salt)

    b64encoded_salt = base64.b16encode(salt).decode('ascii')
    print(b64encoded_salt)

    b65bin_salt = b64encoded_salt.encode('ascii')
    print(b65bin_salt)

    bin_salt = base64.b64decode(b65bin_salt)
    print(bin_salt)

    str_salt = base64.b64decode(b64encoded_salt, )
    print(str_salt)

    key = scrypt('password123', b64encoded_salt, key_len=32, N=2 ** 17, r=8, p=1)  # Your key that you can encrypt with
    encoded_key = base64.b16encode(key).decode()
    print(encoded_key)


if __name__ == "__main__":
    main()
