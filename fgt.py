import re
import base64
from Crypto.Cipher import AES
#Created by Syed Asad Ali Zaidi 

def decrypt_password(encrypted_password):
    key = b'Mary had a littl'
    try:
        data = base64.b64decode(encrypted_password)
        iv = data[0:4] + b'\x00' * 12
        ct = data[4:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = cipher.decrypt(ct)
        return pt.decode(errors='ignore').rstrip('\x00')
    except Exception:
        return str(pt).rstrip('\x00').lstrip("b'").rstrip("'")

def clean_visible(s):
    # Keep: letters, numbers, punctuation, and symbols
    # Remove: control chars, zero-width, other invisible chars
    return re.sub(r'[^\x20-\x7E]', '', s)

x=input("Enter the Enc password:")
y=decrypt_password(x)
zz=clean_visible(y)
print(f"Enc is decrypted:{zz[:-1]}")

