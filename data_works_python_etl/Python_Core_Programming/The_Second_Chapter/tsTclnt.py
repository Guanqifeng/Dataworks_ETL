from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

socketClient = socket(AF_INET,SOCK_STREAM)
socketClientConnect = socketClient.connect(ADDR)

while True:
    data = input('>')
    #data.encode('utf-8')
    if not data:
        break
    socketClient.send(bytes(data,'utf-8'))
    data = socketClient.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
socketClient.close()
