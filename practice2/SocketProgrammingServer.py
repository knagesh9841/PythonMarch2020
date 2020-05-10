import socket

ServerSocket = socket.socket()          # create Socket

print("Server Socket is created.")

ServerSocket.bind(('localhost', 9999))      # Bind the socket with IP Address and Port

ServerSocket.listen(3)                  # listen to How many Client

print("Waiting for Connection")

while True:
    ClientSocket, Address = ServerSocket.accept()       # When Client accept it and return ClientSocket and Address

    print("Connected with Address", Address)

    ClientSocket.send(bytes("Welcome to Python", 'utf-8'))      # Send data

    Msg = ClientSocket.recv(1024).decode()                      # receive data

    print("Connected with Client ", Msg)





