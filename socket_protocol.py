import struct
import socket
import threading
import sys

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def send_one_message(sock, data):
    data = bytes(data, "utf-8")
    length = len(data)
    sock.sendall(struct.pack('!I', length))
    sock.sendall(data)


def recv_one_message(sock):
    lengthbuf = recvall(sock, 4)
    length, = struct.unpack('!I', lengthbuf)
    return recvall(sock, length).decode("utf-8")


class BlinkServer:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((host, port))
            self.socket.listen(10)
            while True:
                conn, addr = self.socket.accept()
                t = threading.Thread(target=self.client_thread, args=(conn,))
                t.start()
            self.socket.close()
        except socket.error as msg:
            print("Bind failed. Error Code : " + str(msg))
            sys.exit()

    @staticmethod
    def add_to_playlist(sock, alias):
        raise NotImplementedError

    @staticmethod
    def remove_from_playlist(sock, it_id):
        raise NotImplementedError

    @staticmethod
    def clear_playlist(sock):
        raise NotImplementedError

    @staticmethod
    def load_clip(sock, params):
        raise NotImplementedError

    @staticmethod
    def get_available_clips(sock):
        raise NotImplementedError

    @staticmethod
    def get_playlist(sock):
        raise NotImplementedError

    @staticmethod
    def receive_file(sock):
        raise NotImplementedError

    def handle_message(self, conn):
        try:
            msg = recv_one_message(conn)
        except:
            print("Client connection closed")
            return False
        cmd, params = msg.split(" ", 1)
        if cmd == "a":
            self.add_to_playlist(conn, params)
        elif cmd == "d":
            self.remove_from_playlist(conn, params)
        elif cmd == "c":
            self.clear_playlist(conn)
        elif cmd == "l":
            self.load_clip(conn, params)
        elif cmd == "v":
            self.get_available_clips(conn)
        elif cmd == "p":
            self.get_playlist(conn)
        elif cmd == "f":
            self.receive_file(conn, params)
        return True

    def client_thread(self, conn):
        while True:
            if not self.handle_message(conn):
                break
        conn.close()


class BlinkClient:
    def __init__(self, host, port):
        try:
            print("Connecting to %s:%d" % (host, port))
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
        except:
            print("Connection could not be established")
            sys.exit(1)

    def add_to_playlist(self, alias):
        msg = "a %s" % alias
        send_one_message(self.socket, msg)
        return recv_one_message(self.socket)

    def remove_from_playlist(self, idx):
        msg = "d %d" % int(idx)
        send_one_message(self.socket, msg)
        return recv_one_message(self.socket)

    def clear_playlist(self):
        msg = "c 1"
        send_one_message(self.socket, msg)
        return recv_one_message(self.socket)

    def load_clip(self, file_name, alias):
        msg = "l %s,%s" % (file_name, alias)
        send_one_message(self.socket, msg)
        return recv_one_message(self.socket)

    def get_available_clips(self):
        msg = "v 1"
        send_one_message(self.socket, msg)
        return recv_one_message(self.socket)

    def get_playlist(self):
        msg = "p 1"
        send_one_message(self.socket, msg)
        return recv_one_message(self.socket)

    def send_data(self, alias, data):
        msg = "f %s %s" % (alias, data)
        send_one_message(self.socket, msg)
        return recv_one_message(self.socket)