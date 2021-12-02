from enum import Enum, auto
import hashlib
import sys

def usage():
    print("Usage : CheckSum.py [path] [algorithm] compare=[Hash to compare]\n \
            Or : CheckSum.py [path] [algorithm]", file=sys.stderr)

#Managed hash algorithm for this version
class Hash(Enum):
    SHA256 = auto()
    SHA1 = auto()
    MD5 = auto()


def getHash(file, algo):
    hash = None
    # Check if the wanted algo is managed
    for i in list(Hash): 
        if i.name == algo:
            hash = i
            break
    if not hash:
        print("Wrong hash algorithm", file=sys.stderr)
        usage()
    
    # Switch case the hash
    if hash.name == Hash.SHA256.name:
        return hashlib.sha256(file)
    elif hash.name == Hash.SHA1.name:
        return hashlib.sha1(file)
    elif hash.name == Hash.MD5.name:
        return hashlib.md5(file)
    
    
if __name__ == '__main__':
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        usage()
    path = ""
    algo = ""
    compare = None
    # Getting the arguments
    for i, arg in enumerate(sys.argv):
        if i == 1:
            path = arg
        elif i == 2:
            algo = arg
        elif i == 3:
            if "compare=" in arg:
                compare = arg.split("=")[1]
            else:
                print("Wrong third parameter (maybe forget the compare= ?)", file=sys.stderr)
                usage()
    
    # Do the algorithm and display the result
    try:
        with open(path, "rb") as File:
            bytesFile = File.read()
            fileHashed = getHash(bytesFile, algo)
            print("\nHash found:\n")
            print("-"*len(fileHashed.hexdigest()))
            print(fileHashed.hexdigest())
            print("-"*len(fileHashed.hexdigest()))
            if compare:
                print("\n<--> Checksum validated: "+ str(fileHashed.hexdigest()==compare.lower())+" <-->\n")
    except FileNotFoundError:
        print("\nPath not found", file=sys.stderr)
