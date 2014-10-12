import dbus


class DBUSBlinkConnector:

    def __init__(self):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SessionBus()
        obj = bus.get_object("de.ch.blink", "/de/ch/blink")
        self.iface = dbus.Interface(obj, dbus_interface="de.ch.blink")