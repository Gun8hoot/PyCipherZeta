from module.color import cl
from Crypto.Cipher import AES
from module.report import wreport
import string, random, base64
method = "AES"

character = string.ascii_letters+string.punctuation+string.digits
key = bytes(''.join(random.choice(character) for x in range(int(16))), 'UTF-8')


def encod_aes(string):
    
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(bytes(string, 'UTF-8'))
    encoded = ciphertext.hex()
    b64_key = base64.b64encode(key)
    decod_b64_keys = b64_key.decode('UTF-8')
    print(f"[!] The AES cipher for {cl.fore_orange}{string}{cl.reset} is: {cl.reset}{cl.fore_green}{encoded}{cl.reset} and you key is {cl.fore_yellow}{decod_b64_keys}{cl.reset}\n{cl.fore_red}[!] The key is encode to BASE64{cl.reset}")
    wreport(method, string, encoded, b64_key)

def decod_aes(string, key):
    decod_keys = base64.b64decode(key)
    print(decod_keys)
    nonce = cipher.nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    text = cipher.decrypt(string)

    try:
        cipher.verify(string)
        print(f"[!] The decoded string is {cl.fore_orange}{text}{cl.reset}")
    except ValueError:
        print(f"{cl.fore_red}[!] An error {cl.reset}")
