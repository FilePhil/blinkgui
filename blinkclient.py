#!/usr/bin/env python3
from socket_protocol import BlinkClient
from blinkconfig import *
import cmd


class Prompt(cmd.Cmd):
    prompt = '> '

    def do_add(self, line):
        ret = connector.add_to_playlist(line)
        print(ret)

    def help_add(self):
        print("Adds a file to the playlist.")

    def do_load_file(self, line):
        line = line.split(" ")
        ret = connector.load_clip(*line)
        print(ret)

    def help_load_file(self):
        print("Loads a .bml file to the storage")

    def do_clear(self, line):
        ret = connector.clear_playlist()
        print(ret)

    def do_remove(self, line):
        try:
            i = int(line)
            ret = connector.remove_from_playlist(i)
            print(ret)
        except ValueError:
            print("ERR")

    def do_show(self, line):
        ret = connector.get_playlist()
        print(ret)

    def do_show_clips(self, line):
        ret = connector.get_available_clips()
        print(ret)

    def help_load_file(self):
        print("Reads a file and adds it to the list of available clips.")

if __name__ == '__main__':
    connector = BlinkClient(getstring("ethernet_host"), getint("ethernet_port"))
    Prompt().cmdloop()
