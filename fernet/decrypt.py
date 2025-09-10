from cryptography.fernet import Fernet

token = input("whats the message you wanna decrypt? ")
pub = input("whats the public key of the message? ")
f = Fernet(pub)
# decrypting the ciphertext
d = f.decrypt(token)

# display the plaintext and the decode() method 
# converts it from byte to string
print(d.decode())