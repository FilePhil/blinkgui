#!/usr/bin/env python3
from collections import namedtuple
from avrconnector import AVRConnector
import random
import time
Size = namedtuple("size", "width height")


if __name__ == "__main__":
    conn = AVRConnector()
    conn.connect()
    time.sleep(4)
    grid_size = Size(3, 3)
    num_tiles = grid_size.height*grid_size.width
    while True:
        colors = []
        pos = random.randint(0, num_tiles-1)
        for x in range(num_tiles):
            colors.extend([(0, 0, 0)])
        colors[pos] = (0, 0, 155)
        conn.write_frame(colors, grid_size)
        time.sleep(1)



