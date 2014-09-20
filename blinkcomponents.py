from PySide import QtGui, QtCore
import time
import random
from colorgenerator import *
from blinkconfig import *
import numpy as np
from PIL import Image, ImageFont, ImageDraw


class Frame:
    def __init__(self, duration, tile_colors):
        self.duration = duration
        self.tile_colors = tile_colors


# noinspection PyCallByClass,PyTypeChecker,PyArgumentList
class Tile(QtGui.QGraphicsRectItem):
    def __init__(self, idx, grid, pos):
        super(Tile, self).__init__()
        self.__grid = grid
        self.id = idx
        self.pos = pos
        self.setBrush(QtGui.QColor.fromRgb(*DEFAULT_TILE_COLOR))
        pen = QtGui.QPen(QtGui.QColor.fromRgb(*GRID_LINE_COLOR))
        pen.setWidth(GRID_WIDTH)
        self.setPen(pen)
        self.__grid.add_item(self)
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable)

    def mouseMoveEvent(self, event):
        if QtGui.QApplication.keyboardModifiers() != 0:
            return
        if event.buttons() != QtCore.Qt.NoButton:
            item = self.__grid.scene.itemAt(event.pos())
            if item is None:
                return
        if event.buttons() == QtCore.Qt.LeftButton:
            item.set_color(self.__grid.current_color)

    def mouseReleaseEvent(self, event):
        if QtGui.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier:
            QtGui.QGraphicsItem.mouseReleaseEvent(self, event)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and \
                        QtGui.QApplication.keyboardModifiers() != QtCore.Qt.ControlModifier\
                and QtGui.QApplication.keyboardModifiers() != QtCore.Qt.ShiftModifier:
            self.__grid.tile_colored.emit(self.id, self.brush().color().name())
            self.set_color(self.__grid.current_color)
        if QtGui.QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
            self.__grid.mouse_shift_event.emit(self.id)

    @property
    def color(self):
        return self.brush().color().getRgb()[:3]

    """
    color: [r,g,b]
    """

    def set_color(self, color, persist=True):
        self.setBrush(QtGui.QBrush(QtGui.QColor.fromRgb(*color)))
        if persist:
            self.__grid.get_current_frame().tile_colors[self.id] = color

    def _swap_selection(self):
        if self.isSelected():
            self.setSelected(False)
        else:
            self.setSelected(True)


# noinspection PyCallByClass,PyArgumentList,PyTypeChecker
class Grid(QtCore.QObject):
    tile_colored = QtCore.Signal(int, str)
    playback_stopped = QtCore.Signal(bool)
    mouse_shift_event = QtCore.Signal(int)

    def __init__(self, widget_size, scene, grid_size, frames=None):
        super(Grid, self).__init__()
        self.__buffer = None
        self.allow_resize = True
        self.grid_size = grid_size
        self.connection = None
        self.scene = scene
        self.scene.grid = self
        self.__stopped = True
        self.__looping = False
        self.tiles = []
        tile_id = 0
        for y in range(0, self.grid_size.height):
            for x in range(0, self.grid_size.width):
                self.tiles.append(Tile(tile_id, self, Pos(x, y)))
                tile_id += 1

        self.resize_tiles(widget_size)
        if frames is None:
            self.frames = [Frame(DEFAULT_FRAME_DURATION, [DEFAULT_TILE_COLOR] * (len(self.tiles)))]
        else:
            self.frames = frames
        self.current_color = DEFAULT_PEN_COLOR
        self.load_frame_number(0)
        self.current_frame_num = 0
        self.widget_size = widget_size

    def add_item(self, item):
        self.scene.addItem(item)

    def persist_tiles(self, clear_selection=False):
        tile_colors = self.get_current_frame().tile_colors
        for t in self.tiles:
            tile_colors[t.id] = t.color
        if clear_selection:
            self.select_all_tiles(False)

    def _calculate_item_size(self, widget_size):
        return int(widget_size / self.grid_size[0] - 1)

    def resize_tiles(self, size, item_size=None):
        if not self.allow_resize:
            return
        self.widget_size = size
        self.scene.setSceneRect(QtCore.QRectF())
        if item_size is None:
            item_size = self._calculate_item_size(size)
        for t in self.tiles:
            t.setRect(t.pos.x*item_size, t.pos.y*item_size, item_size-GRID_WIDTH, item_size-GRID_WIDTH)
        self.scene.setSceneRect(QtCore.QRectF(0, 0, size, size))

    def go_to_next_frame(self):
        if self.current_frame_num < len(self.frames):
            self.load_frame_number(self.current_frame_num + 1)
            return True
        return False

    def go_to_prev_frame(self):
        if self.current_frame_num > 0:
            self.load_frame_number(self.current_frame_num - 1)
            return True
        return False

    def _load_frame(self, frame, persist=True):
        for idx, t in enumerate(self.tiles):
            t.set_color(frame.tile_colors[idx], persist)

    def load_frame_number(self, frame_number):
        if frame_number == -1:
            frame_number = self.get_number_of_frames()-1
        self.current_frame_num = frame_number
        self._load_frame(self.frames[self.current_frame_num])

    def tint_selected_tiles(self):
        for tile in self.scene.selectedItems():
            tile.set_color(self.current_color)

    def create_new_frame(self, duration=DEFAULT_FRAME_DURATION):
        new_frame = Frame(duration, [DEFAULT_TILE_COLOR] * (len(self.tiles)))
        self.frames.insert(self.current_frame_num + 1, new_frame)
        self.current_frame_num += 1
        self._load_frame(self.frames[self.current_frame_num], False)

    def insert_frame(self, frame, pos=None):
        if pos is None:
            self.frames.append(frame)
        else:
            self.frames.insert(pos, frame)

    def insert_frame_with_colors(self, frame_colors, pos=None):
        f = Frame(DEFAULT_FRAME_DURATION, frame_colors)
        self.insert_frame(f, pos)

    def duplicate_frame(self):
        current_frame = self.get_current_frame()
        new_frame = Frame(current_frame.duration, list(current_frame.tile_colors))
        self.frames.insert(self.current_frame_num + 1, new_frame)
        self.current_frame_num += 1
        self._load_frame(self.frames[self.current_frame_num], False)

    def get_current_frame_info(self):
        return FrameInfo(self.current_frame_num, self.frames[self.current_frame_num])

    def get_current_frame(self):
        return self.frames[self.current_frame_num]

    def set_current_duration(self, duration):
        self.frames[self.current_frame_num].duration = duration

    def get_current_duration(self):
        return self.frames[self.current_frame_num].duration

    def delete_frame(self):
        if len(self.frames) == 1:
            return
        del self.frames[self.current_frame_num]
        if self.current_frame_num > 0:
            self.current_frame_num -= 1
        self.refresh()

    def refresh(self):
        self._load_frame(self.get_current_frame())

    def play_sequence(self, on_device=False):
        self.__stopped = False
        while not self.__stopped:
            for f in self.frames:
                if on_device:
                    self.connection.write_frame(f.tile_colors, self.grid_size)
                else:
                    self._load_frame(f, False)
                QtGui.QApplication.processEvents()
                time.sleep(f.duration / 1000.0)
                if self.__stopped:
                    break
            if not self.__looping:
                break
        self.__stopped = True
        if not on_device:
            self.load_frame_number(0)
        self.playback_stopped.emit(on_device)

    def is_stopped(self):
        return self.__stopped

    def select_tile(self, idx, selected=True):
        self.tiles[idx].setSelected(selected)
        self.persist_tiles()

    def select_all_tiles(self, selected=True):
        for t in self.tiles:
            t.setSelected(selected)
        self.persist_tiles()

    def invert_selection(self):
        for t in self.tiles:
            t.setSelected(not t.isSelected())
        self.persist_tiles()

    def delete_selected(self):
        for t in self.tiles:
            if t.isSelected():
                t.set_color(DEFAULT_TILE_COLOR)
        self.select_all_tiles(False)

    def get_selection(self):
        selection = []
        topmost = self.grid_size.height
        bottommost = -1
        leftmost = self.grid_size.width
        rightmost = -1
        for t in self.tiles:
            if t.isSelected():
                selection.append(t)
                leftmost = t.pos.x if t.pos.x < leftmost else leftmost
                rightmost = t.pos.x if t.pos.x > rightmost else rightmost
                topmost = t.pos.y if t.pos.y < topmost else topmost
                bottommost = t.pos.y if t.pos.y > bottommost else bottommost
        return [t for t in self.tiles if t.isSelected()], (leftmost, topmost, rightmost, bottommost)

    def has_selected_tiles(self):
        return any([t.isSelected() for t in self.tiles])

    def select_by_color(self, color):
        for t in self.tiles:
            if t.brush().color().getRgb()[:3] == color:
                t.setSelected(True)
            else:
                t.setSelected(False)
        self.persist_tiles()

    def copy_selection(self, cut=False):
        copy = []
        for t in self.tiles:
            if t.isSelected():
                copy.append(t.color)
                if cut:
                    t.set_color(DEFAULT_TILE_COLOR)
            else:
                copy.append((-1, -1, -1))
        self.__buffer = copy

    def paste(self):
        for idx, tile_color in enumerate(self.__buffer):
            tile = self.tiles[idx]
            if not tile_color == (-1, -1, -1):
                tile.set_color(tile_color, persist=False)
                tile.setSelected(True)
            else:
                tile.setSelected(False)

    def shift_contents_left(self):
        for y in range(0, self.grid_size.height):
            for x in range(0, self.grid_size.width):
                pos = x * self.grid_size.width + y
                r = self.tiles[pos]
                if r.pos.x == self.grid_size.width - 1:
                    r.set_color(DEFAULT_TILE_COLOR)
                elif pos < len(self.tiles) - 1:
                    r.set_color(self.tiles[pos + 1].color)

    def get_possible_moves(self, rect):
        x1, y1, x2, y2 = rect
        return Moves(left=(x1 != 0), up=(y1 != 0), right=(x2 != self.grid_size.width - 1),
                     down=(y2 != self.grid_size.height - 1))

    def shift(self, direction):
        if self.has_selected_tiles():
            self._shift_selection(direction)
        else:
            if direction == "right":
                self._shift_contents_right()
            elif direction == "left":
                self.shift_contents_left()
            elif direction == "up":
                self._shift_contents_up()
            elif direction == "down":
                self._shift_contents_down()

    def _shift_selection(self, direction):
        selection, bounding_rect = self.get_selection()
        move_offsets = {"right": 1, "left": -1, "up": -self.grid_size.width, "down": self.grid_size.width}
        moves = self.get_possible_moves(bounding_rect)
        if not moves._asdict()[direction]:
            return
        frame = self.get_current_frame()
        if direction == "right" or direction == "down":
            selection = reversed(selection)
        for tile in selection:
            idx = tile.id
            new_tile = self.tiles[idx + move_offsets[direction]]
            tile.setSelected(False)
            new_tile.set_color(tile.color, persist=False)
            new_tile.setSelected(True)
            tile.set_color(frame.tile_colors[idx], persist=False)

    def _shift_contents_right(self):
        for y in range(self.grid_size.height, 0, -1):
            for x in range(self.grid_size.width, 0, -1):
                pos = (x - 1) * self.grid_size.width + y - 1
                r = self.tiles[pos]
                if r.pos.x == 0:
                    r.set_color(DEFAULT_TILE_COLOR)
                elif pos > 0:
                    r.set_color(self.tiles[pos - 1].color)

    def _shift_contents_up(self):
        for y in range(0, self.grid_size.height):
            for x in range(0, self.grid_size.width):
                pos = self.grid_size.width * x + y
                r = self.tiles[pos]
                if r.pos.y == self.grid_size.height - 1:
                    r.set_color(DEFAULT_TILE_COLOR)
                else:
                    r.set_color(self.tiles[pos + self.grid_size.width].color)

    def _shift_contents_down(self):
        for y in range(self.grid_size.height, 0, -1):
            for x in range(self.grid_size.width, 0, -1):
                pos = (x - 1) * self.grid_size.height + y - 1
                r = self.tiles[pos]
                if r.pos.y == 0:
                    r.set_color(DEFAULT_TILE_COLOR)
                else:
                    r.set_color(self.tiles[pos - self.grid_size.width].color)

    def randomize_selected_tiles(self):
        for t in self.tiles:
            if t.isSelected():
                t.set_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def _get_tile_colors(self):
        return [t.color for t in self.tiles]

    def _set_tile_colors(self, colors, persist=True):
        for t, c in zip(self.tiles, colors):
            t.set_color(c, persist)

    def rotate_left(self):
        colors = np.concatenate(np.rot90(np.array_split(self._get_tile_colors(), self.grid_size.width))).tolist()
        self._set_tile_colors(colors)

    def rotate_right(self):
        colors = np.concatenate(np.rot90(np.array_split(self._get_tile_colors(), self.grid_size.width), 3)).tolist()
        self._set_tile_colors(colors)

    def stop_playback(self):
        self.__stopped = True

    def set_looping(self, enabled):
        self.__looping = enabled

    def get_total_duration(self):
        return sum([f.duration for f in self.frames])

    def get_number_of_frames(self):
        return len(self.frames)

    def get_bitmap_image(self, frame=None):
        if frame is None:
            colors = list(self.get_current_frame().tile_colors)
        else:
            colors = list(frame.tile_colors)
        image = QtGui.QImage(self.grid_size.width, self.grid_size.height, QtGui.QImage.Format_RGB32)
        transform = QtGui.QTransform()
        for x in range(self.grid_size.width-1, -1, -1):
            for y in range(0, self.grid_size.height):
                image.setPixel(x, y, QtGui.QColor(*colors.pop(0)).rgb())
        transform.rotate(270)
        image = image.transformed(transform)
        return image

    def get_bitmap_images(self):
        for f in self.frames:
            yield self.get_bitmap_image(f)

    def generate_linear_color_gradient(self, params):
        """
        :param params: steps phase_red phase_green phase_blue central_value value_range
        """
        freq = math.pi*2/params.steps
        #freq, phase_red, phase_green, phase_blue, center=None, width=None
        grad = linear_color_gradient(freq, params.phase_red, params.phase_green, params.phase_blue,
                                     params.central_value, params.value_range, length=params.steps*self.grid_size.width)
        chunks = [grad[x:x+self.grid_size.width] for x in range(0, len(grad), 1)]
        for f in range(0, params.steps):
            self.create_new_frame(duration=params.duration)
            self.get_current_frame().tile_colors = chunks[f]*self.grid_size.height
            self._load_frame(self.get_current_frame())

    def generate_function(self, params):
        try:
            frames = sine_cosine(self.grid_size, *params)
            self.frames.extend(frames)
            self.current_frame_num += len(frames)
            return True, ""
        except (SyntaxError, NameError) as err:
            return False, err

    def _generate_text(self, params):
        font = ImageFont.truetype("VCR_OSD_MONO.ttf", params.font_size)
        dimensions = font.getsize(params.text)
        image = Image.new("RGB", (dimensions[0], self.grid_size.height), DEFAULT_TILE_COLOR)
        draw = ImageDraw.Draw(image)
        start = (0, self.grid_size.height/2 - 0.5*dimensions[1])
        draw.text(start, params.text, (255, 255, 255), font=font)
        return image.getdata()

    def generate_ticker_font(self, params):
        """for char in params.text:
            img = self._generate_char(char, params)
            self.create_new_frame(duration=params.duration)
            self._set_tile_colors(img.getdata())
        """
        img = self._generate_text(params)
        for color in img:
            print(color)