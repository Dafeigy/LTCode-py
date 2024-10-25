import socket

class UDP_Client():

    def __init__(self, addr, port) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((addr, port))
    def send(self, data, target):
        self.sock.sendto(data, target)


    def receive(self):
        data, address = self.sock.recvfrom(4096)
        return data