#!/usr/bin/env python3
from collections import namedtuple
from avrconnector import AVRConnector
import random
import time
Size = namedtuple("size", "width height")


if __name__ == "__main__":
    conn = AVRConnector()
    conn.connect(True)
    #time.sleep(2)
    grid_size = Size(3, 3)
    while True:
        #colors = []
        #for x in range(grid_size.height*grid_size.width):
        #    colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        #conn.write_frame(colors, grid_size)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        conn.write_single_color(color, grid_size)
        time.sleep(0.5)



