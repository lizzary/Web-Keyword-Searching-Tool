from PyQt6 import QtWidgets,QtGui

class Dropable_QLineEdit(QtWidgets.QLineEdit):
    def __init__(self,parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setPlaceholderText("(Drop, browse or input your file here)")

    def dragEnterEvent(self, e:QtGui.QDropEvent):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e:QtGui.QDropEvent):
        filePathList = e.mimeData().text()
        filePath = filePathList.split('\n')[0]
        filePath = filePath.replace('file:///','',1)
        self.setText(filePath)
        self.setStyleSheet("color:black")



