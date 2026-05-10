import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9000))
server.listen()

try:
    while True:
        client, address = server.accept()
        data = client.recv(4096).decode()
        print(f"Recebido: {data}")

        # Response
        client.sendall(
            b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Hello World</h1></body></html>"
        )
        client.shutdown(socket.SHUT_WR)
except Exception as e:
    print(f"Erro: {e}")
finally:
    print("Servidor encerrado")
    client.close()
    server.close()