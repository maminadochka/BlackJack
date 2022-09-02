import socket
import struct

ClientSocket = socket.socket()
host = '127.0.0.1'


ClientSocketSocket = socket.socket()


def play():
    response = ClientSocket.recv(1024)
    answer = response.decode('utf-8')
    br = False
    while answer != "exit":
        while answer != "y/n":
            print(answer)
            response = ClientSocket.recv(1024)
            answer = response.decode('utf-8')
            if answer == "exit":
                br = True
                break
        if br:
            break
        response = ClientSocket.recv(1024)
        input_answer = input(response.decode('utf-8'))
        ClientSocket.send(str.encode(input_answer))
        response = ClientSocket.recv(1024)
        answer = response.decode('utf-8')

