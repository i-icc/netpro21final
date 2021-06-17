import socket

def main():
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

    # queue up to 5 requests
    serversocket.listen(5)
    print('waiting connection...')

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()
        print("Got a connection from %s" % str(addr))
        msg = clientsocket.recv(1024)
        msg = f"{msg.decode('ascii').upper()}\n"
        clientsocket.send(msg.encode('UTF8'))
        clientsocket.close()

if __name__ == "__main__":
    main()