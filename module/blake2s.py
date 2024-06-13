from Crypto.Hash import BLAKE2s
from module.color import cl
from module.report import wreport
import random
method = "BLAKE2S"

def init_blake2s(string):
    h_obj = BLAKE2s.new(digest_bits=256)
    h_obj.update(bytes(string, 'UTF-8'))
    hashed = h_obj.hexdigest()
    print(f"{cl.fore_lavander}[!] The SHA3-256 hash for '{string}' is: {cl.reset}{cl.back_green+cl.fore_black}{hashed}{cl.reset}")
    wreport(method, string, hashed, '')