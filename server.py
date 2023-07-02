import threading
import socket

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
nicknames =[]

def broadcast(message):
    for client in clients:
        client.send(message)
 

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]

            broadcast(f'{nickname} left the chat')
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f'connected with address: {str(address)}')

        client.send('Nick'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'nickname of the clien: {nickname}')
        broadcast(f'{nickname} joined'.encode('ascii'))

        client.send('connected to server'.encode('ascii'))

        # threading.Thread(target=handle,args=client)