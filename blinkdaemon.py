#!/usr/bin/env python3

import dbus
import dbus.service
import sys
import os
import dbus.mainloop.glib
import time
import json
import signal
from collections import namedtuple
from avrconnector import AVRConnector
from PySide.QtCore import QCoreApplication
from threading import Thread
from threading import Condition
from bmlparser import BMLReader
Size = namedtuple("size", "width height")
grid_size = Size(3, 3)

playing_items = {}
continue_condition = Condition()


class AVRPlayer():
    def __init__(self):
        self.connector = AVRConnector()
        ret = self.connector.connect(True)
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
            notif = dict(playing_items)
            if len(notif) == 0:
                with continue_condition:
                    continue_condition.wait()
            for msg_id in notif:
                app = notif[int(msg_id)]["alias"]
                player.play(app)


class MyDBUSService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('de.ch.blink', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/de/ch/blink')
        self.id = 0

    @dbus.service.method('de.ch.blink', in_signature='s', out_signature='i')
    def add_to_playlist(self, alias):
        if not alias in player.clips:
            return -1
        di = {"alias": alias}
        idx = int(self.id)
        playing_items[idx] = di
        self.id += 1
        with continue_condition:
            continue_condition.notifyAll()
        return idx

    @dbus.service.method('de.ch.blink', in_signature='i', out_signature='b')
    def remove_from_playlist(self, notif_id):
        if notif_id in playing_items:
            del playing_items[notif_id]
            return True
        return False

    @dbus.service.method('de.ch.blink')
    def clear_playlist(self):
        global playing_items
        playing_items = {}

    @dbus.service.method('de.ch.blink', in_signature='ss', out_signature='b')
    def load_video(self, file_name, alias):
        player.load_clips({alias: file_name})
        return True

    @dbus.service.method('de.ch.blink', out_signature='as')
    def get_available_clips(self):
        return list(player.clips.keys())

    @dbus.service.method('de.ch.blink', out_signature='ai')
    def get_playing_ids(self):
        return playing_items.keys()

    @dbus.service.method('de.ch.blink', in_signature='i', out_signature='as')
    def get_notification(self, notif_id):
        if notif_id in playing_items:
            return [playing_items[notif_id]["appName"], playing_items[notif_id]["ticker"]]
        return ""

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    player = AVRPlayer()
    if os.path.isfile("notifications.cfg"):
        files = json.load(open("notifications.cfg", "r"))
        player.load_clips(files)
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    thread = BlinkDisplayThread()
    thread.start()
    service = MyDBUSService()
    app = QCoreApplication([])
    app.exec_()
