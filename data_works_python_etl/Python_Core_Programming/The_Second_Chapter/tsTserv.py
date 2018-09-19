from socket import *
from time import ctime

#初始化
HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

#创建套接字
socketS = socket(AF_INET,SOCK_STREAM)
socketS.bind(ADDR)
socketS.listen(5)
while True:
    print("Wait for conneting..")
    socketClient,caddr = socketS.accept()
    print("Connecting "+str(caddr))
    while True:
        #getInfo = socketS.recv(BUFSIZE)
        getInfo = socketClient.recv(BUFSIZE)
        if not getInfo:
            break
        socketClient.send(bytes('['+ctime()+' SocketInformation] :','utf-8')+getInfo)

    socketClient.close()
socketS.close()
