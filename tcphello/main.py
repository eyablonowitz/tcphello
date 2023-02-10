import logging
import socket


def hello_server(addr="", port=12345):
    logging.basicConfig(level=logging.INFO)
    if socket.has_dualstack_ipv6():
        s = socket.create_server((addr, port), family=socket.AF_INET6, dualstack_ipv6=True, reuse_port=True)
    else:
        s = socket.create_server((addr, port), reuse_port=True)
    logging.info(f"Listening on port {port}")
    while True:
        conn, addr_port = s.accept()
        addr = addr_port[0]
        hello_message = f"Hello, {addr}!\n"
        logging.info(hello_message)
        with conn:
            conn.send(bytes(hello_message,  'utf-8'))


if __name__ == "__main__":
    hello_server()
