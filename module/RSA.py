from Crypto.PublicKey import RSA
import os, sys, threading, math
from Crypto import Cipher

def encod_rsa():
    mykey = RSA.generate(3072)
    print(mykey)

def decod_rsa(s_s, k_k):
    try:
        f = open(k_k, 'r')
        read_f = f.read()
        print(read_f)
    except FileNotFoundError:
        print('[!] The key path you have enter is not valid')
    
    pass