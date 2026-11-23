import socket
import threading

PORT = 150
HOST = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

NICK = input("Welcome, Enter your name: ")

def receive_messages():
    while True:
        try:
            data = s.recv(1024).decode("utf-8")
            if not data:
                break
            print(data)
        except:
            print("An error occurred!")
            s.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    msg = input(f"{NICK} >> ")
    s.send(msg.encode("utf-8"))
    if msg.strip().lower() == "exit":
        break

s.close()
