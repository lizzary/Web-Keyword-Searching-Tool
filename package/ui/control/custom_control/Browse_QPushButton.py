from PyQt6 import QtWidgets

class Browse_QPushButton(QtWidgets.QPushButton):
    def __init__(self, parent, connection_unit_obj:QtWidgets.QLineEdit,file_format_filter:str):
        super().__init__(parent)
        self.connection_unit_obj = connection_unit_obj
        self.file_format_filter = file_format_filter

    #slot function(use to be connect() with button
    def connect_open_file(self):
        #third para "directory": default path when open a file, "" is the program's path
        file_name, file_format = QtWidgets.QFileDialog.getOpenFileName(self,
                                "Please select a input file","",self.file_format_filter)

        self.connection_unit_obj.setText(file_name)
        self.connection_unit_obj.setStyleSheet("color:black")

    def connect_open_folder(self):
        fd = QtWidgets.QFileDialog.getExistingDirectory(self,"Please select a folder","")
        self.connection_unit_obj.setText(fd)
        self.connection_unit_obj.setStyleSheet("color:black")
