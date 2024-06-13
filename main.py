# Import module
import argparse
from module.color import cl


# Arguments
parser = argparse.ArgumentParser(prog="\nUniversal Cypher/Hashing")
parser.add_argument('-m', '--method', help='Algorithm available: MD5, SHA3-256, AES, Blowfish', dest='method')
parser.add_argument('-s', '-str', '--string', help='Enter the string to hash/crypt', dest='string')
args = parser.parse_args()
m_m = args.method
s_s = args.string

# Init main
def __main__():
    if m_m == "AES" or m_m == "aes":
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.AES import init_aes
                init_aes(bytes(s_s, 'UTF-8'))
        except ValueError:
            pass

    elif m_m == "SHA256" or m_m == "sha256":
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.SHA256 import init_sha256
                init_sha256(s_s)
        except ValueError:
            pass

    elif m_m == "MD5" or m_m == 'md5':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.MD5 import init_md5
                init_md5(s_s)
        except ValueError:
            pass
    elif m_m == 'Blowfish' or m_m == 'BLOWFISH' or m_m == 'blowfish':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.Blowfish import init_blowfish
                init_blowfish(bytes(s_s, 'UTF-8'))
        except ValueError:
            pass

    elif m_m == 'blake2s' or m_m == 'BLAKE2s' or m_m == 'BLAKE2S' or m_m == 'blake2S':
        try:
            if s_s == None:
                print(cl.fore_red+"[!] You need to enter a string!"+cl.reset)
            elif len(s_s) > 1:
                from module.blake2s import init_blake2s
                init_blake2s(bytes(s_s, 'UTF-8'))
        except ValueError:
            pass
    
    else:
        print(cl.back_red+"[!] Do ' python3 ./main.py -h '"+cl.reset)

# Execute
if __name__ == '__main__':
    __main__()
