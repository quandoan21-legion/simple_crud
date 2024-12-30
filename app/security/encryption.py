from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
import base64
from app import secret_key

def encrypt_password(password, key=None):
    if key is None:
        key = secret_key.encode('utf-8')
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_password = pad(password.encode('utf-8'), Blowfish.block_size)
    encrypted_password = cipher.encrypt(padded_password)
    return base64.b64encode(encrypted_password)
