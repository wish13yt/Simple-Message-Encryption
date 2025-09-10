import base64
print("welcome to simple message encryption decrypt tool!")
stuff = input("please enter the string you'd like to decrypt: ")
pub = input("please enter the public key of the message owner: ")
if pub[:6] == stuff[:6]:
    decrypted = stuff[6:]
    base64_bytes = decrypted.encode("ascii")
    decrypted_bytes = base64.b64decode(base64_bytes)
    decrypted_string = decrypted_bytes.decode("ascii")
    print(decrypted_string)