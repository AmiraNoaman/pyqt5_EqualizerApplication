# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1322, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_10.setObjectName("frame_10")
        self.inverse = QtWidgets.QPushButton(self.frame_10)
        self.inverse.setGeometry(QtCore.QRect(10, 30, 91, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inverse.sizePolicy().hasHeightForWidth())
        self.inverse.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inverse.setFont(font)
        self.inverse.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inverse.setStyleSheet("background-color: rgb(0, 0, 122);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.inverse.setObjectName("inverse")
        self.gridLayout_6.addWidget(self.frame_10, 6, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout.setObjectName("gridLayout")
        self.stopInput = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopInput.sizePolicy().hasHeightForWidth())
        self.stopInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stopInput.setFont(font)
        self.stopInput.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.stopInput.setObjectName("stopInput")
        self.gridLayout.addWidget(self.stopInput, 2, 0, 1, 1)
        self.playInput = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playInput.sizePolicy().hasHeightForWidth())
        self.playInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playInput.setFont(font)
        self.playInput.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.playInput.setObjectName("playInput")
        self.gridLayout.addWidget(self.playInput, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_7, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.frame_2.setFont(font)
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.title = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setStyleSheet("\n"
"background-color: rgb(99, 99, 99);\n"
"color: rgb(6, 6, 6);\n"
"background-color: rgb(182, 182, 182);\n"
"")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout_3.addWidget(self.title, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 1, 1, 3)
        self.GVOriginal = PlotWidget(self.frame)
        self.GVOriginal.setObjectName("GVOriginal")
        self.gridLayout_6.addWidget(self.GVOriginal, 2, 1, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Rect = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Rect.sizePolicy().hasHeightForWidth())
        self.Rect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Rect.setFont(font)
        self.Rect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Rect.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.Rect.setObjectName("Rect")
        self.gridLayout_5.addWidget(self.Rect, 7, 0, 1, 1)
        self.hanningbutton = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hanningbutton.sizePolicy().hasHeightForWidth())
        self.hanningbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hanningbutton.setFont(font)
        self.hanningbutton.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.hanningbutton.setObjectName("hanningbutton")
        self.gridLayout_5.addWidget(self.hanningbutton, 2, 0, 1, 1)
        self.hammingbutton = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hammingbutton.sizePolicy().hasHeightForWidth())
        self.hammingbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hammingbutton.setFont(font)
        self.hammingbutton.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.hammingbutton.setObjectName("hammingbutton")
        self.gridLayout_5.addWidget(self.hammingbutton, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_8, 5, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.l2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l2.setObjectName("l2")
        self.gridLayout_2.addWidget(self.l2, 0, 3, 1, 1)
        self.slider7 = QtWidgets.QSlider(self.frame)
        self.slider7.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider7.setMinimum(-10)
        self.slider7.setMaximum(10)
        self.slider7.setOrientation(QtCore.Qt.Vertical)
        self.slider7.setObjectName("slider7")
        self.gridLayout_2.addWidget(self.slider7, 0, 14, 1, 1)
        self.slider6 = QtWidgets.QSlider(self.frame)
        self.slider6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider6.setMinimum(-10)
        self.slider6.setMaximum(10)
        self.slider6.setOrientation(QtCore.Qt.Vertical)
        self.slider6.setObjectName("slider6")
        self.gridLayout_2.addWidget(self.slider6, 0, 12, 1, 1)
        self.slider9 = QtWidgets.QSlider(self.frame)
        self.slider9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider9.setMinimum(-10)
        self.slider9.setMaximum(10)
        self.slider9.setOrientation(QtCore.Qt.Vertical)
        self.slider9.setObjectName("slider9")
        self.gridLayout_2.addWidget(self.slider9, 0, 18, 1, 1)
        self.slider5 = QtWidgets.QSlider(self.frame)
        self.slider5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider5.setMinimum(-10)
        self.slider5.setMaximum(10)
        self.slider5.setOrientation(QtCore.Qt.Vertical)
        self.slider5.setObjectName("slider5")
        self.gridLayout_2.addWidget(self.slider5, 0, 10, 1, 1)
        self.l7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l7.setFont(font)
        self.l7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l7.setObjectName("l7")
        self.gridLayout_2.addWidget(self.l7, 0, 13, 1, 1)
        self.l4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l4.setObjectName("l4")
        self.gridLayout_2.addWidget(self.l4, 0, 7, 1, 1)
        self.slider4 = QtWidgets.QSlider(self.frame)
        self.slider4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider4.setMinimum(-10)
        self.slider4.setMaximum(10)
        self.slider4.setOrientation(QtCore.Qt.Vertical)
        self.slider4.setObjectName("slider4")
        self.gridLayout_2.addWidget(self.slider4, 0, 8, 1, 1)
        self.l3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l3.setObjectName("l3")
        self.gridLayout_2.addWidget(self.l3, 0, 5, 1, 1)
        self.l6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l6.setFont(font)
        self.l6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l6.setObjectName("l6")
        self.gridLayout_2.addWidget(self.l6, 0, 11, 1, 1)
        self.slider8 = QtWidgets.QSlider(self.frame)
        self.slider8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider8.setMinimum(-10)
        self.slider8.setMaximum(10)
        self.slider8.setOrientation(QtCore.Qt.Vertical)
        self.slider8.setObjectName("slider8")
        self.gridLayout_2.addWidget(self.slider8, 0, 16, 1, 1)
        self.l1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAcceptDrops(False)
        self.l1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.l1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l1.setObjectName("l1")
        self.gridLayout_2.addWidget(self.l1, 0, 1, 1, 1)
        self.slider1 = QtWidgets.QSlider(self.frame)
        self.slider1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider1.setMinimum(-10)
        self.slider1.setMaximum(10)
        self.slider1.setOrientation(QtCore.Qt.Vertical)
        self.slider1.setObjectName("slider1")
        self.gridLayout_2.addWidget(self.slider1, 0, 2, 1, 1)
        self.l9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l9.setFont(font)
        self.l9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l9.setObjectName("l9")
        self.gridLayout_2.addWidget(self.l9, 0, 17, 1, 1)
        self.l8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l8.setFont(font)
        self.l8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l8.setObjectName("l8")
        self.gridLayout_2.addWidget(self.l8, 0, 15, 1, 1)
        self.slider2 = QtWidgets.QSlider(self.frame)
        self.slider2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider2.setMinimum(-10)
        self.slider2.setMaximum(10)
        self.slider2.setOrientation(QtCore.Qt.Vertical)
        self.slider2.setObjectName("slider2")
        self.gridLayout_2.addWidget(self.slider2, 0, 4, 1, 1)
        self.l5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.l5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l5.setObjectName("l5")
        self.gridLayout_2.addWidget(self.l5, 0, 9, 1, 1)
        self.slider0 = QtWidgets.QSlider(self.frame)
        self.slider0.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"background-color: rgb(0, 0, 0);")
        self.slider0.setMinimum(-10)
        self.slider0.setMaximum(10)
        self.slider0.setOrientation(QtCore.Qt.Vertical)
        self.slider0.setObjectName("slider0")
        self.gridLayout_2.addWidget(self.slider0, 0, 0, 1, 1)
        self.l10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l10.setFont(font)
        self.l10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l10.setObjectName("l10")
        self.gridLayout_2.addWidget(self.l10, 0, 19, 1, 1)
        self.slider3 = QtWidgets.QSlider(self.frame)
        self.slider3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slider3.setMinimum(-10)
        self.slider3.setMaximum(10)
        self.slider3.setOrientation(QtCore.Qt.Vertical)
        self.slider3.setObjectName("slider3")
        self.gridLayout_2.addWidget(self.slider3, 0, 6, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 6, 1, 1, 2)
        self.GVFourier = PlotWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GVFourier.sizePolicy().hasHeightForWidth())
        self.GVFourier.setSizePolicy(sizePolicy)
        self.GVFourier.setObjectName("GVFourier")
        self.gridLayout_6.addWidget(self.GVFourier, 2, 2, 1, 2)
        self.GVwindow = PlotWidget(self.frame)
        self.GVwindow.setObjectName("GVwindow")
        self.gridLayout_6.addWidget(self.GVwindow, 5, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 3, 3, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_12.setObjectName("frame_12")
        self.exit = QtWidgets.QPushButton(self.frame_12)
        self.exit.setGeometry(QtCore.QRect(120, 60, 351, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exit.setStyleSheet("background-color: rgb(0, 0, 122);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.exit.setObjectName("exit")
        self.gridLayout_6.addWidget(self.frame_12, 6, 3, 1, 1)
        self.upload = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.upload.setFont(font)
        self.upload.setStyleSheet("background-color: rgb(0, 0, 122);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.upload.setObjectName("upload")
        self.gridLayout_6.addWidget(self.upload, 0, 0, 2, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.slider0.valueChanged['int'].connect(self.l1.setNum)
        self.slider2.valueChanged['int'].connect(self.l3.setNum)
        self.slider7.valueChanged['int'].connect(self.l8.setNum)
        self.slider3.valueChanged['int'].connect(self.l4.setNum)
        self.slider1.valueChanged['int'].connect(self.l2.setNum)
        self.slider0.valueChanged['int'].connect(self.l1.setNum)
        self.slider8.valueChanged['int'].connect(self.l9.setNum)
        self.slider5.valueChanged['int'].connect(self.l6.setNum)
        self.slider1.valueChanged['int'].connect(self.l2.setNum)
        self.slider6.valueChanged['int'].connect(self.l7.setNum)
        self.slider4.valueChanged['int'].connect(self.l5.setNum)
        self.slider9.valueChanged['int'].connect(self.l10.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.slider6, self.slider3)
        MainWindow.setTabOrder(self.slider3, self.slider9)
        MainWindow.setTabOrder(self.slider9, self.slider7)
        MainWindow.setTabOrder(self.slider7, self.slider1)
        MainWindow.setTabOrder(self.slider1, self.slider4)
        MainWindow.setTabOrder(self.slider4, self.slider8)
        MainWindow.setTabOrder(self.slider8, self.slider2)
        MainWindow.setTabOrder(self.slider2, self.slider5)
        MainWindow.setTabOrder(self.slider5, self.slider0)
        MainWindow.setTabOrder(self.slider0, self.GVOriginal)
        MainWindow.setTabOrder(self.GVOriginal, self.stopInput)
        MainWindow.setTabOrder(self.stopInput, self.inverse)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inverse.setText(_translate("MainWindow", "Show Output"))
        self.stopInput.setText(_translate("MainWindow", "Stop "))
        self.playInput.setText(_translate("MainWindow", "Play "))
        self.title.setText(_translate("MainWindow", "GEQ GRAPHIC EQUALIZER"))
        self.Rect.setText(_translate("MainWindow", "Rectangular"))
        self.hanningbutton.setText(_translate("MainWindow", "Hanning"))
        self.hammingbutton.setText(_translate("MainWindow", "Hamming"))
        self.l2.setText(_translate("MainWindow", "1"))
        self.l7.setText(_translate("MainWindow", "1"))
        self.l4.setText(_translate("MainWindow", "1"))
        self.l3.setText(_translate("MainWindow", "1"))
        self.l6.setText(_translate("MainWindow", "1"))
        self.l1.setText(_translate("MainWindow", "1"))
        self.l9.setText(_translate("MainWindow", "1"))
        self.l8.setText(_translate("MainWindow", "1"))
        self.l5.setText(_translate("MainWindow", "1"))
        self.l10.setText(_translate("MainWindow", "1"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.upload.setText(_translate("MainWindow", "Upload"))
from pyqtgraph import PlotWidget
