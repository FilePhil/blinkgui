# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lg_dialogYvEhZH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LinearGradientDialog(object):
    def setupUi(self, LinearGradientDialog):
        if not LinearGradientDialog.objectName():
            LinearGradientDialog.setObjectName(u"LinearGradientDialog")
        LinearGradientDialog.resize(275, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LinearGradientDialog.sizePolicy().hasHeightForWidth())
        LinearGradientDialog.setSizePolicy(sizePolicy)
        LinearGradientDialog.setMinimumSize(QSize(275, 200))
        LinearGradientDialog.setMaximumSize(QSize(275, 200))
        self.verticalLayout = QVBoxLayout(LinearGradientDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label = QLabel(LinearGradientDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.stepsSpin = QSpinBox(LinearGradientDialog)
        self.stepsSpin.setObjectName(u"stepsSpin")
        self.stepsSpin.setMaximum(100000)
        self.stepsSpin.setValue(1000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.stepsSpin)

        self.label_2 = QLabel(LinearGradientDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(LinearGradientDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(LinearGradientDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.phaseRedSpin = QDoubleSpinBox(LinearGradientDialog)
        self.phaseRedSpin.setObjectName(u"phaseRedSpin")
        self.phaseRedSpin.setValue(2.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.phaseRedSpin)

        self.phaseGreenSpin = QDoubleSpinBox(LinearGradientDialog)
        self.phaseGreenSpin.setObjectName(u"phaseGreenSpin")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.phaseGreenSpin)

        self.phaseBlueSpin = QDoubleSpinBox(LinearGradientDialog)
        self.phaseBlueSpin.setObjectName(u"phaseBlueSpin")
        self.phaseBlueSpin.setValue(4.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.phaseBlueSpin)

        self.label_5 = QLabel(LinearGradientDialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(LinearGradientDialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.centralValueSpin = QSpinBox(LinearGradientDialog)
        self.centralValueSpin.setObjectName(u"centralValueSpin")
        self.centralValueSpin.setMaximum(255)
        self.centralValueSpin.setValue(128)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.centralValueSpin)

        self.valueRangeSpin = QSpinBox(LinearGradientDialog)
        self.valueRangeSpin.setObjectName(u"valueRangeSpin")
        self.valueRangeSpin.setMaximum(255)
        self.valueRangeSpin.setValue(127)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.valueRangeSpin)

        self.durationSpin = QSpinBox(LinearGradientDialog)
        self.durationSpin.setObjectName(u"durationSpin")
        self.durationSpin.setMaximum(100000)
        self.durationSpin.setValue(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.durationSpin)

        self.label_7 = QLabel(LinearGradientDialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(LinearGradientDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.durationSpin, self.stepsSpin)
        QWidget.setTabOrder(self.stepsSpin, self.phaseRedSpin)
        QWidget.setTabOrder(self.phaseRedSpin, self.phaseGreenSpin)
        QWidget.setTabOrder(self.phaseGreenSpin, self.phaseBlueSpin)
        QWidget.setTabOrder(self.phaseBlueSpin, self.centralValueSpin)
        QWidget.setTabOrder(self.centralValueSpin, self.valueRangeSpin)
        QWidget.setTabOrder(self.valueRangeSpin, self.buttonBox)

        self.retranslateUi(LinearGradientDialog)
        self.buttonBox.accepted.connect(LinearGradientDialog.accept)
        self.buttonBox.rejected.connect(LinearGradientDialog.reject)

        QMetaObject.connectSlotsByName(LinearGradientDialog)
    # setupUi

    def retranslateUi(self, LinearGradientDialog):
        LinearGradientDialog.setWindowTitle(QCoreApplication.translate("LinearGradientDialog", u"Linear color gradient", None))
        self.label.setText(QCoreApplication.translate("LinearGradientDialog", u"Number of steps:", None))
        self.label_2.setText(QCoreApplication.translate("LinearGradientDialog", u"Phase Red:", None))
        self.label_3.setText(QCoreApplication.translate("LinearGradientDialog", u"Phase Green:", None))
        self.label_4.setText(QCoreApplication.translate("LinearGradientDialog", u"Phase Blue:", None))
        self.label_5.setText(QCoreApplication.translate("LinearGradientDialog", u"Central value:", None))
        self.label_6.setText(QCoreApplication.translate("LinearGradientDialog", u"Value range:", None))
        self.label_7.setText(QCoreApplication.translate("LinearGradientDialog", u"Frame Duration (ms):", None))
    # retranslateUi

