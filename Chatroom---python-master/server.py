import socket
import threading
host=socket.gethostname()
port=12345
serv_add=(host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(serv_add)
s.listen()

clients=[]
nickNames=[]
def broadCast(message):
    for cli in clients:
        cli.send(message.encode('ascii'))
    return
def recive(cli):
    while True:
        try:
        #   print('waiting for msg from cl')
            msg=cli.recv(1024)
        #  print('server: msg recved from client',msg.decode('ascii'))
            broadCast(msg.decode('ascii'))
        except:
            print('recive error')
            indx=clients.index(cli)
            clients.remove(cli)
            nickName=nickNames[indx]
            broadCast( nickName+" Left chat room")
            nickNames.remove(nickName)
            break
def Handle():
    while True:
        cli,add=s.accept()
        #print("Connected with ",add)
        cli.send("NICK".encode('ascii'))
        nickName=cli.recv(1024).decode('ascii')
        clients.append(cli)
        nickNames.append(nickName)
        broadCast(nickName+' join the chat room')
        thread=threading.Thread(target=recive,args=(cli,))
        thread.start()

print("Serve is Listening ")
Handle()
