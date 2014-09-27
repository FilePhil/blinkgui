import struct
import serial
from PySide import QtCore
from sys import platform

tr = lambda string: QtCore.QCoreApplication.translate("avrconnector", string)


class AVRConnector():
    def __init__(self, baud_rate=1000000):
        self.baud_rate = baud_rate
        self.__handlers = []
        self.__ser = None
        self.live_mode = False

    def set_live_mode(self, value):
        self.live_mode = value

    def _connect_linux(self):
        dev = "/dev/ttyUSB"
        for x in range(0, 10):
            try:

                self.__ser = serial.Serial("%s%d" % (dev, x), baudrate=self.baud_rate)
                for h in self.__handlers:
                    h(x)
                return True, ""
            except serial.serialutil.SerialException:
                pass
        return False, tr("Connection could not be established")

    def _connect_windows(self):
        self.__ser = serial.Serial(port="\\.\COM3", baudrate=self.baud_rate)
        for h in self.__handlers:
                h("ok")
        return True, ""
        #return False,
        # tr("Win: Connection could not be established")

    def connect(self):
        if platform == "win32":
            return self._connect_windows()
        else:
            return self._connect_linux()

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
        self.__ser.write(d)
        self.__ser.flush()

    def write(self, byte_list):
        self.__ser.write(byte_list)

    def add_connection_handler(self, handler):
        self.__handlers.append(handler)

    def is_active(self):
        return self.__ser.isOpen()

    def close(self):
        self.__ser.close()

# TESTS
if __name__ == "__main__":
    conn = AVRConnector()
    conn.connect()
    while True:
        data = input("> ").split(" ")
        data = [int(d) for d in data]
        print(data*15)
        conn.write_colors(data*15)