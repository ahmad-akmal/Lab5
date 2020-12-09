import socket

ServerSocket = socket.socket()
host = ''
port = 8888
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)

while True:
    Client, address = ServerSocket.accept()
    #Client.send(b'Welcome to server')
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    filename = input(str('Please enter the filename of the file : '))
    Client.send(str.encode(filename))
    file = open(filename, 'rb')
    file_data = file.read(1024)
    Client.send(file_data)
    print("Data has been transmitted successfully")
    break
ServerSocket.close()

