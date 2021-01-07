# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_dialogfmFqaW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VideoDialog(object):
    def setupUi(self, VideoDialog):
        if not VideoDialog.objectName():
            VideoDialog.setObjectName(u"VideoDialog")
        VideoDialog.resize(400, 166)
        self.gridLayout = QGridLayout(VideoDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label_2 = QLabel(VideoDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.videoFile = QLineEdit(VideoDialog)
        self.videoFile.setObjectName(u"videoFile")

        self.horizontalLayout.addWidget(self.videoFile)

        self.openVideoButton = QPushButton(VideoDialog)
        self.openVideoButton.setObjectName(u"openVideoButton")

        self.horizontalLayout.addWidget(self.openVideoButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.sharpnessLabel = QLabel(VideoDialog)
        self.sharpnessLabel.setObjectName(u"sharpnessLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sharpnessLabel)

        self.sharpnessSpin = QSpinBox(VideoDialog)
        self.sharpnessSpin.setObjectName(u"sharpnessSpin")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sharpnessSpin.sizePolicy().hasHeightForWidth())
        self.sharpnessSpin.setSizePolicy(sizePolicy)
        self.sharpnessSpin.setCursor(QCursor(Qt.ArrowCursor))
        self.sharpnessSpin.setMinimum(1)
        self.sharpnessSpin.setMaximum(100)
        self.sharpnessSpin.setSingleStep(10)
        self.sharpnessSpin.setValue(95)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sharpnessSpin)

        self.label_3 = QLabel(VideoDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.durationSpin = QSpinBox(VideoDialog)
        self.durationSpin.setObjectName(u"durationSpin")
        sizePolicy.setHeightForWidth(self.durationSpin.sizePolicy().hasHeightForWidth())
        self.durationSpin.setSizePolicy(sizePolicy)
        self.durationSpin.setMinimum(1)
        self.durationSpin.setMaximum(999999)
        self.durationSpin.setValue(42)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.durationSpin)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(VideoDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.videoFile, self.openVideoButton)
        QWidget.setTabOrder(self.openVideoButton, self.sharpnessSpin)
        QWidget.setTabOrder(self.sharpnessSpin, self.durationSpin)

        self.retranslateUi(VideoDialog)
        self.buttonBox.accepted.connect(VideoDialog.accept)
        self.buttonBox.rejected.connect(VideoDialog.reject)

        QMetaObject.connectSlotsByName(VideoDialog)
    # setupUi

    def retranslateUi(self, VideoDialog):
        VideoDialog.setWindowTitle(QCoreApplication.translate("VideoDialog", u"Convert Video", None))
        self.label_2.setText(QCoreApplication.translate("VideoDialog", u"Video:", None))
        self.openVideoButton.setText(QCoreApplication.translate("VideoDialog", u"Browse", None))
        self.sharpnessLabel.setText(QCoreApplication.translate("VideoDialog", u"Sharpness (%):", None))
        self.label_3.setText(QCoreApplication.translate("VideoDialog", u"Frame duration (ms):", None))
    # retranslateUi

