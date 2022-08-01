import Crypto.Cipher.AES
import base64


class Cipher_AES:
  
  # Padding calculation for 16 bit block size.
  pad_pkcs5 = lambda x, y: x + (y - len(x) % y) * chr(y - len(x) % y).encode("utf-8")
  unpad_pkcs5 = lambda x: x[:-ord(x[-1])]
  
  # initialization of key and initial vector.
  def __init__(self, key="w9z$C&E)H@McQfTjWnZr4u7x!A%D*G-J", iv=""):
    self.__key = key
    self.__iv = iv
    # print(self.__iv)

  # Fix style for AES-256 i.e CBC(Cryptography and Computer Security)
  def Cipher_MODE_CBC(self):
    self.__x = Crypto.Cipher.AES.new(self.__key.encode("utf-8"), Crypto.Cipher.AES.MODE_CBC, self.__iv.encode("utf-8"))
    
  # Encrypt the provided text with the help of padding.
  def encrypt(self, text, cipher_method, pad_method="", code_method=""):
    if cipher_method.upper() == "MODE_CBC":
      self.Cipher_MODE_CBC()
    cipher_text = b"".join([self.__x.encrypt(i) for i in self.text_verify(text.encode("utf-8"), pad_method)])
    # print(cipher_text)
    # print("Cipher text: ",type(cipher_text))
    if code_method.lower() == "base64":
      return base64.encodebytes(cipher_text).decode("utf-8").rstrip()
    else:
      return cipher_text.decode("utf-8").rstrip()
 
  # Decrypt the provided text with the help of padding.
  def decrypt(self,cipher_text, cipher_method, pad_method="", code_method=""):
    if cipher_method.upper() == "MODE_CBC":
      self.Cipher_MODE_CBC()
    if code_method.lower() == "base64":
      cipher_text = base64.decodebytes(cipher_text.encode("utf-8"))
    else:
          cipher_text = cipher_text.encode("utf-8")
    return self.unpad_method(self.__x.decrypt(cipher_text).decode("utf-8"), pad_method)


  def text_verify(self, text, method):
    while len(text) > len(self.__key):
      # print(len(text), len(self.__key))
      text_slice = text[:len(self.__key)]
      text = text[len(self.__key):]
      yield text_slice
    else:
      if len(text) == len(self.__key):
        yield text
      else:
        yield self.pad_method(text, method)
        
  def pad_method(self, text, method):
    if method == "":
      return Cipher_AES.pad_default(text, 16)
    elif method == "PKCS5Padding":
        return Cipher_AES.pad_pkcs5(text, 16)
    else:
      return Cipher_AES.pad_user_defined(text, 16, method)
  
  def unpad_method(self, text, method):
    if method == "":
      return Cipher_AES.unpad_default(text)
    elif method == "PKCS5Padding":
      return Cipher_AES.unpad_pkcs5(text)
    else:
      return Cipher_AES.unpad_user_defined(text, method)
    
# Static key
key = "w9z$C&E)H@McQfTjWnZr4u7x!A%D*G-J"
# Static Initialvector
iv = "fedcba9876543210"

# file containing json
f = open('777.json')
text = f.read()
f.close()

# Mode/Style
cipher_method = "MODE_CBC"
# Padding i.e. PKCS5
pad_method = "PKCS5Padding"
# Length 64 bit
code_method = "base64"
# Encryption
cipher_text = Cipher_AES(key, iv).encrypt(text, cipher_method, pad_method, code_method)
cipher_text = cipher_text.replace('\n','')
# Cipher created after encryption
print('['+cipher_text+']')
# Decryption
text = Cipher_AES(key, iv).decrypt(cipher_text, cipher_method, pad_method, code_method)
# Cipher created after decryption
print(text)