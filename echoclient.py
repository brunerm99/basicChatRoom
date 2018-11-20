#echoclient.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 4949
print(host)
print(port)

s.connect((host, port))
def send(msg):
    s.send(msg)
    data = ''
    data = s.recv(1024)
    print(data)

while 1:
    r = raw_input('enter')
    send(r)

s.close()
