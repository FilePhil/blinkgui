from PySide import QtGui


class CommandDeleteFrame(QtGui.QUndoCommand):
    def __init__(self, gui, description):
        super(CommandDeleteFrame, self).__init__(description)
        self.gui = gui
        self.pos, self.frame = self.gui.grid.get_current_frame_info()

    def redo(self):
        self.gui.grid.delete_frame()
        self.gui.update_frame_controls()

    def undo(self):
        self.gui.grid.insert_frame(self.frame, self.pos)
        self.gui.update_frame_controls()


class CommandColorChanged(QtGui.QUndoCommand):
    def __init__(self, gui, new_color, description, change_selected=True):
        super(CommandColorChanged, self).__init__(description)
        self.color = new_color
        self.gui = gui
        self.change_selected = change_selected
        self.old_color = self.gui.grid.current_color

    def _set_color(self, color):
        self.gui.grid.current_color = color
        self.gui.ui.colorButton.setPalette(QtGui.QColor.fromRgb(*color))
        # Change color of selected tiles when color
        #if not self.change_selected:
        #    return
        #for t in self.gui.grid.tiles:
        #    if t.isSelected():
        #        t.set_color(color)

    def redo(self):
        self._set_color(self.color)

    def undo(self):
        self._set_color(self.old_color)


class CommandTileColored(QtGui.QUndoCommand):
    def __init__(self, grid, tile_id, old_color, description):
        super(CommandTileColored, self).__init__(description)
        self.grid = grid
        self.tile_id = tile_id
        self.old_color = QtGui.QColor(old_color)

    def redo(self):
        pass

    def undo(self):
        self.grid.tiles[self.tile_id].set_color(self.old_color.getRgb())

