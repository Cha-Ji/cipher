from PIL import Image 
from Crypto.Cipher import AES 
from Crypto import Random

filename = "img.bmp" 
filename_out = "ebc_img" 
format = "BMP" 
key = Random.new().read(16)
 
def pad(data): 
    return data + b"\x00"*(16-len(data)%16)  
 
def convert_to_RGB(data): 
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data)) if i % 3 == d], [0, 1, 2])) 
    pixels = tuple(zip(r,g,b)) 
    return pixels 
     
def process_image(filename): 
    im = Image.open(filename) 
    data = im.convert("RGB").tobytes()  
 
    original = len(data)  
 
    new = convert_to_RGB(aes_ecb_encrypt(key, pad(data))[:original])  
     
    im2 = Image.new(im.mode, im.size) 
    im2.putdata(new) 
     
    im2.save(filename_out+"."+format, format) 
 
# CBC 
def aes_cbc_encrypt(key, data, mode=AES.MODE_CBC): 
    IV = "A"*16  
    aes = AES.new(key, mode, IV) 
    new_data = aes.encrypt(data) 
    return new_data 
# ECB 
def aes_ecb_encrypt(key, data, mode=AES.MODE_ECB): 
    aes = AES.new(key, mode) 
    new_data = aes.encrypt(data) 
    return new_data 
 
process_image(filename) 