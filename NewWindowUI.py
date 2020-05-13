# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 503)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 591, 483))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.graphicsViewOP1 = PlotWidget(self.widget)
        self.graphicsViewOP1.setObjectName("graphicsViewOP1")
        self.gridLayout.addWidget(self.graphicsViewOP1, 1, 0, 1, 3)
        self.graphicsViewOP2 = PlotWidget(self.widget)
        self.graphicsViewOP2.setObjectName("graphicsViewOP2")
        self.gridLayout.addWidget(self.graphicsViewOP2, 2, 0, 1, 3)
        self.playOutput = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playOutput.setFont(font)
        self.playOutput.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.playOutput.setIconSize(QtCore.QSize(17, 17))
        self.playOutput.setObjectName("playOutput")
        self.gridLayout.addWidget(self.playOutput, 3, 0, 1, 1)
        self.saveOutput = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveOutput.setFont(font)
        self.saveOutput.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.saveOutput.setObjectName("saveOutput")
        self.gridLayout.addWidget(self.saveOutput, 3, 1, 1, 1)
        self.stopOutput = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stopOutput.setFont(font)
        self.stopOutput.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.stopOutput.setObjectName("stopOutput")
        self.gridLayout.addWidget(self.stopOutput, 3, 2, 2, 1)
        self.playOutput2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playOutput2.setFont(font)
        self.playOutput2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.playOutput2.setIconSize(QtCore.QSize(17, 17))
        self.playOutput2.setObjectName("playOutput2")
        self.gridLayout.addWidget(self.playOutput2, 4, 0, 1, 1)
        self.saveOutput2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveOutput2.setFont(font)
        self.saveOutput2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.saveOutput2.setObjectName("saveOutput2")
        self.gridLayout.addWidget(self.saveOutput2, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Difference Between Output & Original Signal"))
        self.playOutput.setText(_translate("Form", "Play"))
        self.saveOutput.setText(_translate("Form", "Save"))
        self.stopOutput.setText(_translate("Form", "Stop"))
        self.playOutput2.setText(_translate("Form", "Play 2"))
        self.saveOutput2.setText(_translate("Form", "Save 2"))
from pyqtgraph import PlotWidget
