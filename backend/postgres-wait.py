import socket
import sys
from time import sleep


def is_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        return True
    else:
        return False


while not is_open("db", 5432):
    print("Waiting for postgres", file=sys.stderr)
    sleep(1)
