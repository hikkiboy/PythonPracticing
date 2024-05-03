import socket

lista_portas = [80,123,124,124,125,5,754,765,8769,976,86,87]


for porta in lista_portas:

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('bancocn.com', porta))
    client.send(b"oi mundo")
    resposta = client.recv(1024)
    print(resposta.decode())
