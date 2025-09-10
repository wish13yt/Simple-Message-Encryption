import base64
print("now with 69 byte encryption")
print("so like this isnt really that secure so use something better for important stuff please")
print("also this is just for people who already have a private/public key and want to use it")
priv = input("enter your private key: ")
pub = input("enter your public key: ")
message = input("what message do you want to send? ")
sample_string_bytes = message.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
beginning = pub[:6]
print("this is your ENCRYPTED MESSAGE " + beginning + base64_string)
print("to decrypt use the SME Decrypter")