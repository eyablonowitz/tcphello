import socket
import time
import multiprocessing
import re
from tcphello.main import hello_server


def test_hello_server():
    process = multiprocessing.Process(target=hello_server)
    process.start()
    while True:
        try:
            time.sleep(0.1)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('127.0.0.1', 12345))
                data = s.recv(1024)
                break
        except ConnectionRefusedError:
            pass
    assert re.match("^Hello.*", data.decode(encoding="utf-8"))
    process.kill()
