#!/usr/bin/env python3

import dbus
import dbus.service
import dbus.mainloop.glib
from PySide.QtCore import QCoreApplication

playlist_items = {}


class DBUSClient:
    def __init__(self):
        self.__bus = dbus.SessionBus()
        devices_obj = self.__bus.get_object("org.kde.kdeconnect", "/modules/kdeconnect")
        iface = dbus.Interface(devices_obj, dbus_interface="org.kde.kdeconnect.daemon")
        self.__dev = iface.devices()[0]
        obj = self.__bus.get_object("org.kde.kdeconnect", "/modules/kdeconnect/devices/%s" % self.__dev)
        ifa = dbus.Interface(obj, dbus_interface="org.kde.kdeconnect.device.notifications")
        ifa.connect_to_signal("notificationPosted", self.notification_posted)
        ifa.connect_to_signal("notificationRemoved", self.notification_removed)

    def notification_posted(self, msg_id):
        obj = self.__bus.get_object("org.kde.kdeconnect", "/modules/kdeconnect/devices/%s/notifications/%s"
                                    % (self.__dev, msg_id))
        iface = dbus.Interface(obj, dbus_interface="org.freedesktop.DBus.Properties")
        properties = iface.GetAll("org.kde.kdeconnect.device.notifications.notification")
        print("%s -> %s" % (properties["appName"], properties["ticker"]))
        #idx = blinkerface.add_notification(properties["appName"], properties["ticker"])
        idx = conn.iface.add_notification("blue-blink", properties["ticker"])
        playlist_items[int(msg_id)] = idx

    def notification_removed(self, msg_id):
        if int(msg_id) in playlist_items:
            conn.iface.remove_notification(playlist_items[int(msg_id)])
            del playlist_items[int(msg_id)]

if __name__ == "__main__":
    from dbus_connector import DBUSBlinkConnector
    conn = DBUSBlinkConnector()
    client = DBUSClient()
    app = QCoreApplication([])
    app.exec_()