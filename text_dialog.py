# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_dialogRkHvBd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TickerDialog(object):
    def setupUi(self, TickerDialog):
        if not TickerDialog.objectName():
            TickerDialog.setObjectName(u"TickerDialog")
        TickerDialog.resize(400, 378)
        self.gridLayout = QGridLayout(TickerDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label = QLabel(TickerDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.textEdit = QLineEdit(TickerDialog)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEdit)

        self.label_5 = QLabel(TickerDialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.paddingSpin = QSpinBox(TickerDialog)
        self.paddingSpin.setObjectName(u"paddingSpin")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paddingSpin.sizePolicy().hasHeightForWidth())
        self.paddingSpin.setSizePolicy(sizePolicy)
        self.paddingSpin.setValue(2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.paddingSpin)

        self.label_2 = QLabel(TickerDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fontEdit = QLineEdit(TickerDialog)
        self.fontEdit.setObjectName(u"fontEdit")

        self.horizontalLayout.addWidget(self.fontEdit)

        self.openFontButton = QPushButton(TickerDialog)
        self.openFontButton.setObjectName(u"openFontButton")

        self.horizontalLayout.addWidget(self.openFontButton)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_4 = QLabel(TickerDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.fontsizeSpin = QSpinBox(TickerDialog)
        self.fontsizeSpin.setObjectName(u"fontsizeSpin")
        sizePolicy.setHeightForWidth(self.fontsizeSpin.sizePolicy().hasHeightForWidth())
        self.fontsizeSpin.setSizePolicy(sizePolicy)
        self.fontsizeSpin.setValue(8)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.fontsizeSpin)

        self.label_3 = QLabel(TickerDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_3)

        self.durationSpin = QSpinBox(TickerDialog)
        self.durationSpin.setObjectName(u"durationSpin")
        sizePolicy.setHeightForWidth(self.durationSpin.sizePolicy().hasHeightForWidth())
        self.durationSpin.setSizePolicy(sizePolicy)
        self.durationSpin.setMinimum(1)
        self.durationSpin.setMaximum(999999)
        self.durationSpin.setValue(150)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.durationSpin)

        self.label_6 = QLabel(TickerDialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(TickerDialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_7)

        self.fontColorButton = QPushButton(TickerDialog)
        self.fontColorButton.setObjectName(u"fontColorButton")
        sizePolicy.setHeightForWidth(self.fontColorButton.sizePolicy().hasHeightForWidth())
        self.fontColorButton.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.fontColorButton)

        self.backgroundColorButton = QPushButton(TickerDialog)
        self.backgroundColorButton.setObjectName(u"backgroundColorButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backgroundColorButton.sizePolicy().hasHeightForWidth())
        self.backgroundColorButton.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.backgroundColorButton)

        self.sharpnessLabel = QLabel(TickerDialog)
        self.sharpnessLabel.setObjectName(u"sharpnessLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.sharpnessLabel)

        self.sharpnessSpin = QSpinBox(TickerDialog)
        self.sharpnessSpin.setObjectName(u"sharpnessSpin")
        sizePolicy.setHeightForWidth(self.sharpnessSpin.sizePolicy().hasHeightForWidth())
        self.sharpnessSpin.setSizePolicy(sizePolicy)
        self.sharpnessSpin.setCursor(QCursor(Qt.ArrowCursor))
        self.sharpnessSpin.setMinimum(1)
        self.sharpnessSpin.setMaximum(100)
        self.sharpnessSpin.setSingleStep(10)
        self.sharpnessSpin.setValue(95)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.sharpnessSpin)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(TickerDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.textEdit, self.paddingSpin)
        QWidget.setTabOrder(self.paddingSpin, self.fontEdit)
        QWidget.setTabOrder(self.fontEdit, self.openFontButton)
        QWidget.setTabOrder(self.openFontButton, self.fontsizeSpin)
        QWidget.setTabOrder(self.fontsizeSpin, self.sharpnessSpin)
        QWidget.setTabOrder(self.sharpnessSpin, self.fontColorButton)
        QWidget.setTabOrder(self.fontColorButton, self.backgroundColorButton)
        QWidget.setTabOrder(self.backgroundColorButton, self.durationSpin)

        self.retranslateUi(TickerDialog)
        self.buttonBox.accepted.connect(TickerDialog.accept)
        self.buttonBox.rejected.connect(TickerDialog.reject)

        QMetaObject.connectSlotsByName(TickerDialog)
    # setupUi

    def retranslateUi(self, TickerDialog):
        TickerDialog.setWindowTitle(QCoreApplication.translate("TickerDialog", u"Create ticker font", None))
        self.label.setText(QCoreApplication.translate("TickerDialog", u"Text:", None))
        self.label_5.setText(QCoreApplication.translate("TickerDialog", u"Padding:", None))
        self.label_2.setText(QCoreApplication.translate("TickerDialog", u"Font:", None))
        self.openFontButton.setText(QCoreApplication.translate("TickerDialog", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("TickerDialog", u"Font size:", None))
        self.label_3.setText(QCoreApplication.translate("TickerDialog", u"Frame duration (ms):", None))
        self.label_6.setText(QCoreApplication.translate("TickerDialog", u"Font color:", None))
        self.label_7.setText(QCoreApplication.translate("TickerDialog", u"Background color:", None))
        self.fontColorButton.setText(QCoreApplication.translate("TickerDialog", u"Choose color", None))
        self.backgroundColorButton.setText(QCoreApplication.translate("TickerDialog", u"Choose color", None))
        self.sharpnessLabel.setText(QCoreApplication.translate("TickerDialog", u"Sharpness (%):", None))
    # retranslateUi
