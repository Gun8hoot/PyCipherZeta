from module.color import cl
from module.report import wreport
from Crypto.Hash import MD5
method = "MD5"

def encod_md5(string):
    h_str = MD5.new()
    h_str.update(bytes(string, 'UTF-8'))
    hashed = h_str.hexdigest()
    print(f"[!] The MD5 hash for {cl.fore_orange}{string}{cl.reset} is:\n {cl.reset}{cl.fore_green}{hashed}{cl.reset}")
    wreport(method, string, hashed, '')