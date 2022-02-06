
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

from aes256.api.utils import *

def decrypt(cipher_text: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    message = decryptor.update(cipher_text) + decryptor.finalize()
    return message

def decrypt_file(input_path: str, key: str, output_path: str) -> None:
    with open(input_path, 'rb') as fp:
        full_text = fp.read()

    salt = full_text[:LENGTH]
    iv = full_text[LENGTH:LENGTH+IV_LENGTH]
    cipher_text = full_text[LENGTH+IV_LENGTH:]

    derived_key = derive_key(key, salt)
    clear_text = decrypt(cipher_text, derived_key, iv)

    unpadder = padding.PKCS7(BLOCK_SIZE).unpadder()
    message = unpadder.update(clear_text) + unpadder.finalize()

    with open(output_path, 'wb') as fp:
        fp.write(message)
