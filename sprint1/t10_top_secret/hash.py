import hashlib

def md5_hash(string):
    hash = hashlib.md5(string.encode())
    print(f'Original string: {string}\nmd5 hash generated is\n{hash.hexdigest()}')

def sha1_hash(string):
    hash = hashlib.sha1(string.encode())
    print(f'Original string: {string}\nsha1 hash generated is\n{hash.hexdigest()}')