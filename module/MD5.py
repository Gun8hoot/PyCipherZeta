from module.color import cl
from module.report import wreport
from Crypto.Hash import MD5
method = "MD5"

def init_md5(string):
    h_str = MD5.new()
    h_str.update(bytes(string, 'UTF-8'))
    hashed = h_str.hexdigest()
    print(f"{cl.fore_lavander}[!] The SHA3-256 hash for '{string}' is: {cl.back_green}{hashed}{cl.reset}")
    wreport(method, string, hashed, '')