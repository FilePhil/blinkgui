# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_dialog.ui'
#
# Created: Sat Sep 20 15:22:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TickerDialog(object):
    def setupUi(self, TickerDialog):
        TickerDialog.setObjectName("TickerDialog")
        TickerDialog.resize(400, 143)
        self.gridLayout = QtGui.QGridLayout(TickerDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(TickerDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.textEdit = QtGui.QLineEdit(TickerDialog)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.textEdit)
        self.fontComboBox = QtGui.QFontComboBox(TickerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setFontFilters(QtGui.QFontComboBox.ScalableFonts)
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.fontComboBox)
        self.label_2 = QtGui.QLabel(TickerDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.durationSpin = QtGui.QSpinBox(TickerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durationSpin.sizePolicy().hasHeightForWidth())
        self.durationSpin.setSizePolicy(sizePolicy)
        self.durationSpin.setMinimum(1)
        self.durationSpin.setMaximum(999999)
        self.durationSpin.setProperty("value", 2000)
        self.durationSpin.setObjectName("durationSpin")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.durationSpin)
        self.label_3 = QtGui.QLabel(TickerDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.fontsizeSpin = QtGui.QSpinBox(TickerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontsizeSpin.sizePolicy().hasHeightForWidth())
        self.fontsizeSpin.setSizePolicy(sizePolicy)
        self.fontsizeSpin.setProperty("value", 8)
        self.fontsizeSpin.setObjectName("fontsizeSpin")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.fontsizeSpin)
        self.label_4 = QtGui.QLabel(TickerDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TickerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(TickerDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TickerDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TickerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TickerDialog)

    def retranslateUi(self, TickerDialog):
        TickerDialog.setWindowTitle(QtGui.QApplication.translate("TickerDialog", "Create ticker font", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TickerDialog", "Text:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TickerDialog", "Font:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TickerDialog", "Duration (ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TickerDialog", "Font size:", None, QtGui.QApplication.UnicodeUTF8))

