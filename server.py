import socket
import threading

PORT=50000
HOST=socket.gethostbyname(socket.gethostname())

ADDRESS=(HOST,PORT)

FORMAT= "utf-8"

clients=[]
names=[]

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDRESS)

def startChat():
    print("Sever is working on "+ HOST)

    server.listen()

    while True:
        connection, addr = server.accept()
        connection.send("NAME".encode(FORMAT))

        name = connection.recv(1025).decode(FORMAT)

        names.append(name)

        clients.append(connection)

        print(f"Name is: {name}")

        broadcastMessage(f"{name} has joined the group".encode(FORMAT))

        connection.send("Connection successful".encode(FORMAT))

        thread = threading.Thread(target=receive, args=(connection,addr))

        thread.start()

        print(f"active connections {threading.active_count()-1}")


def receive(connection,addr):
    print(f"New Connection {addr}")

    connected = True

    while connected:
        message= connection.recv(1025)

        broadcastMesaage(message)

    connection.close()

def broadcastMessage(message):
    for client in clients:
        client.send(message)

startChat()


