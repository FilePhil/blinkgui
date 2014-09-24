# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color_transition_dialog.ui'
#
# Created: Wed Sep 24 15:20:47 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ColorTransitionDialog(object):
    def setupUi(self, ColorTransitionDialog):
        ColorTransitionDialog.setObjectName("ColorTransitionDialog")
        ColorTransitionDialog.resize(350, 177)
        ColorTransitionDialog.setMinimumSize(QtCore.QSize(350, 177))
        ColorTransitionDialog.setMaximumSize(QtCore.QSize(350, 177))
        self.gridLayout = QtGui.QGridLayout(ColorTransitionDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(ColorTransitionDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.frameSpin = QtGui.QSpinBox(ColorTransitionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpin.sizePolicy().hasHeightForWidth())
        self.frameSpin.setSizePolicy(sizePolicy)
        self.frameSpin.setMaximum(10000000)
        self.frameSpin.setProperty("value", 1000)
        self.frameSpin.setObjectName("frameSpin")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.frameSpin)
        self.label_2 = QtGui.QLabel(ColorTransitionDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.durationSpin = QtGui.QSpinBox(ColorTransitionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durationSpin.sizePolicy().hasHeightForWidth())
        self.durationSpin.setSizePolicy(sizePolicy)
        self.durationSpin.setMaximum(10000000)
        self.durationSpin.setProperty("value", 10)
        self.durationSpin.setObjectName("durationSpin")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.durationSpin)
        self.label_4 = QtGui.QLabel(ColorTransitionDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.valueSpin = QtGui.QDoubleSpinBox(ColorTransitionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueSpin.sizePolicy().hasHeightForWidth())
        self.valueSpin.setSizePolicy(sizePolicy)
        self.valueSpin.setMaximum(1.0)
        self.valueSpin.setSingleStep(0.001)
        self.valueSpin.setProperty("value", 0.5)
        self.valueSpin.setObjectName("valueSpin")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.valueSpin)
        self.label_5 = QtGui.QLabel(ColorTransitionDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.saturationSpin = QtGui.QDoubleSpinBox(ColorTransitionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saturationSpin.sizePolicy().hasHeightForWidth())
        self.saturationSpin.setSizePolicy(sizePolicy)
        self.saturationSpin.setMaximum(1.0)
        self.saturationSpin.setSingleStep(0.001)
        self.saturationSpin.setProperty("value", 1.0)
        self.saturationSpin.setObjectName("saturationSpin")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.saturationSpin)
        self.label_3 = QtGui.QLabel(ColorTransitionDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.functionEdit = QtGui.QLineEdit(ColorTransitionDialog)
        self.functionEdit.setObjectName("functionEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.functionEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ColorTransitionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ColorTransitionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ColorTransitionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ColorTransitionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ColorTransitionDialog)

    def retranslateUi(self, ColorTransitionDialog):
        ColorTransitionDialog.setWindowTitle(QtGui.QApplication.translate("ColorTransitionDialog", "Color transition", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ColorTransitionDialog", "Number of frames:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ColorTransitionDialog", "Frame duration (ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ColorTransitionDialog", "Value (brightness):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ColorTransitionDialog", "Saturation:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ColorTransitionDialog", "Function(x,y,f) to evaluate:", None, QtGui.QApplication.UnicodeUTF8))
        self.functionEdit.setText(QtGui.QApplication.translate("ColorTransitionDialog", "sin(x)+cos(y) + 0.001*f", None, QtGui.QApplication.UnicodeUTF8))

