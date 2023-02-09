import socket

HOST = "0.0.0.0"
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr_port = s.accept()
        addr = addr_port[0]
        with conn:
            conn.send(bytes(f"Hello, {addr}!\n",  'utf-8'))
