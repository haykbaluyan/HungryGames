__author__ = 'akarapetyan'

import sys
from hungrygamesqt.hungrygames import *
try:
    from PyQt4 import QtCore, QtGui
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

except Exception as err:
    print 'HungryGames badly requires PyQt unless you want to run it as a daemon'
    print 'Error message:', err
    sys.exit()


class WarmUpGui:

    def __init__(self):
        #starting the GUI
        self.app = QtGui.QApplication(sys.argv)
        self.HungryGames = QtGui.QMainWindow()
        self.ui = Ui_HungryGames()
        self.ui.setupUi(self.HungryGames)
        self.HungryGames.show()
        #Here goes connectors for buttons
        QtCore.QObject.connect(self.ui.startbutton, QtCore.SIGNAL("clicked()"), self.clicked_startbutton)
        sys.exit(self.app.exec_())

    def clicked_startbutton(self):
        #Checking if we are ready to start the tournament
        fighters = participants(self.ui)
        #Checking that there are at least 2 selected strategies
        if len(fighters) < 2:
            self.msgBox = QMessageBox()
            QtGui.QMessageBox.warning(self.msgBox, 'Warning', "Oops !!! \r\n \r\n You forgot to choose at least 2 strategies", QtGui.QMessageBox.Ok)
            return False
        else:
            return True


def participants(gui):
    fighters = []
    for checkbox in gui.strategybox.children():
        if (isinstance(checkbox, QtGui.QCheckBox)) & (checkbox.objectName() != "referee"):
            if checkbox.isChecked():
                fighters.append(checkbox.objectName())
    return fighters


def run():

    startgui = WarmUpGui()
    return startgui



