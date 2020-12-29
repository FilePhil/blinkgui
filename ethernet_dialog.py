# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ethernet_dialogOLifdh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EthernetDialog(object):
    def setupUi(self, EthernetDialog):
        if not EthernetDialog.objectName():
            EthernetDialog.setObjectName(u"EthernetDialog")
        EthernetDialog.resize(340, 90)
        EthernetDialog.setMinimumSize(QSize(340, 90))
        EthernetDialog.setMaximumSize(QSize(340, 90))
        self.gridLayout = QGridLayout(EthernetDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(EthernetDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(EthernetDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(EthernetDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.hostnameEdit = QLineEdit(EthernetDialog)
        self.hostnameEdit.setObjectName(u"hostnameEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.hostnameEdit)

        self.portSpin = QSpinBox(EthernetDialog)
        self.portSpin.setObjectName(u"portSpin")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portSpin.sizePolicy().hasHeightForWidth())
        self.portSpin.setSizePolicy(sizePolicy)
        self.portSpin.setMinimum(1000)
        self.portSpin.setMaximum(999999)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.portSpin)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 2)


        self.retranslateUi(EthernetDialog)
        self.buttonBox.accepted.connect(EthernetDialog.accept)
        self.buttonBox.rejected.connect(EthernetDialog.reject)

        QMetaObject.connectSlotsByName(EthernetDialog)
    # setupUi

    def retranslateUi(self, EthernetDialog):
        EthernetDialog.setWindowTitle(QCoreApplication.translate("EthernetDialog", u"Ethernet Connection", None))
        self.label.setText(QCoreApplication.translate("EthernetDialog", u"Host name / IP address:", None))
        self.label_2.setText(QCoreApplication.translate("EthernetDialog", u"Port:", None))
    # retranslateUi

