from module.report import wreport
from module.color import cl
from Crypto.Hash import SHA3_512
method = "SHA512"

def encod_sha512(string):
    h_obj = SHA3_512.new()
    h_obj.update(bytes(string, 'UTF-8'))
    hashed = h_obj.hexdigest()
    print(f"[!] The SHA3-512 hash for {cl.fore_orange}{string}{cl.reset} is: {cl.reset}{cl.fore_green}{hashed}{cl.reset}")
    wreport(method, string, hashed, '')
