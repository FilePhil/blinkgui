from PySide import QtGui, QtCore
from lg_dialog import Ui_LinearGradientDialog
from color_transition_dialog import Ui_ColorTransitionDialog
from text_dialog import Ui_TickerDialog
from blinkconfig import *

tr = lambda string: QtCore.QCoreApplication.translate("GUI", string)

LinearGradientDialogResult = namedtuple("colordialogresult",
                                        "duration steps phase_red phase_green phase_blue central_value value_range")
ColorTransitionDialogResult = namedtuple("colortransitionresult",
                                         "function num_frames duration value saturation")
TickerDialogResult = namedtuple("tickerresult", "text padding duration font font_size font_color background_color")


class LinearGradientDialog(QtGui.QDialog, Ui_LinearGradientDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

    def get_values(self):
        res = LinearGradientDialogResult(self.durationSpin.value(), self.stepsSpin.value(), self.phaseRedSpin.value(),
                                         self.phaseGreenSpin.value(), self.phaseBlueSpin.value(), self.centralValueSpin.value(),
                                         self.valueRangeSpin.value())
        return res


class ColorTransitionDialog(QtGui.QDialog, Ui_ColorTransitionDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

    def get_values(self):
        res = ColorTransitionDialogResult(self.frameSpin.value(), self.durationSpin.value(),
                                          self.valueSpin.value(), self.saturationSpin.value(), self.functionEdit.text())
        return res


class TickerTextDialog(QtGui.QDialog, Ui_TickerDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.openFontButton.clicked.connect(self.font_button_clicked)
        self.fontColorButton.clicked.connect(self.font_color_button_clicked)
        self.backgroundColorButton.clicked.connect(self.background_color_button_clicked)
        self.fontEdit.setText(config.getstring("font"))
        self.background_color = config.getcolor("tile_color")
        self.font_color = config.getcolor("pen_color")
        self.fontColorButton.setPalette(QtGui.QColor.fromRgb(*self.font_color))
        self.backgroundColorButton.setPalette(QtGui.QColor.fromRgb(*self.background_color))

    def font_button_clicked(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, tr("Open file"), "~", config.FONT_FILTER)
        if filename[0] == "":
            return
        self.fontEdit.setText(filename[0])

    def font_color_button_clicked(self):
        color = QtGui.QColorDialog.getColor(QtGui.QColor.fromRgb(*self.font_color))
        if color.isValid():
            self.font_color = color.getRgb()[:3]
            self.fontColorButton.setPalette(color)

    def background_color_button_clicked(self):
        color = QtGui.QColorDialog.getColor(QtGui.QColor.fromRgb(*self.background_color))
        if color.isValid():
            self.background_color = color.getRgb()[:3]
            self.backgroundColorButton.setPalette(color)

    def get_values(self):
        res = TickerDialogResult(self.textEdit.text(), self.paddingSpin.value(), self.durationSpin.value(),
                                 self.fontEdit.text(), self.fontsizeSpin.value(), self.font_color,
                                 self.background_color)
        return res



