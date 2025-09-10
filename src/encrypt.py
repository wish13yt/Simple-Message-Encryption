import random
import string
import base64
print("now with 69 byte encryption")
print("so like this isnt really that secure so use something better for important stuff please")
length = 69
characters = string.ascii_uppercase + string.digits
priv = ''.join(random.choices(characters, k=length))
print("ts is your private key keep it safe youll need it " + priv)
length = 16
characters = string.ascii_uppercase + string.digits
pub = ''.join(random.choices(characters, k=length))
print("ts is your public key give it to trusted folks you want to read the message " + pub)
message = input("what message do you want to send? ")
sample_string_bytes = message.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
beginning = pub[:6]
print("this is your ENCRYPTED MESSAGE " + beginning + base64_string)
print("to decrypt use the SME Decrypter")