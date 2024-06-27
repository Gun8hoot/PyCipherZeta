# Import module
import argparse
from module.color import cl

# Arguments
parser = argparse.ArgumentParser(prog="\n\nPyCipherZeta")
parser.add_argument('-m', '-M', '--method', help='Algorithm available: MD5, SHA3-256, SHA3-512, BASE64, AES, Blowfish, BLAKE2S, RSA', dest='method')
parser.add_argument('-s', '-S', '-str', '--string', dest='string')
parser.add_argument('-e', '-E', '--encode', dest='encode', action='store_true')
parser.add_argument('-d', '-D', '--decode', dest='decode', action='store_true')
parser.add_argument('-k', '-K', '--key', dest='keys', required=False)
parser.add_argument('-o', '-O', '--output', dest='output', required=False)
args = parser.parse_args()
# -------
m_m = args.method
s_s = args.string
e_e = args.encode
d_d = args.decode
k_k = args.keys
o_o = args.output


# Functions
def __main__():
    try:
        if e_e == True:
            __encrypt__()
        elif d_d == True:
            __decrypt__()
        else:
            print(cl.back_red+"[!] A problem has occurred during program execution, try to do 'python3 ./main.py -h'"+cl.reset)
    except ValueError:
        print(cl.back_red+"[!] A problem has occurred during program execution, try to do 'python3 ./main.py -h'"+cl.reset)
# -------


def __encrypt__():
    if m_m == "AES" or m_m == "aes":
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.AES import encod_aes
                encod_aes(s_s)
        except ValueError:
            pass

    elif m_m == "SHA256" or m_m == "sha256":
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.SHA256 import encod_sha256
                encod_sha256(s_s)
        except ValueError:
            pass

    elif m_m == "MD5" or m_m == 'md5':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.MD5 import encod_md5
                encod_md5(s_s)
        except ValueError:
            pass
    elif m_m == 'Blowfish' or m_m == 'BLOWFISH' or m_m == 'blowfish':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.BLOWFISH import encod_blowfish
                encod_blowfish(s_s)
        except ValueError:
            pass

    elif m_m == 'blake2s' or m_m == 'BLAKE2s' or m_m == 'BLAKE2S' or m_m == 'blake2S':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.BLAKE2S import encod_blake2s
                encod_blake2s(s_s)
        except ValueError:
            pass

    elif m_m == 'sha512' or m_m == 'SHA512' or m_m == 'Sha512':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.SHA512 import encod_sha512
                encod_sha512(s_s)
        except ValueError:
            pass
    
    elif m_m == 'base64' or m_m == 'BASE64' or m_m == 'Base64':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.BASE64 import encod_base64
                encod_base64(s_s)
        except ValueError:
            pass

    elif m_m == 'RSA' or m_m == 'rsa' or m_m == 'Rsa':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.RSA import encod_rsa
                encod_rsa(s_s)
        except ValueError:
            pass


    pass


def __decrypt__():
    if m_m == 'base64' or m_m == 'BASE64' or m_m == 'Base64':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.BASE64 import decod_base64
                decod_base64(s_s)
        except ValueError:
            pass
    
    elif m_m == "AES" or m_m == "aes":
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                if k_k == None:
                    print(cl.fore_red+"[!] You need to specify the encoded key"+cl.reset)
                elif len(k_k) > 1:
                    from module.AES import decod_aes
                    decod_aes(s_s, k_k)
        except ValueError:
            pass

    elif m_m == 'RSA' or m_m == 'rsa' or m_m == 'Rsa':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                if k_k == None:
                    print(cl.fore_red+"[!] You need to specify the public key file"+cl.reset)
                elif len(k_k) > 1:
                    from module.RSA import decod_rsa
                    decod_rsa(s_s, k_k)
        except ValueError:
            pass

    pass



# Execution
if __name__ == '__main__':
    __main__()