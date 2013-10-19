__author__ = 'akarapetyan'

import sys
import hungrygamesqt
import strategies
import games
import singleton

try:
    from PyQt4 import QtCore, QtGui
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

except Exception as err:
    print 'HungryGames badly requires PyQt unless you want to run it as a daemon'
    print 'Error message:', err
    sys.exit()

def ShowSevereError(jet):
    jet.msgBox = QMessageBox()
    QtGui.QMessageBox.critical(jet.msgBox, 'ERROR', "NOP !!! \r\n \r\nCheating is a very dangerous thing. I am shutting down, see you later ;-) ", QtGui.QMessageBox.Ok)
    sys.exit()

def tournament_begin(RoundsNumber, selected_fighters, selected_game):
    k=0


def main(Motor):
    #Warming up fighters
    Fighters = strategies.Strategies()
    selected_fighters = Motor.participants()
    trigger = False
    for selected in selected_fighters:
        for i in Fighters.allstrategies.keys():
            if selected == i:
                trigger = True
                break
            else:
                trigger = False
        if trigger != True:
            break
    if trigger:
         #Preparing the arena
        Games = games.Games()
        selected_game = Motor.selectedGame()
        flag = False
        for i in Games.allgames.keys():
                if selected_game == i:
                    flag = True
        if flag:
            #Getting number of rounds
            RoundsNumber =  Motor.GetRoundsQty()
            #Here we go !! starting the tournament.
            tournament_begin(RoundsNumber, selected_fighters, selected_game)
        else:
            ShowSevereError(Motor)
    else:
        ShowSevereError(Motor)


def Base():
    # is the application already running?  If yes then exit.
    thisapp = singleton.singleinstance()
    #Simply calls and starts the GUI
    Base = hungrygamesqt.run()
    Base.app.exec_()

if __name__ == "__main__":
    Base()