import socket

def main():
    print('start client')
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    # host = socket.gethostname()
    host = "localhost"
    port = 9999
    # connection to hostname on the port.
    s.connect((host, port))
    msg = input("Please enter your message.: ")
    s.send(msg.encode('ascii'))
    print(f"send a message: {msg}")
    # Receive no more than 1024 bytes
    msg = s.recv(1024)
    s.close()
    print(f"receive a message: {msg.decode('ascii')}")

if __name__ == "__main__":
    main()