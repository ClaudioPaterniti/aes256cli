import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

from aes256.api.utils import *

def encrypt(message: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(message) + encryptor.finalize()

    return cipher_text

def encrypt_file(input_path: str, key: str, output_path: str) -> None:
    with open(input_path, 'rb') as fp:
        message = fp.read()

    salt = os.urandom(LENGTH)
    iv = os.urandom(IV_LENGTH)

    padder = padding.PKCS7(BLOCK_SIZE).padder()
    clear_text = padder.update(message) + padder.finalize()

    derived_key = derive_key(key, salt)
    cipher_text = encrypt(clear_text, derived_key, iv)
    full_text = salt+iv+cipher_text

    with open(output_path, 'wb') as fp:
        fp.write(full_text)
