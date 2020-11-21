from Crypto.Cipher import DES

# block size = 8
def pad(text):
    while len(text) % 8 != 0:
        text += ' '.encode()
    return text

# 파일의 text를 인코딩해서 저장한다.
def encodeText(text_name):
    with open(text_name, "r") as f:
        text = f.read()
        print("원본: ", text)

    # 8바이트 단위로 묶음
    padded_text = pad(text.encode())
    encrypted_text = des.encrypt(padded_text) 

    with open(text_name, "wb") as f:
        f.write(encrypted_text)
    return encrypted_text

# 파일을 복호화해서 다시 저장한다.
def decodeCrypto(text_name):
    with open(text_name, "rb") as f:
        decrypted_text = des.decrypt(f.read())
    with open(text_name, "wb") as f:
        f.write(decrypted_text)
    return decrypted_text.decode()

key = 'qwerasdf'.encode()
des = DES.new(key, DES.MODE_ECB)

text_file = "text2.txt"
encoded_text = encodeText(text_file)
print("DES 암호화 :",encoded_text)

decoded_text = decodeCrypto(text_file)
print("복호 : ", decoded_text)




