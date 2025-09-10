from cryptography.fernet import Fernet
import random
import string
import base64

print("so like this uses fernet and stuff and idk how secure that is so use something better for important stuff please")
ferpub_string = input("whats your public key? ")
f = Fernet(ferpub_string)
message = input("what message do you want to send? ")
message_bytes = message.encode("ascii")
token = f.encrypt(message_bytes)
strtoken = str(token)
print("this is your ENCRYPTED MESSAGE: " + strtoken[2:-1])
print("use the SME decrypter (Fernet) to decrypt!")