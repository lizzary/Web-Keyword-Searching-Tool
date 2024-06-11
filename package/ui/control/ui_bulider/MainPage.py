
from package.ui.control.custom_control.Dropable_QLineEdit import Dropable_QLineEdit
from package.ui.control.custom_control.Browse_QPushButton import Browse_QPushButton
from PyQt6 import QtCore, QtGui, QtWidgets

class Main_Page(object):
    def __init__(self,Form:QtWidgets.QWidget):
        # overview setting
        Form.setObjectName("Form")
        Form.setFixedSize(1075, 454)  # fix the window size

        self.Input_Ouput_Setting_Groupbox = QtWidgets.QGroupBox(parent=Form)
        self.Input_Ouput_Setting_Groupbox.setGeometry(QtCore.QRect(20, 10, 1031, 241))
        self.Input_Ouput_Setting_Groupbox.setObjectName("Input_Ouput_Setting_Groupbox")

        self.Single_Input_Checkbox = QtWidgets.QCheckBox(parent=self.Input_Ouput_Setting_Groupbox)
        self.Single_Input_Checkbox.setGeometry(QtCore.QRect(20, 20, 121, 23))
        self.Single_Input_Checkbox.setObjectName("Single_Input_Checkbox")
        self.Single_Input_Checkbox.setChecked(True)

        self.Single_Input_Groupbox = QtWidgets.QGroupBox(parent=self.Input_Ouput_Setting_Groupbox)
        self.Single_Input_Groupbox.setGeometry(QtCore.QRect(20, 50, 491, 171))
        self.Single_Input_Groupbox.setTitle("")
        self.Single_Input_Groupbox.setObjectName("Single_Input_Groupbox")

        self.URL_lable = QtWidgets.QLabel(parent=self.Single_Input_Groupbox)
        self.URL_lable.setGeometry(QtCore.QRect(20, 10, 51, 19))
        self.URL_lable.setObjectName("URL_lable")

        self.URL_lineEdit = QtWidgets.QLineEdit(parent=self.Single_Input_Groupbox)
        self.URL_lineEdit.setGeometry(QtCore.QRect(20, 30, 351, 25))
        self.URL_lineEdit.setObjectName("URL_lineEdit")

        self.single_Keyword_lable = QtWidgets.QLabel(parent=self.Single_Input_Groupbox)
        self.single_Keyword_lable.setGeometry(QtCore.QRect(20, 60, 91, 19))
        self.single_Keyword_lable.setObjectName("single_Keyword_lable")

        self.single_keyword_lineEdit = QtWidgets.QLineEdit(parent=self.Single_Input_Groupbox)
        self.single_keyword_lineEdit.setGeometry(QtCore.QRect(20, 80, 351, 25))
        self.single_keyword_lineEdit.setObjectName("single_keyword_lineEdit")

        self.Single_Output_Path_lable = QtWidgets.QLabel(parent=self.Single_Input_Groupbox)
        self.Single_Output_Path_lable.setGeometry(QtCore.QRect(20, 110, 101, 19))
        self.Single_Output_Path_lable.setObjectName("Single_Output_Path_lable")

        self.Single_Output_Path_lineEdit = Dropable_QLineEdit(parent=self.Single_Input_Groupbox)
        self.Single_Output_Path_lineEdit.setGeometry(QtCore.QRect(20, 130, 351, 25))
        self.Single_Output_Path_lineEdit.setObjectName("Single_Output_Path_lineEdit")

        self.Single_Output_Path_pushButton = Browse_QPushButton(parent=self.Single_Input_Groupbox,
                                                                connection_unit_obj=self.Single_Output_Path_lineEdit,
                                                                file_format_filter="Folder")
        self.Single_Output_Path_pushButton.setGeometry(QtCore.QRect(380, 130, 93, 28))
        self.Single_Output_Path_pushButton.setObjectName("Single_Output_Path_pushButton")

        self.Batch_Input_Checkbox = QtWidgets.QCheckBox(parent=self.Input_Ouput_Setting_Groupbox)
        self.Batch_Input_Checkbox.setGeometry(QtCore.QRect(530, 20, 121, 23))
        self.Batch_Input_Checkbox.setObjectName("Batch_Input_Checkbox")
        self.Batch_Input_Checkbox.setChecked(False)

        self.Batch_Input_Groupbox = QtWidgets.QGroupBox(parent=self.Input_Ouput_Setting_Groupbox)
        self.Batch_Input_Groupbox.setGeometry(QtCore.QRect(530, 50, 481, 171))
        self.Batch_Input_Groupbox.setTitle("")
        self.Batch_Input_Groupbox.setObjectName("Batch_Input_Groupbox")
        self.Batch_Input_Groupbox.setDisabled(True)

        self.Batch_Input_Searching_Target_List_Path_lable = QtWidgets.QLabel(parent=self.Batch_Input_Groupbox)
        self.Batch_Input_Searching_Target_List_Path_lable.setGeometry(QtCore.QRect(20, 10, 241, 19))
        self.Batch_Input_Searching_Target_List_Path_lable.setObjectName("Batch_Input_Searching_Target_List_Path_lable")

        self.Batch_Input_Searching_Target_List_Path_Input_lineEdit = Dropable_QLineEdit(parent=self.Batch_Input_Groupbox)
        self.Batch_Input_Searching_Target_List_Path_Input_lineEdit.setGeometry(QtCore.QRect(20, 30, 341, 25))
        self.Batch_Input_Searching_Target_List_Path_Input_lineEdit.setObjectName("Batch_Input_Searching_Target_List_Path_Input_lineEdit")

        self.Batch_Input_Searching_Target_List_Path_pushButton = Browse_QPushButton(parent=self.Batch_Input_Groupbox,
                                                                          connection_unit_obj=self.Batch_Input_Searching_Target_List_Path_Input_lineEdit,
                                                                          file_format_filter="*.xlsx;;*.xlsm;;*.xls;;*.xltx;;*.xltm;;*.xlt")
        self.Batch_Input_Searching_Target_List_Path_pushButton.setGeometry(QtCore.QRect(370, 30, 93, 28))
        self.Batch_Input_Searching_Target_List_Path_pushButton.setObjectName("Batch_Input_Searching_Target_List_Path_pushButton")

        self.Keyword_list_Input_lable = QtWidgets.QLabel(parent=self.Batch_Input_Groupbox)
        self.Keyword_list_Input_lable.setGeometry(QtCore.QRect(20, 60, 141, 19))
        self.Keyword_list_Input_lable.setObjectName("Keyword_list_Input_lable")

        self.Batch_Input_Keyword_List_Input_Path_lineEdit = Dropable_QLineEdit(parent=self.Batch_Input_Groupbox)
        self.Batch_Input_Keyword_List_Input_Path_lineEdit.setGeometry(QtCore.QRect(20, 80, 341, 25))
        self.Batch_Input_Keyword_List_Input_Path_lineEdit.setObjectName("Batch_Input_Keyword_List_Input_Path_lineEdit")

        self.Batch_Input_Keyword_list_Path_pushButton = Browse_QPushButton(parent=self.Batch_Input_Groupbox,
                                                                          connection_unit_obj=self.Batch_Input_Keyword_List_Input_Path_lineEdit,
                                                                          file_format_filter="*.xlsx;;*.xlsm;;*.xls;;*.xltx;;*.xltm;;*.xlt")
        self.Batch_Input_Keyword_list_Path_pushButton.setGeometry(QtCore.QRect(370, 80, 93, 28))
        self.Batch_Input_Keyword_list_Path_pushButton.setObjectName("Batch_Input_Keyword_list_Path_pushButton")

        self.Batch_Output_Path_lable = QtWidgets.QLabel(parent=self.Batch_Input_Groupbox)
        self.Batch_Output_Path_lable.setGeometry(QtCore.QRect(20, 110, 101, 19))
        self.Batch_Output_Path_lable.setObjectName("Batch_Output_Path_lable")

        self.Batch_Output_Path_lineEdit = Dropable_QLineEdit(parent=self.Batch_Input_Groupbox)
        self.Batch_Output_Path_lineEdit.setGeometry(QtCore.QRect(20, 130, 341, 25))
        self.Batch_Output_Path_lineEdit.setObjectName("Batch_Output_Path_lineEdit")

        self.Batch_Output_Path_pushButton = Browse_QPushButton(parent=self.Batch_Input_Groupbox,
                                                                          connection_unit_obj=self.Batch_Output_Path_lineEdit,
                                                                          file_format_filter="Folder")
        self.Batch_Output_Path_pushButton.setGeometry(QtCore.QRect(370, 130, 93, 28))
        self.Batch_Output_Path_pushButton.setObjectName("Batch_Output_Path_pushButton")

        self.searching_process = QtWidgets.QProgressBar(parent=Form)
        self.searching_process.setGeometry(QtCore.QRect(20, 260, 1031, 23))
        self.searching_process.setProperty("value", 0)
        self.searching_process.setTextVisible(False)
        self.searching_process.setInvertedAppearance(False)
        self.searching_process.setObjectName("searching_process")

        self.Reset_pushButton = QtWidgets.QPushButton(parent=Form)
        self.Reset_pushButton.setGeometry(QtCore.QRect(760, 290, 93, 28))
        self.Reset_pushButton.setObjectName("Reset_pushButton")

        self.Cancel_pushButton = QtWidgets.QPushButton(parent=Form)
        self.Cancel_pushButton.setGeometry(QtCore.QRect(860, 290, 93, 28))
        self.Cancel_pushButton.setObjectName("Cancel_pushButton")

        self.Start_pushButton = QtWidgets.QPushButton(parent=Form)
        self.Start_pushButton.setGeometry(QtCore.QRect(960, 290, 93, 28))
        self.Start_pushButton.setObjectName("Start_pushButton")

        self.System_Message_label = QtWidgets.QLabel(parent=Form)
        self.System_Message_label.setGeometry(QtCore.QRect(20, 310, 121, 19))
        self.System_Message_label.setObjectName("System_Message_label")

        self.System_Message_textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.System_Message_textBrowser.setGeometry(QtCore.QRect(20, 330, 1031, 101))
        self.System_Message_textBrowser.setObjectName("System_Message_textBrowser")

        self.retranslateUi(Form)
        # QtCore.QMetaObject.connectSlotsByName(Form)
        # Form.setTabOrder(self.Browse_pushButton1, self.Batch_Input)
        # Form.setTabOrder(self.Batch_Input, self.Output_Path_lineEdit)
        # Form.setTabOrder(self.Output_Path_lineEdit, self.Browse_pushButton2)
        # Form.setTabOrder(self.Browse_pushButton2, self.Input_Path_lineEdit)

    def retranslateUi(self, Form:QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Input_Ouput_Setting_Groupbox.setTitle(_translate("Form", "Input/Output Setting"))
        self.Batch_Input_Searching_Target_List_Path_lable.setText(_translate("Form", "Searching Target List Path:"))
        self.Batch_Input_Searching_Target_List_Path_pushButton.setText(_translate("Form", "Browse"))
        self.Batch_Output_Path_lable.setText(_translate("Form", "Output Path:"))
        self.Batch_Output_Path_pushButton.setText(_translate("Form", "Browse"))
        self.Keyword_list_Input_lable.setText(_translate("Form", "Keyword list Path:"))
        self.Batch_Input_Keyword_list_Path_pushButton.setText(_translate("Form", "Browse"))
        self.Batch_Input_Checkbox.setText(_translate("Form", "Batch Input"))
        self.Single_Input_Checkbox.setText(_translate("Form", "Single Input"))
        self.URL_lable.setText(_translate("Form", "URL:"))
        self.Single_Output_Path_pushButton.setText(_translate("Form", "Browse"))
        self.single_Keyword_lable.setText(_translate("Form", "Keyword:"))
        self.Single_Output_Path_lable.setText(_translate("Form", "Output Path:"))
        self.searching_process.setFormat(_translate("Form", "%p%"))
        self.System_Message_label.setText(_translate("Form", "System Message"))
        self.Start_pushButton.setText(_translate("Form", "Start"))
        self.Cancel_pushButton.setText(_translate("Form", "Cancel"))
        self.Reset_pushButton.setText(_translate("Form", "Reset"))

