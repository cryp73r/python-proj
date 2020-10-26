import sys
import zipfile


if (len(sys.argv) == 1) or (len(sys.argv) == 2):
    print("Usage : python3 zipfile.py <wordlist> <zipfile>")
if len(sys.argv) == 3:
    file = sys.argv[1]
    zf = zipfile.ZipFile(sys.argv[2])
    f = open(file)
    for words in f.readlines():
        pwd = words.strip()
        try:
            zf.extractall(pwd = str.encode(pwd))
            print("[+] Password found: {} Success".format(pwd))
            break

        except:
            continue
        else:print("[-] Not Found use more dense wordlist")
