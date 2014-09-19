from PySide import QtGui
from lg_dialog import Ui_LinearGradientDialog
from color_transition_dialog import Ui_ColorTransitionDialog
from collections import namedtuple
LinearGradientDialogResult = namedtuple("colordialogresult",
                                        "duration steps phase_red phase_green phase_blue central_value value_range")
ColorTransitionDialogResult = namedtuple("colortransitionresult",
                                         "function num_frames duration value saturation")


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



