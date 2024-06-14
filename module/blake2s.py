from Crypto.Hash import BLAKE2s
from module.color import cl
from module.report import wreport
import random
method = "BLAKE2S"

def encod_blake2s(string):
    h_obj = BLAKE2s.new(digest_bits=256)
    h_obj.update(bytes(string, 'UTF-8'))
    hashed = h_obj.hexdigest()
    print(f"[!] The BLAKE2S chain for {cl.fore_orange}{string}{cl.reset} is: {cl.reset}{cl.fore_green}{hashed}{cl.reset}")
    wreport(method, string, hashed, '')