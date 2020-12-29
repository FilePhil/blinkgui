# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_transition_dialogcdFqRn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ColorTransitionDialog(object):
    def setupUi(self, ColorTransitionDialog):
        if not ColorTransitionDialog.objectName():
            ColorTransitionDialog.setObjectName(u"ColorTransitionDialog")
        ColorTransitionDialog.resize(350, 177)
        ColorTransitionDialog.setMinimumSize(QSize(350, 177))
        ColorTransitionDialog.setMaximumSize(QSize(350, 177))
        self.gridLayout = QGridLayout(ColorTransitionDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label = QLabel(ColorTransitionDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.frameSpin = QSpinBox(ColorTransitionDialog)
        self.frameSpin.setObjectName(u"frameSpin")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpin.sizePolicy().hasHeightForWidth())
        self.frameSpin.setSizePolicy(sizePolicy)
        self.frameSpin.setMaximum(10000000)
        self.frameSpin.setValue(1000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frameSpin)

        self.label_2 = QLabel(ColorTransitionDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.durationSpin = QSpinBox(ColorTransitionDialog)
        self.durationSpin.setObjectName(u"durationSpin")
        sizePolicy.setHeightForWidth(self.durationSpin.sizePolicy().hasHeightForWidth())
        self.durationSpin.setSizePolicy(sizePolicy)
        self.durationSpin.setMaximum(10000000)
        self.durationSpin.setValue(10)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.durationSpin)

        self.label_4 = QLabel(ColorTransitionDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.valueSpin = QDoubleSpinBox(ColorTransitionDialog)
        self.valueSpin.setObjectName(u"valueSpin")
        sizePolicy.setHeightForWidth(self.valueSpin.sizePolicy().hasHeightForWidth())
        self.valueSpin.setSizePolicy(sizePolicy)
        self.valueSpin.setMaximum(1.000000000000000)
        self.valueSpin.setSingleStep(0.001000000000000)
        self.valueSpin.setValue(0.500000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.valueSpin)

        self.label_5 = QLabel(ColorTransitionDialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.saturationSpin = QDoubleSpinBox(ColorTransitionDialog)
        self.saturationSpin.setObjectName(u"saturationSpin")
        sizePolicy.setHeightForWidth(self.saturationSpin.sizePolicy().hasHeightForWidth())
        self.saturationSpin.setSizePolicy(sizePolicy)
        self.saturationSpin.setMaximum(1.000000000000000)
        self.saturationSpin.setSingleStep(0.001000000000000)
        self.saturationSpin.setValue(1.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.saturationSpin)

        self.label_3 = QLabel(ColorTransitionDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.functionEdit = QLineEdit(ColorTransitionDialog)
        self.functionEdit.setObjectName(u"functionEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.functionEdit)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ColorTransitionDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ColorTransitionDialog)
        self.buttonBox.accepted.connect(ColorTransitionDialog.accept)
        self.buttonBox.rejected.connect(ColorTransitionDialog.reject)

        QMetaObject.connectSlotsByName(ColorTransitionDialog)
    # setupUi

    def retranslateUi(self, ColorTransitionDialog):
        ColorTransitionDialog.setWindowTitle(QCoreApplication.translate("ColorTransitionDialog", u"Color transition", None))
        self.label.setText(QCoreApplication.translate("ColorTransitionDialog", u"Number of frames:", None))
        self.label_2.setText(QCoreApplication.translate("ColorTransitionDialog", u"Frame duration (ms):", None))
        self.label_4.setText(QCoreApplication.translate("ColorTransitionDialog", u"Value (brightness):", None))
        self.label_5.setText(QCoreApplication.translate("ColorTransitionDialog", u"Saturation:", None))
        self.label_3.setText(QCoreApplication.translate("ColorTransitionDialog", u"Function(x,y,f) to evaluate:", None))
        self.functionEdit.setText(QCoreApplication.translate("ColorTransitionDialog", u"sin(x)+cos(y) + 0.001*f", None))
    # retranslateUi

