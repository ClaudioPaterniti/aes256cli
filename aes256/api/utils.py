from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

LENGTH = 32
IV_LENGTH = 16
BLOCK_SIZE = 128

def derive_key(key: str, salt: bytes) -> bytes:
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        info= None,
        backend= None
    )
    key_bytes = bytes(key, 'utf-8')
    return hkdf.derive(key_bytes)