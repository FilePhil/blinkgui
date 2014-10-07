#!/usr/bin/env python3
import sys
import time
from collections import namedtuple
from avrconnector import AVRConnector
from bmlparser import BMLReader

Size = namedtuple("size", "width height")


class AVRPlayer():
    def __init__(self):
        self.connector = AVRConnector()
        ret = self.connector.connect(True)
        time.sleep(2)
        if not ret:
            print("ERR")
            sys.exit(1)
        self.frames = []

    def load_frames(self, frames, size):
        for f in frames:
            packet = self.connector.pack_mcuf(f.tile_colors, size, False)
            self.frames.append((f.duration/1000, packet))

    def play(self, loop=False):
        while True:
            for f in self.frames:
                self.connector.write(f[1])
                time.sleep(f[0])
            if not loop:
                break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    reader = BMLReader()
    fra, info, (width, height) = reader.read_xml(sys.argv[1])
    player = AVRPlayer()
    player.load_frames(fra, Size(width, height))
    player.play(True)


