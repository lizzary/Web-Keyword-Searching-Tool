from package.ui.control.ui_bulider.Slot import Slot
from PyQt6 import QtCore, QtGui, QtWidgets

class Connect(Slot):
    def __init__(self,Form:QtWidgets.QWidget):
        super().__init__(Form)

        #checkbox
        self.Batch_Input_Checkbox.stateChanged.connect(self.check_batch_input_checkbox_state)
        self.Batch_Input_Count_Internal_Link_checkBox.stateChanged.connect(self.batch_input_count_internal_url_checkbox_state)
        self.Single_Input_Checkbox.stateChanged.connect(self.check_single_input_checkbox_state)
        self.Single_Input_Count_Internal_Link_checkBox.stateChanged.connect(self.single_input_count_internal_url_checkbox_state)


        #browse pushbutton
        self.Single_Output_Path_pushButton.released.connect(self.Single_Output_Path_pushButton.connect_open_folder)
        self.Batch_Input_Searching_Target_List_Path_pushButton.released.connect(self.Batch_Input_Searching_Target_List_Path_pushButton.connect_open_file)
        self.Batch_Input_Keyword_list_Path_pushButton.released.connect(self.Batch_Input_Keyword_list_Path_pushButton.connect_open_file)
        self.Batch_Output_Path_pushButton.released.connect(self.Batch_Output_Path_pushButton.connect_open_folder)

        #lineEdit
        self.URL_lineEdit.textChanged.connect(self.single_url_lineEdit_event)
        self.Single_keyword_lineEdit.textChanged.connect(self.single_keyword_lineEdit_event)
        self.Single_Output_Path_lineEdit.textChanged.connect(self.single_output_path_lineEdit_event)
        self.Batch_Input_Searching_Target_List_Path_Input_lineEdit.textChanged.connect(self.batch_input_searching_target_list_path_lineEdit_event)
        self.Batch_Input_Keyword_List_Input_Path_lineEdit.textChanged.connect(self.batch_keyword_list_path_lineEdit_event)
        self.Batch_Output_Path_lineEdit.textChanged.connect(self.batch_output_path_lineEdit_event)

        #reset pushbutton
        self.Reset_pushButton.released.connect(self.reset)

        #cancel pushbutton
        self.Cancel_pushButton.released.connect(self.cancel)

        #start pushbutton
        self.Start_pushButton.released.connect(self.start)


