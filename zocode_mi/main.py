#!/usr/bin/env python
#encoding: utf-8
from zocode_mi.AESEncrypt import AESCipher

key = "0A0C4652E008BE970CA84534C0E2D572"
key = key[:32]
encryptor = AESCipher(key=key)
decryptor = AESCipher(key) #Use:decryptor.decrypt("encrypy text")

