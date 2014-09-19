from collections import namedtuple
Moves = namedtuple("moves", "left up right down")
Pos = namedtuple("pos", "x y")
FrameInfo = namedtuple("frame", "frame_number frame")
Grid_Size = namedtuple("grid_size", "width height")

HEADER_FIELDS = ["title", "description", "creator", "author", "email", "loop"]
RO_FIELDS = ["bits", "channels"]
EMPTY_HEADER = {"bits": 8, "channels": 3, "title": "Untitled", "description": None, "creator": None, "author": None,
                "email": None, "loop": None}
FILE_FILTER = "Blinkenlights Markup (*.bml) (*.bml);;All files (*.*)"
EXPORT_FILTER = "Images (*.png) (*.png)"
IMPORT_FILTER = "Images (*.png) (*.png)"

# DEFAULTS
DEFAULT_GRID_SIZE = Grid_Size(10, 10)
DEFAULT_TILE_COLOR = (0, 0, 0)
DEFAULT_FRAME_DURATION = 100
DEFAULT_PEN_COLOR = (255, 255, 255)
MAX_ZOOM = 40
ZOOM_STEP = 0.05
GRID_LINE_COLOR = (30, 30, 30)
GRID_WIDTH = 1
BACKGROUND_COLOR = (30, 30, 30)