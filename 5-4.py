import socket
import time
ServerSocket = socket.socket()
host = ''
port = 8888

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(2)


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    filename = Client.recv(1024)

    if not filename:
       time.sleep(1)
       break

    file = open(filename,'wb')
    file_data = Client.recv(1024)
    file.write(file_data)
    file.close()
    print("File has been received successfully")
ServerSocket.close()
