from collections import namedtuple
from os.path import expanduser

VERSION = "1.0.8"
AUTHOR = "Christoph Hirtz"
MAIL = "christoph.hirtz@online.de"

Moves = namedtuple("moves", ['left', 'up', 'right', 'down'])
Pos = namedtuple("pos", ['x', 'y'])
FrameInfo = namedtuple("frame", ['frame_number', 'frame'])
Size = namedtuple("size", ['width', 'height'])

HEADER_FIELDS = ["title", "description", "creator", "author", "email", "loop"]
RO_FIELDS = ["bits", "channels"]
EMPTY_HEADER = {"bits": 8, "channels": 3, "title": "Untitled", "description": None, "creator": None, "author": None,
                "email": None, "loop": None}
FILE_FILTER = "Blinkenlights Markup (*.bml) (*.bml);;All files (*.*)"
EXPORT_FILTER = "Images (*.png) (*.png)"
IMPORT_FILTER = "Images (*.png) (*.png)"
FONT_FILTER = "TrueType Fonts (*.ttf) (*.ttf)"
default_values = {"grid_size": "10, 10",
                "tile_color": "0, 0, 0",
                "frame_duration": "100",
                "pen_color": "255, 255, 255",
                "font": "VCR_OSD_MONO.ttf",
                "max_zoom": "40",
                "zoom_step": "0.05",
                "grid_line_color": "30, 30, 30",
                "grid_width": "1",
                "background_color": "30, 30, 30",
                "bluetooth_mac": "98:D3:31:50:0E:E7",
                "serial_device_linux": "/dev/ttyUSB",
                "serial_device_windows": "\\.\COM3",
                "serial_device_macos": "/dev/ttyusb",
                "bluetooth_device_windows": "\\.\COM5",
                "bluetooth_device_macos": "/dev/BLUE-DevB",
                "ethernet_host": "127.0.0.1",
                "ethernet_port": "2222",
                "connection_timeout": "10"}

DEFAULT_SECTION = "DEFAULT"

try:
    from configparser import ConfigParser
    config = ConfigParser(default_values)
    config.read("%s/.blinkrc" % expanduser("~"))

    def getcolor(key):
        value = config.get(DEFAULT_SECTION, key)
        items = [int(val) for val in value.split(",")]
        return items

    def getint(key):
        return config.getint(DEFAULT_SECTION, key)

    def getfloat(key):
        return config.getfloat(DEFAULT_SECTION, key)

    def getstring(key):
        return str(config.get(DEFAULT_SECTION, key))

    def setvalue(key, value):
        config.set(DEFAULT_SECTION, key, str(value))

    def getsize(key):
        value = config.get(DEFAULT_SECTION, key)
        items = [int(val) for val in value.split(",")]
        assert len(items) == 2
        return Size(*items)


except ImportError:
    pass
