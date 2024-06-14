import base64
from module.color import cl
from module.report import wreport
method = "BASE64"

def encod_base64(string):
    b64_enc = base64.b64encode(bytes(string, 'UTF-8'))
    encoded = b64_enc.decode('UTF-8')
    print(f"[!] The BASE64 encoded string for {cl.fore_orange}{string}{cl.reset} is: {cl.reset}{cl.fore_green}{encoded}{cl.reset}")
    wreport(method,string,encoded,'')


def decod_base64(string):
    b64_dec = base64.b64decode(bytes(string, 'UTF-8'))
    decoded = b64_dec.decode('UTF-8')
    print(f"[!] The BASE64 decoded string for {cl.fore_orange}{string}{cl.reset} is: {cl.reset}{cl.fore_green}{decoded}{cl.reset}")
    wreport(method,string,decoded,'')
