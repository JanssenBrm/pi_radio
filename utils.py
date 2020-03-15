import socket

def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)