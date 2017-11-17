#!/usr/bin/env python
#encoding: utf-8
from Crypto.Cipher import AES
from Crypto import Random

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:
    def __init__( self, key ):
        """
        Requires hex encoded param as a key
        """
        self.key = key.decode("hex")

    def encrypt( self, raw ):
        """
        Returns hex encoded encrypted value!
        """
        raw = pad(raw)
        iv = Random.new().read(AES.block_size);
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return ( iv + cipher.encrypt( raw ) ).encode("hex")

    def decrypt( self, enc ):
        """
        Requires hex encoded param to decrypt
        """
        enc = enc.decode("hex")
        iv = enc[:16]
        enc= enc[16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc))

if __name__== "__main__":
    key = "0A0C4652E008BE970CA84534C0E2D572"
    ciphertext = "3fc4c58fd310f8b8d254eb77ac0d7306146091e80010ae6d3b56bef6ddabf166";
    key=key[:32]
    encryptor = AESCipher(key=key)
    result = encryptor.encrypt("new daas")
    print result
    # decryptor = AESCipher(key)
    # plaintext = decryptor.decrypt(ciphertext)
    # print "%s" % plaintext