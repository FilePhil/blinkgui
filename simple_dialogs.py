from PySide2 import QtWidgets, QtCore, QtGui
from lg_dialog import Ui_LinearGradientDialog
from color_transition_dialog import Ui_ColorTransitionDialog
from ethernet_dialog import Ui_EthernetDialog
from text_dialog import Ui_TickerDialog
from video_dialog import Ui_VideoDialog
from blinkconfig import *

tr = lambda string: QtCore.QCoreApplication.translate("GUI", string)

LinearGradientDialogResult = namedtuple("colordialogresult",
                                        "duration steps phase_red phase_green phase_blue central_value value_range")
ColorTransitionDialogResult = namedtuple("colortransitionresult",
                                         ["function", "num_frames", "duration", "value", "saturation"])
TickerDialogResult = namedtuple("tickerresult", ["text", "padding", "duration", "font", "font_size", "font_color", "background_color","sharpness"])
EthernetDialogResult = namedtuple("ethernetresult", "host_name port")
VideoDialogResult = namedtuple("videoresult",
                                         ["video_file", "duration"])

class EthernetDialog(QtWidgets.QDialog, Ui_EthernetDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.portSpin.setValue(getint("ethernet_port"))
        self.hostnameEdit.setText(getstring("ethernet_host"))

    def get_values(self):
        res = EthernetDialogResult(self.hostnameEdit.text(), self.portSpin.value())
        return res


class LinearGradientDialog(QtWidgets.QDialog, Ui_LinearGradientDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

    def get_values(self):
        res = LinearGradientDialogResult(self.durationSpin.value(), self.stepsSpin.value(), self.phaseRedSpin.value(),
                                         self.phaseGreenSpin.value(), self.phaseBlueSpin.value(),
                                         self.centralValueSpin.value(), self.valueRangeSpin.value())
        return res


class ColorTransitionDialog(QtWidgets.QDialog, Ui_ColorTransitionDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

    def get_values(self):
        res = ColorTransitionDialogResult(self.frameSpin.value(), self.durationSpin.value(),
                                          self.valueSpin.value(), self.saturationSpin.value(), self.functionEdit.text())
        return res


class TickerTextDialog(QtWidgets.QDialog, Ui_TickerDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.openFontButton.clicked.connect(self.font_button_clicked)
        self.fontColorButton.clicked.connect(self.font_color_button_clicked)
        self.backgroundColorButton.clicked.connect(self.background_color_button_clicked)
        self.fontEdit.setText(getstring("font"))
        self.background_color = getcolor("tile_color")
        self.font_color = getcolor("pen_color")
        self.fontColorButton.setPalette(QtGui.QColor.fromRgb(*self.font_color))
        self.backgroundColorButton.setPalette(QtGui.QColor.fromRgb(*self.background_color))

    def font_button_clicked(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, tr("Open file"), "~", FONT_FILTER)
        if filename[0] == "":
            return
        self.fontEdit.setText(filename[0])

    def font_color_button_clicked(self):
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor.fromRgb(*self.font_color))
        if color.isValid():
            self.font_color = color.getRgb()[:3]
            self.fontColorButton.setPalette(color)

    def background_color_button_clicked(self):
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor.fromRgb(*self.background_color))
        if color.isValid():
            self.background_color = color.getRgb()[:3]
            self.backgroundColorButton.setPalette(color)

    def get_values(self):
        res = TickerDialogResult(self.textEdit.text(), self.paddingSpin.value(), self.durationSpin.value(),
                                 self.fontEdit.text(), self.fontsizeSpin.value(), self.font_color,
                                 self.background_color,self.sharpnessSpin.value())
        return res


class VideoDialog(QtWidgets.QDialog, Ui_VideoDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.openVideoButton.clicked.connect(self.openVideo_button_clicked)


    def openVideo_button_clicked(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, tr("Open Video"), "~", '*.mp4,*.avi')
        if filename[0] == "":
            return
        self.videoFile.setText(filename[0])

    def get_values(self):
        res = VideoDialogResult(self.videoFile.text(),self.durationSpin.value())
        return res
