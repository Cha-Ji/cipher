from socket import *
while True:
    message= input("input : ")
    for i in range(len(message)):
        s = socket(AF_INET,SOCK_STREAM)
        if not s.connect(('127.0.0.1',18000)):
            print('connected server!')
    if message == 'q':
        exit()
    s.sendall(message.encode())
    print(s.recv(1000).decode())
