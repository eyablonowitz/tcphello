import socket


def hello_server(host="0.0.0.0", port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr_port = s.accept()
            addr = addr_port[0]
            with conn:
                conn.send(bytes(f"Hello, {addr}!\n",  'utf-8'))


if __name__ == "__main__":
    hello_server()
