#!/usr/bin/env python3
import dbus
import dbus.mainloop.glib
import cmd


class DBUSBlinkConnector:

    def __init__(self):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SessionBus()
        obj = bus.get_object("de.ch.blink", "/de/ch/blink")
        self.iface = dbus.Interface(obj, dbus_interface="de.ch.blink")


class Prompt(cmd.Cmd):
    prompt = '> '

    def do_add(self, line):
        idx = connector.iface.add_to_playlist(line)
        if idx == -1:
            print("ERR")
        else:
            print("OK. ID: %d" % idx)

    def help_add(self):
        print("Adds a file to the playlist.")

    def do_load_file(self, line):
        line = line.split(" ")
        connector.iface.load_clip(*line)
        print("OK")

    def help_load_file(self):
        print("Loads a .bml file to the storage")

    def do_clear(self, line):
        connector.iface.clear()
        print("OK")

    def do_remove(self, line):
        try:
            i = int(line)
        except ValueError:
            print("ERR")
        ret = connector.iface.remove_from_playlist(i)
        if ret:
            print("OK")
        else:
            print("ERR")

    def do_show(self, line):
        items = [str(x) for x in list(connector.iface.get_playlist())]
        for item in items:
            print(item)

    def do_show_clips(self, line):
        clips = [str(x) for x in list(connector.iface.get_available_clips())]
        for c in clips:
            print(c)

    def help_load_file(self):
        print("Reads a file and adds it to the list of available clips.")

if __name__ == '__main__':
    connector = DBUSBlinkConnector()
    Prompt().cmdloop()
