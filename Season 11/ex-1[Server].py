import socket
import threading

HOST = socket.gethostname()
PORT = 150
clients = []

def handle_client(conn, addr):
    while True:
        try:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            print(f"Received message from {addr}: {data}")
            broadcast(data, conn)
        except:
            remove(conn)
            break

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
print(f"Chat server started at {HOST}:{PORT}")

while True:
    conn, addr = s.accept()
    print(f"Connection established with {addr}")
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()
