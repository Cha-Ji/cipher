from socket import *
import TP_1_DES # a번에서 사용한 암호화
from Crypto.Cipher import DES

s = socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',18000))
s.listen(1)

while True:
    clientData,addr = s.accept()
    print('다음 클라이언트가 연결됩니다. ',addr)
    answer=0
    while True:
        data = clientData.recv(1024).decode()
        if not data:
            break
        
        key = 'qwerasdf'.encode()
        des = DES.new(key, DES.MODE_ECB)

        text_file = "text.txt"
        with open(text_file,"w") as f:
            f.write(data)

        encoded_text = TP_1_DES.encodeText(text_file)
        print("DES 암호화 :",encoded_text)

        decoded_text = TP_1_DES.decodeCrypto(text_file)
        print("복호 : ", decoded_text)

        clientData.sendall(decoded_text.encode())
