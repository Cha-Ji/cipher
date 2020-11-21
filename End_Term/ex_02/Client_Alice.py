# 서버에 정수를 전달한다.
# 사용자 인증이 가능하다.
# DES 암호화를 통해 사용자 정보를 전달한다.
from socket import *
from Crypto.Cipher import DES

# block size = 8
def pad(text):
    while len(text) % 8 != 0:
        text += ' '.encode()
    return text

# 암호화를 위한 des 키
key = 'qwerasdf'.encode()
des = DES.new(key, DES.MODE_ECB)

# TCP 연결
s = socket(AF_INET, SOCK_STREAM)
port_number, ip_address = 18000, '127.0.0.1'

if not s.connect((ip_address, port_number)):
    # 사용자 인증
    print("======================")
    user_id = input("아이디를 입력하세요 : ")
    padded_id = pad(user_id.encode())
    encrypted_id = des.encrypt(padded_id) 
    s.send(encrypted_id)

    user_pw = input("비밀번호를 입력하세요 : ")
    padded_pw = pad(user_pw.encode())
    encrypted_pw = des.encrypt(padded_pw) 
    s.send(encrypted_pw)
    print("======================")

    server_message = s.recv(1024)
    print(server_message.decode())

if server_message.decode() == '인증 실패!':
    exit()

#전달할 정수
message= input("제곱값이 궁금한 정수 : ")

# 서버에 정수 값을 전달
s.sendall(message.encode())
print(s.recv(1000).decode())
