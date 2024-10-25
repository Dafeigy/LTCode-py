import socket

def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))


def prPurple(skk): print("\033[95m {}\033[00m".format(skk))


def prCyan(skk): print("\033[96m {}\033[00m".format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))


def prBlack(skk): print("\033[98m {}\033[00m".format(skk))


class UDP_Client():

    def __init__(self, addr, port) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((addr, port))
    def send(self, data, target):
        self.sock.sendto(data, target)


    def receive(self, addr):
        data, address = self.sock.recvfrom(4096)
        return data