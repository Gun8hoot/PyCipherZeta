import sys
from module.report import wreport
from module.color import cl
from Crypto.Hash import SHA3_256

method = "SHA3-256"

def init_sha256(string):
    h_str = SHA3_256.new()
    h_str.update(bytes(string, 'UTF-8'))
    hashed = h_str.hexdigest()
    print(f"{cl.fore_lavander}[!] The SHA3-256 hash for '{string}' is: {cl.back_green}{hashed}{cl.reset}")
    wreport(method, string, hashed, '')