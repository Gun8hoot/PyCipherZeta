from module.color import cl
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
method = "AES"

def init_aes(string):
    h = get_random_bytes(256)
    print(h)
    print(f"\n{string}")