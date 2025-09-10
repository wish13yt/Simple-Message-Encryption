from cryptography.fernet import Fernet
import random
import string
import base64

print("so like this uses fernet and stuff and idk how secure that is so use something better for important stuff please")
length = 32
characters = string.ascii_uppercase + string.digits
pub = ''.join(random.choices(characters, k=length))
ferpub = pub.encode("ascii")
ferpub_bytes = base64.b64encode(ferpub)
ferpub_string = ferpub_bytes.decode("ascii")
print("ts is your public key share it with those you want to see the message " + ferpub_string)
f = Fernet(ferpub_string)
message = input("what message do you want to send? ")
message_bytes = message.encode("ascii")
token = f.encrypt(message_bytes)
strtoken = str(token)
print("this is your ENCRYPTED MESSAGE: " + strtoken[2:-1])
print("use the SME decrypter (Fernet) to decrypt!")