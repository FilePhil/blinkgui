#!/usr/bin/env python3

import os
import time
import json
from io import StringIO
from threading import Thread
from threading import Condition
from socket_protocol import *
from blinkconfig import *
from avrconnector import AVRConnector, ConnectionType
from bmlparser import BMLReader

Size = namedtuple("size", "width height")
grid_size = Size(3, 3)

playlist_items = []
continue_condition = Condition()


class AVRPlayer():
    def __init__(self):
        self.connector = AVRConnector()
        ret = self.connector.connect(ConnectionType.usb)
        if not ret:
            print("ERR")
            sys.exit(1)
        self.clips = {}

    def load_clips(self, file_names):
        """
        :param files: {}
        :return:
        """
        reader = BMLReader()
        for f in file_names:
            fra, info, (width, height) = reader.read_xml(file_names[f])
            frames = []
            for frame in fra:
                packet = self.connector.pack_mcuf(frame.tile_colors, grid_size, False)
                frames.append((frame.duration/1000, packet))
            self.clips[f] = frames

    def play(self, video):
        v = self.clips[video]
        for frame in v:
            self.connector.write(frame[1])
            time.sleep(frame[0])


class BlinkDisplayThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            playlist = list(playlist_items)
            if len(playlist) == 0:
                with continue_condition:
                    continue_condition.wait()
            for msg in playlist:
                item = msg["alias"]
                player.play(item)


class EthernetSocket(BlinkServer):
    def __init__(self):
        BlinkServer.__init__(self, getstring("ethernet_host"), getint("ethernet_port"))

    @staticmethod
    def add_to_playlist(sock, alias):
        if not alias in player.clips:
            send_one_message(sock, "ERROR")
            return
        di = {"alias": alias}
        playlist_items.append(di)
        with continue_condition:
            continue_condition.notifyAll()
        send_one_message(sock, str(len(playlist_items)-1))

    @staticmethod
    def remove_from_playlist(sock, it_id):
        item_id = int(it_id)
        try:
            del playlist_items[item_id]
            send_one_message(sock, "OK")
        except IndexError:
            send_one_message(sock, "ERROR")

    @staticmethod
    def clear_playlist(sock):
        global playlist_items
        playlist_items = []
        send_one_message(sock, "OK")

    @staticmethod
    def load_clip(sock, params):
        file_name, alias = params.split(",")
        player.load_clips({alias: file_name})
        send_one_message(sock, "OK")

    @staticmethod
    def get_available_clips(sock):
        send_one_message(sock, str(list(player.clips.keys())))

    @staticmethod
    def get_playlist(sock):
        lis = ["%d -> %s" % (idx, str(item["alias"])) for idx, item in enumerate(playlist_items)]
        send_one_message(sock, str(lis))

    @staticmethod
    def receive_file(sock, dat):
        alias, data = dat.split(" ", 1)
        player.load_clips({alias: StringIO(data)})
        send_one_message(sock, "OK")



if __name__ == "__main__":
    player = AVRPlayer()
    if len(sys.argv) == 2:
        files = json.load(open(sys.argv[1], "r"))
        player.load_clips(files)
    elif os.path.isfile("playlist.cfg"):
        files = json.load(open("playlist.cfg", "r"))
        player.load_clips(files)
    thread = BlinkDisplayThread()
    thread.start()
    socket = EthernetSocket()
