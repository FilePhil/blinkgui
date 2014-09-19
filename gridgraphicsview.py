from PySide import QtGui, QtCore


class GridGraphicsView(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        QtGui.QGraphicsView.__init__(self, parent)

    def heightForWidth(self, width):
        return width

    def mouseMoveEvent(self, event):
        if event.modifiers() == QtCore.Qt.ControlModifier:
            item = self.itemAt(event.pos())
            if item is not None:
                item.setSelected(True)
        QtGui.QGraphicsView.mouseMoveEvent(self, event)

    def resizeEvent(self, evt=None):
        size = evt.size()
        height = size.height()
        width = size.width()
        self.scene().grid.resize_tiles(min(height, width))





