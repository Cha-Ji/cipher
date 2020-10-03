from Crypto.Cipher import AES
from PIL import Image
import base64
import os
import sys
from Crypto import Random

BLOCK_LEN = 16

def encrypt(key, imagefile):
    if len(key) % 16 != 0:
        sys.exit(1)

    with open(imagefile, 'rb') as image_file:
        img_read = image_file.read()
        image_str = base64.b16encode(img_read)

    padding = BLOCK_LEN - len(image_str) % BLOCK_LEN
    image_str += bytes([padding]) * padding
    aes = AES.new(key, AES.MODE_ECB)
    enc = aes.encrypt(image_str)
    
    with open('enc_'+imagefile, 'wb') as image_file:
        image_file.write(enc)

    size = (len(enc)/3) ** (1. / 2)
    encrypted_img = Image.frombytes("RGB", (int(size), int(size)), enc, "raw","RGB",0,1)
    encrypted_img.save('RGB.bmp', 'bmp')
 
def decrypt(key, imagefile):
    if len(key) % 16 != 0:
        sys.exit(1)
    
    with open(imagefile, 'rb') as image_file:
        enc_str = image_file.read()

    aes = AES.new(key,AES.MODE_ECB)
    data = aes.decrypt(enc_str)
    data = data[:-data[-1]]
    
    with open('dec_'+imagefile[4:], 'wb') as image_file:
        image_file.write(base64.b16decode(data))
key = Random.new().read(16)

encrypt(key, 'img.bmp')
decrypt(key, 'enc_img.bmp')