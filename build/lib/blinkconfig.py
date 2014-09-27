from collections import namedtuple
from configparser import ConfigParser
from os.path import expanduser

Moves = namedtuple("moves", "left up right down")
Pos = namedtuple("pos", "x y")
FrameInfo = namedtuple("frame", "frame_number frame")
Size = namedtuple("size", "width height")

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
                "background_color": "30, 30, 30"}

DEFAULT_SECTION = "DEFAULT"


class Config(ConfigParser):
    def __init__(self, defaults):
        ConfigParser.__init__(self, defaults)

    def getcolor(self, key):
        value = ConfigParser.get(self, DEFAULT_SECTION, key)
        items = [int(val) for val in value.split(",")]
        return items

    def getint(self, key):
        return ConfigParser.getint(self, DEFAULT_SECTION, key)

    def getfloat(self, key):
        return ConfigParser.getfloat(self, DEFAULT_SECTION, key)

    def getstring(self, key):
        return str(ConfigParser.get(self, DEFAULT_SECTION, key))

    def getsize(self, key):
        value = ConfigParser.get(self, DEFAULT_SECTION, key)
        items = [int(val) for val in value.split(",")]
        assert len(items) == 2
        return Size(*items)


config = Config(default_values)
config.read("%s/.blinkrc" % expanduser("~"))
