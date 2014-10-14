#!/usr/bin/env python3

import socket
import sys
import threading
from avrconnector import AVRConnector, ConnectionType

HOST = ""
PORT = 8888


class BlinkConnector:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((HOST, PORT))
            self.socket.listen(10)
            while True:
                #wait to accept a connection - blocking call
                conn, addr = self.socket.accept()
                t = threading.Thread(target=self.client_thread, args=(conn,))
                t.start()
            self.socket.close()
        except socket.error as msg:
            print("Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]")
            sys.exit()

    def client_thread(self, conn):
        while True:
            data = conn.recv(1024)
            avr_connector.write(data)
            if not data:
                break
        conn.close()


if __name__ == "__main__":
    avr_connector = AVRConnector()
    avr_connector.connect(ConnectionType.bluetooth)
    connector = BlinkConnector()

