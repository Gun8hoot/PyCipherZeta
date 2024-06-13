from module.report import wreport
from module.color import cl
from Crypto.Hash import SHA3_512
method = "SHA512"

def init_sha512(string):
    h_obj = SHA3_512.new()
    h_obj.update(bytes(string, 'UTF-8'))
    hashed = h_obj.hexdigest()
    print(f"{cl.fore_lavander}[!] The SHA3-512 hash for '{string}' is: {cl.reset}{cl.back_green+cl.fore_black}{hashed}{cl.reset}")
    wreport(method, string, hashed, '')
