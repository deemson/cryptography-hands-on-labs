from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def xor(first: bytes, second: bytes):
    return bytearray(x ^ y for x, y in zip(first, second))


key = b'0123456789abcdef0123456789abcdef'
iv = b'0123456789abcdef'
cipher = Cipher(algorithms.AES(key), modes.OFB(iv))
encryptor = cipher.encryptor()
p1 = b'known message'
c1 = encryptor.update(p1) + encryptor.finalize()
encryptor = cipher.encryptor()
c2 = encryptor.update(b'secret message') + encryptor.finalize()
p2 = xor(xor(p1, c1), c2)
print(str(p2, 'utf-8'))