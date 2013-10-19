__author__ = 'akarapetyan'

import sys
from hungrygamesmain import *
from hungrygamesqt.hungrygames import *



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

    def clicked_startbutton(self):
        #Checking if we are ready to start the tournament
        fighters = self.participants()
        #Checking that there are at least 2 selected strategies
        if len(fighters) < 2:
            self.msgBox = QMessageBox()
            QtGui.QMessageBox.warning(self.msgBox, 'Warning', "Oops !!! \r\n \r\nYou forgot to choose at least 2 strategies", QtGui.QMessageBox.Ok)
            return False
        else:
            main(self)

    def selectedGame(self):
        #Functions that gets the selected game
        for radio in self.ui.gamebox.children():
            if isinstance(radio, QtGui.QRadioButton):
                if radio.isChecked():
                    return radio.objectName()

    def participants(self):
        #Function that gets the selected strategies
        fighters = []
        for checkbox in self.ui.strategybox.children():
            if (isinstance(checkbox, QtGui.QCheckBox)) & (checkbox.objectName() != "referee"):
                if checkbox.isChecked():
                    fighters.append(checkbox.objectName())
        return fighters

    def GetRoundsQty(self):
        #Function that gets the number of rounds
        return self.ui.roundsqty.intValue()


def run():

    startgui = WarmUpGui()
    return startgui



