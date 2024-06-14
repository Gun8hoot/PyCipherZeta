import sys
from module.report import wreport
from module.color import cl
from Crypto.Hash import SHA3_256

method = "SHA3-256"

def encod_sha256(string):
    h_str = SHA3_256.new()
    h_str.update(bytes(string, 'UTF-8'))
    hashed = h_str.hexdigest()
    print(f"[!] The SHA3-256 hash for {cl.fore_orange}{string}{cl.reset} is: {cl.reset}{cl.fore_green}{hashed}{cl.reset}")
    wreport(method, string, hashed, '')

