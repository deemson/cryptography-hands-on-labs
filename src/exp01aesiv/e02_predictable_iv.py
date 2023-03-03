from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def xor(first: bytes, second: bytes):
    return bytearray(x ^ y for x, y in zip(first, second))


message = b'message1message2'
key = b'0123456789abcdef0123456789abcdef'
iv1 = b'0123456789abcdef'
iv2 = b'fedcba9876543210'
cipher1 = Cipher(algorithms.AES(key), modes.CBC(iv1))
encryptor1 = cipher1.encryptor()
p1 = message
c1 = encryptor1.update(p1) + encryptor1.finalize()
print('c1: ', c1.hex())
cipher2 = Cipher(algorithms.AES(key), modes.CBC(iv2))
encryptor2 = cipher2.encryptor()
p2 = xor(xor(message, iv2), iv1)
c2 = encryptor2.update(p2) + encryptor2.finalize()
print('c2: ', c2.hex())
