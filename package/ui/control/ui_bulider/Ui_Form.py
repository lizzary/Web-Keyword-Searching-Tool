############################################################################################
#   _________________________                                                              #
#   |                       | decorate  ___________ decorate  ______ decorate  _________   #
#   | QtWidgets.QWidget obj | --------> |Main_Page| --------> |Slot| --------> |Connect|   #
#   |                       | <-------- ‾‾‾‾‾‾‾‾‾‾‾ <-------- ‾‾‾‾‾‾ <-------- ‾‾‾‾‾‾‾‾‾   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ inheritance            inheritance     inheritance           #
############################################################################################

from package.ui.control.ui_bulider.MainPage import Main_Page
from package.ui.control.ui_bulider.Slot import Slot
from package.ui.control.ui_bulider.Connect import Connect
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(Connect):
    def __init__(self,Form:QtWidgets.QWidget):
        super().__init__(Form)

