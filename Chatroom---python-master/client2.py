import socket
import threading
host=socket.gethostname()
port=12345
serv_add=(host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(serv_add)
nickName=input("Enter you nickname ")
def recive():
    while True:
        try:
            msg=s.recv(1024).decode('ascii')
            if msg=='NICK':
                s.sendall(nickName.encode('ascii'))
            else:
                print(msg)
        except:
            print('an error occure')
            s.close()
            break
def Write():
    while True:
        try:
            msg=nickName+': '+input()
            s.sendall(msg.encode('ascii'))
        except:
            print("Write error")

rec_Thread=threading.Thread(target=recive)
rec_Thread.start()
wr_Thread=threading.Thread(target=Write)
wr_Thread.start()
