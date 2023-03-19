import base58

mystring = b'hello world'
mybase58 = base58.b58encode(mystring)
print("Base58 String: ")
print(mybase58)

anotherBase58String = b'5QWTsqdM9CC9on'
res = base58.b58decode(anotherBase58String)
print("Another String decoded: ")
print(res)
