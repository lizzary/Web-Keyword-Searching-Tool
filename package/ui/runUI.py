import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from package.ui.control.ui_bulider.Ui_Form import Ui_Form


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form(self)

def run():
    app = QtWidgets.QApplication(sys.argv)
    myWidget = Widget()
    myWidget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWidget = Widget()
    myWidget.show()
    sys.exit(app.exec())