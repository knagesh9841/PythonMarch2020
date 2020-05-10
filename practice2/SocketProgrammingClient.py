import socket

ClientSocket = socket.socket()

ClientSocket.connect(('localhost', 9999))       # Connect to Server

Msg = ClientSocket.recv(1024).decode()

print("Connected to Server ", Msg)

ClientSocket.send(bytes("Xpanxion", 'utf-8'))



