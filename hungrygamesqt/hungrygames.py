# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hungrygames.ui'
#
# Created: Fri Oct 04 18:50:20 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HungryGames(object):
    def setupUi(self, HungryGames):
        HungryGames.setObjectName(_fromUtf8("HungryGames"))
        HungryGames.resize(777, 600)
        self.centralwidget = QtGui.QWidget(HungryGames)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 400, 321, 121))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 751, 251))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Game1 = QtGui.QTableView(self.groupBox)
        self.Game1.setGeometry(QtCore.QRect(30, 30, 171, 161))
        self.Game1.setObjectName(_fromUtf8("Game1"))
        self.Game2 = QtGui.QTableView(self.groupBox)
        self.Game2.setGeometry(QtCore.QRect(300, 30, 171, 161))
        self.Game2.setObjectName(_fromUtf8("Game2"))
        self.Game3 = QtGui.QTableView(self.groupBox)
        self.Game3.setGeometry(QtCore.QRect(550, 30, 171, 161))
        self.Game3.setObjectName(_fromUtf8("Game3"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(60, 210, 111, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(360, 210, 61, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(600, 210, 82, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 300, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 340, 241, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 300, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(500, 290, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        HungryGames.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(HungryGames)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        HungryGames.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(HungryGames)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        HungryGames.setStatusBar(self.statusbar)

        self.retranslateUi(HungryGames)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_2.setNum)
        QtCore.QMetaObject.connectSlotsByName(HungryGames)

    def retranslateUi(self, HungryGames):
        HungryGames.setWindowTitle(_translate("HungryGames", "MainWindow", None))
        self.groupBox.setTitle(_translate("HungryGames", "GroupBox", None))
        self.radioButton.setText(_translate("HungryGames", "Prisoner\'s Dilemma", None))
        self.radioButton_2.setText(_translate("HungryGames", "Chicken", None))
        self.radioButton_3.setText(_translate("HungryGames", "Stag Hunt", None))
        self.label.setText(_translate("HungryGames", "Number of rounds:", None))
        self.label_2.setText(_translate("HungryGames", "0", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("HungryGames", "lkdksd", None))
        item = self.listWidget.item(1)
        item.setText(_translate("HungryGames", "s;ldfjkopsfs", None))
        item = self.listWidget.item(2)
        item.setText(_translate("HungryGames", "lskdfjosifsfs", None))
        item = self.listWidget.item(3)
        item.setText(_translate("HungryGames", "osldjfoisfs", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)



