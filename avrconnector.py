import struct
import serial
from blinkconfig import config
from sys import platform
import logging


class AVRConnector():
    def __init__(self, baud_rate=38400):
        self.baud_rate = baud_rate
        self.__handlers = []
        self.write = None
        self.close = None
        self.active = False

    def _connect_linux(self):
        dev = config.getstring("serial_device_linux")
        for x in [""] + list(range(0, 10)):
            try:
                logging.info("Trying to connect to %s%s" % (dev, str(x)))
                ser = serial.Serial("%s%s" % (dev, str(x)), baudrate=self.baud_rate)
                for h in self.__handlers:
                    h()
                return ser.write, ser.close
            except serial.serialutil.SerialException:
                pass
        return False

    def _connect_bluetooth(self):
        try:
            import socket
            server_mac = config.getstring("bluetooth_mac")
            s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            s.settimeout(config.getint("connection_timeout"))
            s.connect((server_mac, 1))
            for h in self.__handlers:
                h()
            return s.send, s.close
        except:
            return False

    def _connect_windows(self):
        try:
            ser = serial.Serial(port=config.getstring("serial_device_windows"), baudrate=self.baud_rate)
            for h in self.__handlers:
                    h()
            return ser.write, ser.close
        except:
            return False

    def connect(self, use_bluetooth=False):
        if use_bluetooth:
            ret = self._connect_bluetooth()
        elif platform == "win32":
            ret = self._connect_windows()
        else:
            ret = self._connect_linux()
        if not ret:
            return False
        else:
            self.write, self.close = ret
            self.active = True
            return True

    @staticmethod
    def pack_mcuf(dat, size, even_line_starts_left):
        if not even_line_starts_left:
            copy = list(dat)
            chunks = [copy[x:x+size.width] for x in range(0, len(copy), size.width)]
            dat = []
            for idx, c in enumerate(chunks):
                if idx % 2 == 1:
                    c.reverse()
                dat.extend(c)
        dat = [item for sub in dat for item in sub]
        data_len = len(dat)
        return struct.pack("!HHHHHH" + "B"*data_len, 13, 37, size.height, size.width, 3, 255, *dat)

    def write_frame(self, colors, grid_size, even_line_starts_left=False):
        d = self.pack_mcuf(colors, grid_size, even_line_starts_left)
        self.write(d)

    def add_connection_handler(self, handler):
        self.__handlers.append(handler)

    def is_active(self):
        return self.active

    def close(self):
        self.close()
        self.active = False

# TESTS
if __name__ == "__main__":
    conn = AVRConnector()
    conn.connect()
    while True:
        data = input("> ").split(" ")
        data = [int(d) for d in data]
        print(data*15)
        conn.write_colors(data*15)