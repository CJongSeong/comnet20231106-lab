import socket

HOST = input("server address : ")
PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
while 1:
    text = input('Write to Server : ').strip()
    print("Sending data :", text)
    s.sendall(text.encode('utf-8'))
    data = s.recv(1024)
    data = data.decode('utf-8')
    print("Data from server :", data)
