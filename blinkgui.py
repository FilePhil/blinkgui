#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import locale
from blinkcomponents import *
from mainwindow import Ui_MainWindow
from bmlparser import BMLReader, BMLWriter
from undocommands import *
from blinkconfig import *
from avrconnector import AVRConnector, ConnectionType

tr = lambda string: QtCore.QCoreApplication.translate("GUI", string)


# noinspection PyCallByClass,PyTypeChecker
class BlinkGui(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, args, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.frame_id_label = QtGui.QLabel()
        self.statusBar.addPermanentWidget(self.frame_id_label)
        self.centralwidget.keyPressEvent = lambda event: self._modifier_event(0, event)
        self.centralwidget.keyReleaseEvent = lambda event: self._modifier_event(1, event)
        self._fill_info_table()
        self.__active_connection = None
        self.filename = None
        self.__zoom = 0
        self._initialize(getsize("grid_size"))
        if len(args) == 2:
            self._load(args[1])

    """
    BUTTON EVENTS
    """

    def _color_button_clicked(self):
        color = QtGui.QColorDialog.getColor(QtGui.QColor.fromRgb(*self.__grid.current_color))
        if color.isValid():
            self._set_working_color(color.getRgb()[:3])

    def _create_frame_button_clicked(self):
        self.__grid.create_new_frame()
        self.update_frame_controls()

    def _delete_frame_button_clicked(self):
        cmd = CommandDeleteFrame(self, tr("Delete frame"))
        self._exec_and_add_cmd(cmd)

    def _duplicate_frame_button_clicked(self):
        self.__grid.duplicate_frame()
        self.update_frame_controls()

    def _slider_moved(self, value):
        self.__grid.load_frame_number(value)
        self.update_frame_controls()

    def _play(self):
        if self.__grid.is_stopped():
            self.progressBar.setMaximum(self.__grid.get_number_of_frames())
            self.frameSlider.setVisible(False)
            self.progressBar.setVisible(True)
            self.currentFrameBox.setEnabled(False)
            self.colorBox.setEnabled(False)
            self.actionPlayStop.setText(tr("Stop playback"))
            self.actionPlayStop.setIcon(QtGui.QIcon(":/icons/media-playback-stop.png"))
            self.actionPlayStopDevice.setEnabled(False)
            QtGui.QApplication.processEvents()
            self.__grid.play_sequence()
        else:
            self.__grid.stop_playback()

    def _play_device(self):
        if self.__grid.is_stopped():
            self.actionPlayStop.setEnabled(False)
            self.actionPlayStopDevice.setText(tr("Stop playback"))
            QtGui.QApplication.processEvents()
            self.__grid.play_sequence(on_device=True)
        else:
            self.__grid.stop_playback()

    def _save_as(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, tr("Save file"), "~", FILE_FILTER)
        if filename[0] == "":
            return
        self._save_file(filename[0])
        self.actionSave.setEnabled(True)

    def _save(self):
        if self.filename is not None:
            self._save_file(self.filename)
        else:
            self.save_as()

    def _load(self, filename=None):
        if filename is None:
            filename = QtGui.QFileDialog.getOpenFileName(self, tr("Open file"), "~", FILE_FILTER)
            if filename[0] == "":
                return
            filename = filename[0]
        if not os.path.isfile(filename):
            self._show_error(tr("File does not exist."))
        reader = BMLReader()
        frames, info, dimensions = reader.read_xml(filename)
        # re-initialize grid with new dimensions
        self._initialize(dimensions, frames=frames)
        self._apply_header_info(info)
        self.update_frame_controls()
        self.filename = filename

    def _export_frame(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, tr("Export frame"), "~", EXPORT_FILTER)
        if filename[0] == "":
            return
        writer = QtGui.QImageWriter(filename[0])
        image = self.__grid.get_bitmap_image()
        writer.write(image)

    def _export_frames(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, tr("Export frame"), "~", EXPORT_FILTER)
        if filename[0] == "":
            return
        file_name, file_extension = os.path.splitext(filename[0])
        writer = QtGui.QImageWriter(filename[0])
        for idx, image in enumerate(self.__grid.get_bitmap_images()):
            writer.setFileName("%s_%d%s" % (file_name, idx, file_extension))
            writer.write(image)

    def _import_frame(self):
        file_names = QtGui.QFileDialog.getOpenFileNames(self, tr("Import frame"), "~", IMPORT_FILTER)
        if len(file_names[0]) == 0:
            return
        for f in file_names[0]:
            reader = QtGui.QImageReader(f)
            image = reader.read()
            image = image.scaled(QtCore.QSize(*self.__grid.grid_size))
            transform = QtGui.QTransform()
            transform.rotate(270)
            image = image.transformed(transform)
            colors = []
            for x in range(0, self.__grid.grid_size.width):
                for y in range(self.__grid.grid_size.height-1, -1, -1):
                    colors.append(QtGui.QColor(image.pixel(x, y)).getRgb()[:3])
            self.__grid.insert_frame_with_colors(colors)
        self.__grid.load_frame_number(-1)
        self.update_frame_controls()

    """
    EVENT CALLBACKS
    """

    @QtCore.Slot(int)
    def _handle_mouse_shift_event(self, idx):
        """
        Called when a tile is shift-clicked
        :param idx: tile index [0 .. (m x n) -1]
        """
        self._set_working_color(self.__grid.get_current_frame().tile_colors[idx], change_selected=False)

    @QtCore.Slot(int, str, str)
    def _handle_tile_colored(self, idx, old_color):
        cmd = CommandTileColored(self.__grid, idx, old_color, tr("Color tile"))
        self._exec_and_add_cmd(cmd)

    @QtCore.Slot(bool)
    def _handle_playback_stopped(self, on_device):
        if on_device:
            self.actionPlayStopDevice.setText(tr("Play on device"))
            if self.__grid.get_number_of_frames() > 1:
                self.actionPlayStop.setEnabled(True)
        else:
            self.actionPlayStop.setText(tr("Play preview"))
            self.actionPlayStop.setIcon(QtGui.QIcon(":/icons/media-playback-start.png"))
            self.frameSlider.setVisible(True)
            self.progressBar.setVisible(False)
            self.currentFrameBox.setEnabled(True)
            self.colorBox.setEnabled(True)
            if self.__active_connection:
                self.actionPlayStopDevice.setEnabled(True)
            self.__grid.load_frame_number(0)
        self.update_frame_controls()

    @QtCore.Slot(int)
    def _handle_frame_changed(self, idx):
        self.progressBar.setValue(idx+1)

    def _set_working_color(self, color, change_selected=True):
        cmd = CommandColorChanged(self, color, tr("Set color"), change_selected)
        self._exec_and_add_cmd(cmd)

    def _get_header_params(self):
        header_params = {}
        for idx in range(self.metaInfoTable.rowCount()):
            item = self.metaInfoTable.item(idx, 1)
            if item is not None:
                value = item.text()
                header_params[self.metaInfoTable.item(idx, 0).text()] = value if value != "" else None
        return header_params

    def _save_file(self, filename):
        writer = BMLWriter(self.__grid.grid_size.width, self.__grid.grid_size.height)
        header_params = self._get_header_params()
        if any(header_params.values()):
            writer.set_header(**header_params)
        writer.write_xml(self.__grid.frames, filename)
        self.filename = filename

    def _apply_header_info(self, data):
        for idx, item in enumerate(RO_FIELDS+HEADER_FIELDS):
            text = str(data[item]) if data[item] is not None else None
            item2 = QtGui.QTableWidgetItem(text)
            if idx < len(RO_FIELDS):
                item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.metaInfoTable.setItem(idx, 1, item2)
        if data["loop"] is not None and data["loop"] == "yes":
            self.loopCheckbox.setChecked(True)
            self.__grid.set_looping(True)
        else:
            self.loopCheckbox.setChecked(False)
            self.__grid.set_looping(False)

    def update_frame_controls(self):
        num_frames = self.__grid.get_number_of_frames()
        # Update slider
        self.frameSlider.setMaximum(num_frames - 1)
        self.frameSlider.setSliderPosition(self.__grid.current_frame_num)
        # Update frame buttons
        if self.__grid.current_frame_num == num_frames - 1:
            self.actionGo_to_next_frame.setEnabled(False)
        else:
            self.actionGo_to_next_frame.setEnabled(True)
        if self.__grid.current_frame_num == 0:
            self.actionGo_to_previous_frame.setEnabled(False)
        else:
            self.actionGo_to_previous_frame.setEnabled(True)

        # Update current frame label
        self.frame_id_label.setText(tr("Frame: %d/%d, Total duration: %dms") %
                                         (self.__grid.current_frame_num + 1, num_frames,
                                          self.__grid.get_total_duration()))
        # Update delete frame button
        if num_frames <= 1:
            self.actionDelete_frame.setEnabled(False)
            self.actionPlayStop.setEnabled(False)
        else:
            self.actionDelete_frame.setEnabled(True)
            self.actionPlayStop.setEnabled(True)
        self.durationSpinBox.setValue(self.__grid.get_current_duration())

    def _go_to_next(self):
        self.__grid.go_to_next_frame()
        self.update_frame_controls()

    def _go_to_prev(self):
        self.__grid.go_to_prev_frame()
        self.update_frame_controls()

    def _go_to_frame(self):
        frame_num, ok = QtGui.QInputDialog.getInt(self, tr("Go to frame"), tr("Please enter the frame number:"),
                                                  QtGui.QLineEdit.Normal, 1, self.__grid.get_number_of_frames(), 0)
        if ok:
            self.__grid.load_frame_number(frame_num-1)
            self.update_frame_controls()

    @property
    def grid(self):
        return self.__grid

    @property
    def ui(self):
        return self

    def _new_document(self):
        grid_size = self.__grid.grid_size
        while True:
            try:
                text, ok = QtGui.QInputDialog.getText(self, tr("New file"), tr("Please enter the grid dimensions:"),
                                                      QtGui.QLineEdit.Normal,
                                                      "%dx%d" % (grid_size.width, grid_size.height))
                if ok:
                    dimensions = [int(x) for x in text.split("x")]
                    if len(dimensions) != 2:
                        continue
                    if 0 < dimensions[0] <= 1000 and 0 < dimensions[1] <= 1000:
                        self._initialize(dimensions)
                        break
                else:
                    break
            except ValueError:
                pass

    def _connect_to_device(self, connection_type):
        def connect_handler():
            self.menuConnect_to_device.setEnabled(False)
            self.actionPlayStopDevice.setEnabled(True)
            self.actionDisconnect.setEnabled(True)
        if not self.__active_connection:
            connection = AVRConnector()
            connection.add_connection_handler(connect_handler)
            ret = connection.connect(connection_type)
            if not ret:
                self._show_error(tr("Connection could not be established."))
                return
            self.__active_connection = connection
            self.__grid.connection = self.__active_connection
        else:
            self._show_error(tr("A connection already exists."))

    def _disconnect_device(self):
        assert self.__active_connection
        self.__active_connection.close()
        self.__active_connection = None
        self.menuConnect_to_device.setEnabled(True)
        self.actionDisconnect.setEnabled(False)

    def _disconnect_slots(self):
        try:
            for slot in self.__connected_slots:
                slot.disconnect()
        except AttributeError:
            pass
        self.__connected_slots = []

    def _connect_slot(self, action, handler):
        action.connect(handler)
        try:
            self.__connected_slots.append(action)
        except AttributeError:
            self.__connected_slots = [action]

    def closeEvent(self, event):
        self.close()
        event.accept()

    def _close(self):
        if not self.__grid.is_stopped():
            self.__grid.stop_playback()
        if self.__active_connection:
            self.__active_connection.close()
        QtGui.QMainWindow.close(self)

    def _connect_slots(self):
        self._disconnect_slots()
        self._connect_slot(self.colorButton.clicked, self._color_button_clicked)
        self._connect_slot(self.actionChoose_color.triggered, self._color_button_clicked)
        self._connect_slot(self.actionTint_selected_tiles.triggered, self.__grid.tint_selected_tiles)
        self._connect_slot(self.actionExit.triggered, self._close)
        self._connect_slot(self.actionDuplicate_frame.triggered, self._duplicate_frame_button_clicked)
        self._connect_slot(self.tintButton.clicked, self.__grid.tint_selected_tiles)
        self._connect_slot(self.actionCreate_new_frame.triggered, self._create_frame_button_clicked)
        self._connect_slot(self.actionDelete_frame.triggered, self._delete_frame_button_clicked)
        self._connect_slot(self.frameSlider.valueChanged, self._slider_moved)
        self._connect_slot(self.durationSpinBox.valueChanged, self._set_current_duration)
        self._connect_slot(self.actionNew.triggered, self._new_document)
        self._connect_slot(self.actionLoad_BLM.triggered, self._load)
        self._connect_slot(self.actionSave_as.triggered, self._save_as)
        self._connect_slot(self.actionSave.triggered, self._save)
        self._connect_slot(self.loopCheckbox.stateChanged, lambda state: self.__grid.set_looping(state))
        self._connect_slot(self.actionGo_to_next_frame.triggered, self._go_to_next)
        self._connect_slot(self.actionGo_to_previous_frame.triggered, self._go_to_prev)
        self._connect_slot(self.actionSelect_all.triggered, lambda: self.__grid.select_all_tiles(selected=True))
        self._connect_slot(self.actionDeselect_all.triggered, lambda: self.__grid.select_all_tiles(selected=False))
        self._connect_slot(self.actionInvert_selection.triggered, self.__grid.invert_selection)
        self._connect_slot(self.actionSelect_by_color.triggered,
                           lambda: self.__grid.select_by_color(self.__grid.current_color))
        self._connect_slot(self.actionUndo.triggered, self._undo)
        self._connect_slot(self.actionShift_left.triggered, lambda: self.__grid.shift("left"))
        self._connect_slot(self.actionShift_right.triggered, lambda: self.__grid.shift("right"))
        self._connect_slot(self.actionConnectBluetooth.triggered,
                           lambda: self._connect_to_device(connection_type=ConnectionType.bluetooth))
        self._connect_slot(self.actionConnectUSB.triggered,
                           lambda: self._connect_to_device(connection_type=ConnectionType.usb))
        self._connect_slot(self.actionConnectEthernet.triggered, self._connect_ethernet)
        self._connect_slot(self.actionDisconnect.triggered, self._disconnect_device)
        self._connect_slot(self.actionPlayStop.triggered, self._play)
        self._connect_slot(self.actionPlayStopDevice.triggered, self._play_device)
        self._connect_slot(self.actionRandomize_selected_tiles.triggered, self.__grid.randomize_selected_tiles)
        self._connect_slot(self.actionShift_content_down.triggered, lambda: self.__grid.shift("down"))
        self._connect_slot(self.actionShift_content_up.triggered, lambda: self.__grid.shift("up"))
        self._connect_slot(self.actionCopy_Selection.triggered, lambda: self._copy_or_cut(cut=False))
        self._connect_slot(self.actionCut_Selection.triggered, lambda: self._copy_or_cut(cut=True))
        self._connect_slot(self.actionPaste.triggered, self.__grid.paste)
        self._connect_slot(self.actionPersist_changes.triggered, lambda: self.__grid.persist_tiles(True))
        self._connect_slot(self.actionExport_frame.triggered, self._export_frame)
        self._connect_slot(self.actionExport_frames.triggered, self._export_frames)
        self._connect_slot(self.actionImport_from_image.triggered, self._import_frame)
        self._connect_slot(self.actionGenerate_color_gradient.triggered, self._generate_color_gradient)
        self._connect_slot(self.actionGenerate_function.triggered, self._generate_function)
        self._connect_slot(self.actionGenerate_ticker_font.triggered, self._generate_ticker_font)
        self._connect_slot(self.actionGo_to_frame.triggered, self._go_to_frame)
        self._connect_slot(self.actionZoom_in.triggered, lambda: self._zoom(1))
        self._connect_slot(self.actionZoom_out.triggered, lambda: self._zoom(-1))
        self._connect_slot(self.actionFit_zoom.triggered, lambda: self._zoom(0))
        self._connect_slot(self.actionRotate_left.triggered, self.__grid.rotate_left)
        self._connect_slot(self.actionRotate_right.triggered, self.__grid.rotate_right)
        self._connect_slot(self.actionDelete_colors.triggered, self.__grid.delete_selected)
        self._connect_slot(self.actionAbout.triggered, self._show_about)
        self._connect_slot(self.actionAbout_Qt.triggered, QtGui.QApplication.aboutQt)

    def _connect_ethernet(self):
        from simple_dialogs import EthernetDialog
        dialog = EthernetDialog(self)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            values = dialog.get_values()
            setvalue("ethernet_hostname", values.host_name)
            setvalue("ethernet_port", values.port)
            print (getint("ethernet_port"))
            self._connect_to_device(connection_type=ConnectionType.ethernet)

    def _show_about(self):
        QtGui.QMessageBox.about(self, "Blink", "Version: %s\nAuthor: %s" % (VERSION, AUTHOR))

    def _zoom(self, scale):
        zoom_step = getfloat("zoom_step")
        if scale > 0:
            self.__grid.allow_resize = False
            self.graphicsView.scale(1.0 + zoom_step, 1.0 + zoom_step)
            self.__zoom += 1
            if self.__zoom == getint("max_zoom"):
                self.actionZoom_in.setEnabled(False)
            self.actionZoom_out.setEnabled(True)
        elif scale < 0:
            self.__grid.allow_resize = False
            self.graphicsView.scale(1.0 - zoom_step, 1.0 - zoom_step)
            self.__zoom -= 1
            if self.__zoom == - getint("max_zoom"):
                self.actionZoom_out.setEnabled(False)
            self.actionZoom_in.setEnabled(True)
        else:
            self.__zoom = 0
            self.actionZoom_out.setEnabled(True)
            self.actionZoom_in.setEnabled(True)
            self.graphicsView.resetTransform()
            self.__grid.allow_resize = True
            self.grid.resize_tiles(min(self.graphicsView.height(), self.graphicsView.width()))

    def _set_current_duration(self, value):
        self.__grid.set_current_duration(value)
        self.update_frame_controls()

    def _generate_color_gradient(self):
        from simple_dialogs import LinearGradientDialog
        dialog = LinearGradientDialog(self)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.__grid.generate_linear_color_gradient(dialog.get_values())
            self.update_frame_controls()

    def _generate_function(self):
        from simple_dialogs import ColorTransitionDialog
        dialog = ColorTransitionDialog(self)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            ok, err = self.__grid.generate_function(dialog.get_values())
            if not ok:
                self._show_error(str(err))
        self.update_frame_controls()

    def _generate_ticker_font(self):
        from simple_dialogs import TickerTextDialog
        dialog = TickerTextDialog(self)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.__grid.generate_ticker_font(dialog.get_values())
            self.update_frame_controls()

    def _copy_or_cut(self, cut):
        if self.__grid.has_selected_tiles():
            self.__grid.copy_selection(cut)
            self.actionPaste.setEnabled(True)

    def _undo(self):
        self.undoStack.undo()
        if self.undoStack.isClean():
            self.actionUndo.setEnabled(False)
            self.actionUndo.setText(tr("Undo"))

    def _exec_and_add_cmd(self, cmd):
        self.undoStack.push(cmd)
        self.actionUndo.setText(tr("Undo \"%s\"") % cmd.text())
        self.actionUndo.setEnabled(True)

    def _modifier_event(self, typ, event):
        if typ == 0:  # press
            if event.modifiers() == QtCore.Qt.ShiftModifier:
                self.statusBar.showMessage(tr("SHIFT: Left-Click on a tile to record its color"), 3000)
            elif event.modifiers() == QtCore.Qt.ControlModifier:
                self.statusBar.showMessage(tr("CTRL: Left-Click to select multiple tiles"), 3000)
        else:
            self.statusBar.clearMessage()

    def _initialize(self, dimensions, frames=None):
        if frames is None:
            self.filename = None
            self.actionSave.setEnabled(False)
        else:
            self.actionSave.setEnabled(True)
        self.loopCheckbox.setChecked(False)
        self.actionPaste.setEnabled(False)
        self.menuBar.setNativeMenuBar(False)
        self.menuEdit.setVisible(False)  # TODO: Remove after implementing undo
        self.progressBar.setVisible(False)
        self.graphicsView.setCacheMode(QtGui.QGraphicsView.CacheNone)
        self.graphicsView.setBackgroundBrush(QtGui.QColor.fromRgb(*getcolor("background_color")))
        scene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(scene)
        max_size = min(self.graphicsView.minimumWidth(), self.graphicsView.minimumHeight())
        self.__grid = Grid(max_size, scene, Size(*dimensions), frames)
        self.__grid.playback_stopped_event.connect(self._handle_playback_stopped)
        self.__grid.mouse_shift_event.connect(self._handle_mouse_shift_event)
        self.__grid.tile_colored_event.connect(self._handle_tile_colored)
        self.__grid.frame_changed_event.connect(self._handle_frame_changed)
        if not self.__active_connection:
            self.menuConnect_to_device.setEnabled(True)
            self.actionPlayStopDevice.setEnabled(False)
            self.actionDisconnect.setEnabled(False)
        else:
            self.__grid.connection = self.__active_connection
            self.actionDisconnect.setEnabled(True)
        self.undoStack = QtGui.QUndoStack(self)
        self._connect_slots()
        self.colorWidget.setAutoFillBackground(True)
        self.colorWidget.setPalette(QtGui.QColor.fromRgb(*getcolor("pen_color")))
        #self.colorButton.setPalette(QtGui.QColor.fromRgb(255, 255, 255))
        self.update_frame_controls()
        self.graphicsView.resize(self.graphicsView.width(), self.graphicsView.height())
        self.__zoom = 0
        self._zoom(0)
        self.playButton.setDefaultAction(self.actionPlayStop)
        self.playOnDeviceButton.setDefaultAction(self.actionPlayStopDevice)
        self._apply_header_info(EMPTY_HEADER)

    def _fill_info_table(self):
        fields = RO_FIELDS + HEADER_FIELDS
        self.metaInfoTable.setRowCount(len(fields))
        for idx, item in enumerate(fields):
            item1 = QtGui.QTableWidgetItem(item)
            item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            font = QtGui.QFont()
            font.setBold(True)
            item1.setFont(font)
            self.metaInfoTable.setItem(idx, 0, item1)

    def _show_error(self, msg, title=tr("Error")):
        QtGui.QMessageBox.critical(self, title, msg)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    translator.load("translations/blinkgui_%s.qm" % (locale.getlocale()[0]))
    app.installTranslator(translator)
    gui = BlinkGui(sys.argv)
    gui.show()
    sys.exit(app.exec_())