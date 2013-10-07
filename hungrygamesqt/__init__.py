__author__ = 'akarapetyan'

import sys
from hungrygames import *
try:
    from PyQt4 import QtCore, QtGui
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

except Exception as err:
    print 'HungryGames badly requires PyQt unless you want to run it as a daemon'
    print 'Error message:', err
    sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    HungryGames = QtGui.QMainWindow()
    ui = Ui_HungryGames()
    ui.setupUi(HungryGames)
    HungryGames.show()
    sys.exit(app.exec_())



