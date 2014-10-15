# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ethernet_dialog.ui'
#
# Created: Wed Oct 15 10:48:03 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EthernetDialog(object):
    def setupUi(self, EthernetDialog):
        EthernetDialog.setObjectName("EthernetDialog")
        EthernetDialog.resize(340, 90)
        EthernetDialog.setMinimumSize(QtCore.QSize(340, 90))
        EthernetDialog.setMaximumSize(QtCore.QSize(340, 90))
        self.gridLayout = QtGui.QGridLayout(EthernetDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(EthernetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(EthernetDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(EthernetDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.hostnameEdit = QtGui.QLineEdit(EthernetDialog)
        self.hostnameEdit.setObjectName("hostnameEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.hostnameEdit)
        self.portSpin = QtGui.QSpinBox(EthernetDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portSpin.sizePolicy().hasHeightForWidth())
        self.portSpin.setSizePolicy(sizePolicy)
        self.portSpin.setMinimum(1000)
        self.portSpin.setMaximum(999999)
        self.portSpin.setObjectName("portSpin")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.portSpin)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 2)

        self.retranslateUi(EthernetDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), EthernetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), EthernetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EthernetDialog)

    def retranslateUi(self, EthernetDialog):
        EthernetDialog.setWindowTitle(QtGui.QApplication.translate("EthernetDialog", "Ethernet Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EthernetDialog", "Host name / IP address:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EthernetDialog", "Port:", None, QtGui.QApplication.UnicodeUTF8))

