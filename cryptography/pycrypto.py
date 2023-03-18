from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify

message = b'I love cryptography!'  # We will be ENCRYPTING this message using keys

# Generating private key first
privateKey = RSA.generate(1024)  # key length is 1024

# Generating public key from private key
publicKey = privateKey.public_key()
print(type(privateKey))  # <class 'Crypto.PublicKey.RSA.RsaKey'>
print(type(publicKey))  # <class 'Crypto.PublicKey.RSA.RsaKey'>

# Converting our keys to strings, and saving them in .pem files
privatePem = privateKey.export_key().decode()
publicPem = publicKey.export_key().decode()

with open('private.pem', 'w') as pr:
    pr.write(privatePem)

with open('public.pem', 'w') as pu:
    pu.write(publicPem)

print('private.pm:')
with open('private.pem', 'r') as f:
    print(f.read())

print('public.pem:')
with open('public.pem', 'r') as f:
    print(f.read())

# Converting the keys back to RSA key objects, and do encrypting
prKey = RSA.import_key(open('private.pem', 'r').read())
puKey = RSA.import_key(open('public.pem', 'r').read())

# ENCRYPTION!!
# Data is encrypted with public key, and decrypted with corresponding private key
cipher = PKCS1_OAEP.new(key=puKey)
cipherText = cipher.encrypt(message)

print(cipherText)

decrypt = PKCS1_OAEP.new(key=prKey)
decryptedMessage = decrypt.decrypt(cipherText)

print(decryptedMessage)
