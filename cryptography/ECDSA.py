# Elliptic Curve Digital Signature Algorithm

from ecdsa import SigningKey, SECP256k1

# We are using secp256k1 curve here

###
#  First let's generate some private key, which ecdsa library calls a signing key
#  and a corresponding public key which is called verifying key

sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key

# We are signing this message
signature = sk.sign(b"Not your keys, not your coins!")

print(signature)

assert vk.verify(signature, b"Not your keys, not your coins!")
