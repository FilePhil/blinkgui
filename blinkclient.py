#!/usr/bin/env python3
import cmd
import sys
from socket_protocol import BlinkClient
from blinkconfig import *


class Prompt(cmd.Cmd):
    prompt = '> '

    def do_add(self, line):
        if len(line) == 0:
            self.help_add()
            return
        ret = connector.add_to_playlist(line)
        print(ret)

    def help_add(self):
        print("Usage: add <alias>")

    def do_load_file(self, line):
        line = line.split(" ")
        if len(line) != 2:
            self.help_load_file()
            return
        ret = connector.load_clip(*line)
        print(ret)

    def help_load_file(self):
        print("Usage: load_file <path> <alias>")

    def do_clear(self, line):
        ret = connector.clear_playlist()
        print(ret)

    def help_clear(self):
        print("Clears the playlist")

    def do_remove(self, line):
        try:
            i = int(line)
            ret = connector.remove_from_playlist(i)
            print(ret)
        except ValueError:
            print("ERR")

    def help_remove(self):
        print("Usage: remove <id>")

    def do_show(self, line):
        ret = connector.get_playlist()
        print(ret)

    def help_show(self):
        print("Shows the contents of the playlist")

    def do_show_clips(self, line):
        ret = connector.get_available_clips()
        print(ret)

    def help_show_clips(self):
        print("Shows all available (loaded) clips that can be added to the playlist")

    def do_quit(self, line):
        return True

    def do_send_file(self, line):
        file_name, alias = line.split(" ", 1)
        with open(file_name, "r") as f:
            read_data = f.read()
        ret = connector.send_data(alias, read_data)
        print(ret)

    def help_quit(self):
        print("Closes the client")

if __name__ == '__main__':
    args = sys.argv[1:]
    host = args[0] if len(args) > 0 else getstring("ethernet_host")
    port = int(args[1]) if len(args) == 2 else getint("ethernet_port")
    connector = BlinkClient(host, port)
    Prompt().cmdloop()
