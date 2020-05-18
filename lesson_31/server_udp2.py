import socket
import argparse
import traceback

from command.stat import cmd_stat

msgFromServer = "Hi UDP Client"
bytesToSend = str.encode(msgFromServer)


def cmd_cmd(message, address, UDPServerSocket):
    pass

def load_conf():  # Function for load server configuration
    parser = argparse.ArgumentParser(description="Server UDP")
    parser.add_argument('--host', '-i', default="127.0.0.1", required=False, help='Which IP adress')
    parser.add_argument('--port', '-p', default=5000, type=int, required=False, help='Which port')
    parser.add_argument('--buffer_size', '-b', default=1024, type=int, required=False, help='Buffer size')
    args = parser.parse_args()
    print(args)
    return args
def route(message, address, UDPServerSocket):
    print("Message from Client:{}".format(message))
    print("Client IP Address:{}".format(address))
    # Sending a reply to client
    if cmd_stat(message, address, UDPServerSocket):
        return
    elif cmd_cmd(message, address, UDPServerSocket):
        return

    UDPServerSocket.sendto(bytesToSend, address)

def start_server(cfg: dict):  # Function for start server
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    UDPServerSocket.bind((cfg['host'], cfg['port']))
    while True:
        message, address = UDPServerSocket.recvfrom(cfg['buffer_size'])  # read data from socket
        route(message, address, UDPServerSocket)


if __name__ == '__main__':

    config = load_conf()
    print("UDP server up and listening")

    while True:
        try:
            start_server(config)
        except:
            print(traceback.format_exc())
