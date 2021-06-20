import socket
import time

def main():
    field = [[0,1,0],[0,0,1]]
    req = {"field":field}

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
    clientsocket2.send(f"{req}".encode('ascii'))
    clientsocket1.send(f"{req}".encode('ascii'))

    for i in range(5):
        print(f"{i}ターン目")
        print(clientsocket1.recv(1024).decode('ascii'))
        clientsocket2.send(f"{req}".encode('ascii'))
        print(clientsocket2.recv(1024).decode('ascii'))
        clientsocket1.send(f"{req}".encode('ascii'))
    
    clientsocket2.close()
    clientsocket1.close()


if __name__ == "__main__":
    main()