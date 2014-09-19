from lxml import etree
from blinkcomponents import Frame
from PySide.QtGui import QColor


class BMLWriter:

    def __init__(self, width, height, bits=8, channels=3):
        self.blm_root = etree.Element("blm")
        self.width = width
        self.blm_root.set("width", str(width))
        self.blm_root.set("height", str(height))
        self.blm_root.set("bits", str(bits))
        self.blm_root.set("channels", str(channels))

    def set_header(self, **args):
        valid_arguments = ["title", "description", "creator", "author", "email", "loop"]
        if not "title" in args:
            return
        blm_header = etree.Element("header")
        for arg in args:
            if arg in valid_arguments and args[arg] is not None:
                elem = etree.Element(arg)
                elem.text = args[arg]
                blm_header.append(elem)
        self.blm_root.append(blm_header)

    def write_xml(self, frames, file_name):
        for frame in frames:
            frame_elem = etree.Element("frame")
            frame_elem.set("duration", str(frame.duration))
            tile_count = 0
            row = etree.Element("row")
            row_text = ""
            for color in frame.tile_colors:
                tile_count += 1
                row_text += str(QColor.fromRgb(*color).name()[1:])
                if tile_count == self.width:
                    tile_count = 0
                    row.text = row_text
                    frame_elem.append(row)
                    row = etree.Element("row")
                    row_text = ""
            self.blm_root.append(frame_elem)
        tree = etree.ElementTree(self.blm_root)
        tree.write(file_name)


class BMLReader:

    def __init__(self):
        pass

    @staticmethod
    def _chunks(string, n):
        for pos in range(0, len(string), n):
            yield string[pos:pos+n]

    def read_xml(self, file_name):
        tree = etree.parse(file_name)
        blm_root = tree.getroot()
        width = int(blm_root.get("width"))
        height = int(blm_root.get("height"))
        bits = int(blm_root.get("bits"))
        channels = int(blm_root.get("channels"))
        header = blm_root.find("header")
        info = {"title": None, "description": None, "creator": None, "author": None, "email": None, "loop": None}
        if header is not None:
            for elem in header.iter():
                if elem.tag in info:
                    info[elem.tag] = elem.text
        info["bits"] = bits
        info["channels"] = channels
        frames = []
        if bits <= 4:
            chunk_size = channels
        else:  # 5 <= bits <= 8
            chunk_size = 2*channels
        repetitions = int(6/chunk_size)
        for frame in blm_root.iter("frame"):
            tile_colors = []
            for row in frame.iter("row"):
                for c in self._chunks(row.text, chunk_size):
                    c *= repetitions
                    hexa = "#%s" % c
                    tile_colors.append(QColor(hexa).getRgb()[:3])
            duration = int(frame.get("duration"))
            frames.append(Frame(duration, tile_colors))
        return frames, info, (width, height)