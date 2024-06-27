import random
from module.color import cl
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from struct import pack
method = "BLOWFISH"

def encod_blowfish(string):
    key = get_random_bytes(random.randint(5, 56))
    bs = Blowfish.block_size
    cipher = Blowfish.new(key, Blowfish.MODE_EAX)
    plen = bs - len(string) % bs
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    encoded = cipher.iv + cipher.encrypt(string + padding)
    print(encoded)