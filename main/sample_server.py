import socket

def main():
    field = [[0,1,0],[0,0,1]]
    req = {"field":field}

    print('start server')
    # create a socket object
    serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    #host = socket.gethostname()
    host = "localhost"
    port = 9999
    # bind to the port
    serversocket.bind((host, port))

    # queue up to 10000 requests
    serversocket.listen(10)
    print('waiting connection...')

    # 待機中
    for i in range(2):
        # establish a connection
        clientsocket, addr = serversocket.accept()
        print(addr)
        clientsocket.send(f"{i}".encode('ascii'))
        clientsocket.send(f"{req}".encode('ascii'))
        clientsocket.close()
    
    for _ in range(4):
        clientsocket1, addr1 = serversocket.accept()
        print(addr1)
        

        clientsocket2, addr2 = serversocket.accept()
        print(addr2)
        msg = clientsocket2.recv(1024)
        print(msg.decode('ascii'))
        clientsocket2.close()

        clientsocket1.send(f"{req}".encode('ascii'))
        clientsocket1.close()


if __name__ == "__main__":
    main()