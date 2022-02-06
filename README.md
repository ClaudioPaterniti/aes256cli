## AES256 cli

This is a simple command line wrapper to _criptography_ (https://cryptography.io) to easily encrypt and decrypt small files with AES256.

### Example of use

Encrypt a file:  
``aes256 encrypt message.txt -o cipher_text.txt``

Decrypt:  
``aes256 decrypt cipher_text.txt -o message.txt``

### Encryption parameters and file format

The original message is encrypted with AES256/CBC/PKCS7:

- the message is padded with PKCS7 16 bit padding
- the encryption key is derived from the user key with HKDF with SHA256 hashing, and 32 bit random salt
- the message is encrypted with AES256 with CBC mode and a 16 bit random inizialization vector

The encrypted file has the following format:

- the random salt and the random CBC inizialization vector are saved as clear text in the first 32+16 bits
- the encrypted cipher text is saved from the 48th bit to the end of the file