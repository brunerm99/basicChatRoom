#echoserver.py
import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 4949
print(host)
print(port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print 'Client sent:',  self.sock.recv(1024)
            self.sock.send('message recieved')

serversocket.listen(5)
print('server listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)

