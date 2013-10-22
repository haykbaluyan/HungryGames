# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tournamentresults.ui'
#
# Created: Tue Oct 22 23:15:38 2013
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

class Ui_resultswindow(object):
    def setupUi(self, resultswindow):
        resultswindow.setObjectName(_fromUtf8("resultswindow"))
        resultswindow.resize(1260, 850)
        resultswindow.setMinimumSize(QtCore.QSize(1260, 850))
        resultswindow.setMaximumSize(QtCore.QSize(1260, 850))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resultswindow.setWindowIcon(icon)
        self.body = QtWebKit.QWebView(resultswindow)
        self.body.setGeometry(QtCore.QRect(0, 0, 1261, 851))
        self.body.setUrl(QtCore.QUrl(_fromUtf8("file:///Users/Areg/HungryGames/resultsfiles/table.html")))
        self.body.setObjectName(_fromUtf8("body"))

        self.retranslateUi(resultswindow)
        QtCore.QMetaObject.connectSlotsByName(resultswindow)

    def retranslateUi(self, resultswindow):
        resultswindow.setWindowTitle(_translate("resultswindow", "Tournament Results", None))

from PyQt4 import QtWebKit

