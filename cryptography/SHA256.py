import hashlib
message = 'Python is fun!'

hashValue = hashlib.sha256(message.encode())
print("SHA256 hash is: ", hashValue.hexdigest())
# 64, no matter what is the message length
print("Length of SHA256 hash is: ", len(hashValue.hexdigest()))
