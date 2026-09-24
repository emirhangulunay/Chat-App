from threading import Thread
from socket import AF_INET, socket, SOCK_STREAM

# def client_communication(client):



def wait_for_connection(SERVER):
    run = True
    while run:
        client, addr = SERVER.accept()
        Thread(target= client_communication, args=(client,)).start()

HOST = ''
PORT = 5500
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target= wait_for_connection, (SERVER))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()