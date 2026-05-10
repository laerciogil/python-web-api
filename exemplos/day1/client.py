import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))

# request
cmd = "GET / HTTP/1.0\r\nHost: localhost\r\n\r\n".encode()
client.send(cmd)

while True:
    data = client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

client.close()