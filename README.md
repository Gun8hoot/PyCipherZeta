# PyCipherZeta
# FREE PALESTINE 🇵🇸
- With this project, you can encode a string to ```MD5, SHA3-256, SHA3-512, BASE64, AES, Blowfish, BLAKE2S```
- ⚠️ This program is not currently compatible with Windows, I will develop the Windows version later. ⚠️

## Install
### Linux
- Clone the project repository: 
```sh
git clone https://github.com/Gun8hoot/PyCipherZeta.git
```
- Go to the project folder:
```sh
cd ./PyCipherZeta
```
- I highly recommend creating a virtual python environment (venv) before installing the requirements.txt:
```sh
python3 -m venv .venv && source ./.venv/bin/activate
```
- Install necessary modules:
```sh
pip install -r ./requirements.txt
```
- Execute the program with: 
```sh
python3 ./main.py -e/-d -m (ALGORITHM) -s (STRING)
```

### Arguments
| Arguments                   |                    Description                             |
| :---                        |    :----:                                                  |
| -s , -S , -str , --string   | Specify the string to encode/decode                        |
| -m , -M , --method          | Choose the wanted algorithm                                |
| -k , -k , --key             | You need this arguments if decode a symmetric or asymmetric cipher        |
| -o , -O , --output          | You need this arguments if you want encode a string        |
| -e , -E , --encode          | You need this arguments if you want encode a string        |
| -d , -D , --decode          | You need this arguments if you want decode a string        |

## Example
**Input:**
```sh
python3 ./main.py -m SHA512 -m HelloWorld
```
**Output:**
```sh
[!] The SHA3-512 hash for HelloWorld is: 60846a2369ad408101216c7f952be7019559acfa146e6b5c51d0a18424a620a22e937e5650ed332cbdb9ebe21f03f86207078958e0ef7b60bb285851cf9f9a32 
```    

###
> ***Project write in:***       
> [![S/O skillicons for the py & md icon](https://skillicons.dev/icons?i=python,markdown&theme=dark)](https://skillcons.dev/)