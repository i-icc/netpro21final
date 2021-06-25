import socket
import time
from game import Game 

def main():
    game = Game()
    req = {"field":game,"flag":"0","winner":"d"}

    print('start server')
    # create a socket object
    serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = "localhost"
    port = 9999
    # bind to the port
    serversocket.bind((host, port))

    # queue up to 10000 requests
    serversocket.listen(10)
    print('waiting connection...')

    clientsocket1, addr = serversocket.accept()
    print(addr)
    clientsocket1.send(f"{0}".encode('ascii'))

    clientsocket2, addr = serversocket.accept()
    print(addr)
    clientsocket2.send(f"{1}".encode('ascii'))
    time.sleep(1)
    clientsocket2.send(f"{req['field'].dump()}".encode('ascii'))
    clientsocket1.send(f"{req['field'].dump()}".encode('ascii'))

    n = 2
    for i in range(n):
        print(f"{i}ターン目")
        print(clientsocket1.recv(1024).decode('ascii'))
        clientsocket2.send(f"{req['field'].dump()}".encode('ascii'))
        print(clientsocket2.recv(1024).decode('ascii'))
        if i != n - 1:
            clientsocket1.send(f"{req['field'].dump()}".encode('ascii'))

    clientsocket2.send("flag".encode('ascii'))
    clientsocket1.send("flag".encode('ascii'))
    time.sleep(1)
    clientsocket2.send(f"{req['field'].dump()}".encode('ascii'))
    clientsocket1.send(f"{req['field'].dump()}".encode('ascii'))
    
    clientsocket2.close()
    clientsocket1.close()


if __name__ == "__main__":
    main()