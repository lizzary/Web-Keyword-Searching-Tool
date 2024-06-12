from package.ui.control.ui_bulider.MainPage import Main_Page
from PyQt6 import QtCore, QtGui, QtWidgets
from package.ui.control import event_data
from package.data.Data import data_reader,data_writer
from package.data.Count import Count
import re
import os


class Slot(Main_Page):
    def __init__(self,Form:QtWidgets.QWidget):
        super().__init__(Form)

    def check_batch_input_checkbox_state(self):
        #checked
        if(self.Batch_Input_Checkbox.checkState().value == 2):
            self.Batch_Input_Groupbox.setDisabled(False)
            self.Single_Input_Checkbox.setChecked(False)

            self.Batch_Input_Searching_Target_List_Path_Input_lineEdit.setStyleSheet("color:black")
            self.Batch_Input_Keyword_List_Input_Path_lineEdit.setStyleSheet("color:black")
            self.Batch_Output_Path_lineEdit.setStyleSheet("color:black")

        #unchecked
        if(self.Batch_Input_Checkbox.checkState().value == 0):
            self.Batch_Input_Groupbox.setDisabled(True)

            self.Batch_Input_Searching_Target_List_Path_Input_lineEdit.setStyleSheet("color:#A0A0A0")
            self.Batch_Input_Keyword_List_Input_Path_lineEdit.setStyleSheet("color:#A0A0A0")
            self.Batch_Output_Path_lineEdit.setStyleSheet("color:#A0A0A0")

    def check_single_input_checkbox_state(self):
        #checked
        if(self.Single_Input_Checkbox.checkState().value == 2):
            self.Single_Input_Groupbox.setDisabled(False)
            self.Batch_Input_Checkbox.setChecked(False)

            self.URL_lineEdit.setStyleSheet("color:black")
            self.single_keyword_lineEdit.setStyleSheet("color:black")
            self.Single_Output_Path_lineEdit.setStyleSheet("color:black")

        #unchecked
        if(self.Single_Input_Checkbox.checkState().value == 0):
            self.Single_Input_Groupbox.setDisabled(True)

            self.URL_lineEdit.setStyleSheet("color:#A0A0A0")
            self.single_keyword_lineEdit.setStyleSheet("color:#A0A0A0")
            self.Single_Output_Path_lineEdit.setStyleSheet("color:#A0A0A0")

    def single_url_lineEdit_event(self):
        event_data.URL_LINEEDIT_CONTENT = self.URL_lineEdit.text()
        self.URL_lineEdit.setStyleSheet("color:black")
        print(event_data.URL_LINEEDIT_CONTENT)

    def single_keyword_lineEdit_event(self):
        event_data.SINGLE_INPUT_KEYWORD = self.single_keyword_lineEdit.text()
    def single_output_path_lineEdit_event(self):
        event_data.SINGLE_OUTPUT_PATH_LINEEDIT_CONTENT = self.Single_Output_Path_lineEdit.text()
        self.Single_Output_Path_lineEdit.setStyleSheet("color:black")
        print(event_data.SINGLE_OUTPUT_PATH_LINEEDIT_CONTENT)

    def batch_input_searching_target_list_path_lineEdit_event(self):
        event_data.BATCH_INPUT_SEARCHING_TARGET_LIST_PATH_LINEEDIT_CONTENT = self.Batch_Input_Searching_Target_List_Path_Input_lineEdit.text()

        file_folder_path = os.path.dirname(event_data.BATCH_INPUT_SEARCHING_TARGET_LIST_PATH_LINEEDIT_CONTENT)
        if(file_folder_path != ''):
            self.Batch_Output_Path_lineEdit.setText(file_folder_path)

        self.Batch_Input_Searching_Target_List_Path_Input_lineEdit.setStyleSheet("color:black")
        print(event_data.BATCH_INPUT_SEARCHING_TARGET_LIST_PATH_LINEEDIT_CONTENT)

    def batch_keyword_list_path_lineEdit_event(self):
        event_data.BATCH_INPUT_KEYWORD_LIST_PATH_LINEEDIT_CONTENT = self.Batch_Input_Keyword_List_Input_Path_lineEdit.text()

        file_folder_path = os.path.dirname(event_data.BATCH_INPUT_KEYWORD_LIST_PATH_LINEEDIT_CONTENT)
        if(file_folder_path != ''):
            self.Batch_Output_Path_lineEdit.setText(file_folder_path)

        self.Batch_Input_Keyword_List_Input_Path_lineEdit.setStyleSheet("color:black")
        print(event_data.BATCH_INPUT_KEYWORD_LIST_PATH_LINEEDIT_CONTENT)



    def batch_output_path_lineEdit_event(self):
        event_data.BATCH_OUTPUT_PATH_LINEEDIT_CONTENT = self.Batch_Output_Path_lineEdit.text()
        self.Batch_Output_Path_lineEdit.setStyleSheet("color:black")
        print('output: '+event_data.BATCH_OUTPUT_PATH_LINEEDIT_CONTENT)


    def reset(self):
        self.URL_lineEdit.clear()
        event_data.URL_LINEEDIT_CONTENT = ""

        self.single_keyword_lineEdit.clear()
        event_data.SINGLE_INPUT_KEYWORD = ""

        self.Single_Output_Path_lineEdit.clear()
        event_data.SINGLE_INPUT_KEYWORD = ""

        self.Batch_Input_Searching_Target_List_Path_Input_lineEdit.clear()
        event_data.BATCH_INPUT_SEARCHING_TARGET_LIST_PATH_LINEEDIT_CONTENT = ""

        self.Batch_Input_Keyword_List_Input_Path_lineEdit.clear()
        event_data.BATCH_INPUT_KEYWORD_LIST_PATH_LINEEDIT_CONTENT = ""

        self.Batch_Output_Path_lable.clear()
        event_data.BATCH_OUTPUT_PATH_LINEEDIT_CONTENT = ""

    def cancel(self):
        event_data.SEARCHING_PROCESSING= False

    def start(self):
        self.System_Message_textBrowser.clear()
        self.searching_process.setValue(0)

        if(self.Batch_Input_Checkbox.checkState().value == 2):
            url_file_reader = data_reader(event_data.BATCH_INPUT_SEARCHING_TARGET_LIST_PATH_LINEEDIT_CONTENT)
            keyword_file_reader = data_reader(event_data.BATCH_INPUT_KEYWORD_LIST_PATH_LINEEDIT_CONTENT)

            self.searching_process.setValue(10)


            if(url_file_reader.try_to_read_excel_columns() == False):
                self.System_Message_textBrowser.append('ERROR! Please check your searching target list file and path')

            if(keyword_file_reader.try_to_read_excel_columns() == False):
                self.System_Message_textBrowser.append('ERROR! Please check your keywork list file and path')

            if (len(url_file_reader.result_list) > len(keyword_file_reader.result_list)):
                for i in range(len(url_file_reader.result_list) - len(keyword_file_reader.result_list)):
                    keyword_file_reader.result_list.append([])

            self.searching_process.setValue(20)

            count_obj_list = [Count(i[0], k) if i != [] else Count('', k) for i, k in zip(url_file_reader.result_list, keyword_file_reader.result_list)]
            print('keywords_list',keyword_file_reader.result_list)


            self.searching_process.setValue(50)

            for obj in count_obj_list:
                obj.count_keyword()

            self.searching_process.setValue(80)

            filepath = ''
            for obj in count_obj_list:
                if(obj.available_URL == True):
                    filepath = data_writer(obj,event_data.BATCH_OUTPUT_PATH_LINEEDIT_CONTENT).filepath
                    break

            print('filepath is=',filepath)
            output_writer_list = [data_writer(count_obj,filepath) for count_obj in count_obj_list]

            # delete old result report
            if os.path.exists(filepath):
                os.remove(filepath)

            for obj in output_writer_list:
                obj.write(self.System_Message_textBrowser.append)

                try:
                    f = open(filepath, 'a', encoding='utf-8')

                    def write_file(text):
                        if (text != ' '):
                            f.write(text + '\n')
                        if (text == ' '):
                            f.write('\n')
                    obj.write(write_file)

                except FileNotFoundError:
                    self.System_Message_textBrowser.append('ERROR! Please check your output path')

            self.searching_process.setValue(100)



        if(self.Single_Input_Checkbox.checkState().value == 2):
            url = event_data.URL_LINEEDIT_CONTENT
            keywords_input = re.split('\n|;|；',event_data.SINGLE_INPUT_KEYWORD)
            lower_case_keywords_input = [word.lower() for word in keywords_input]
            count = Count(url,lower_case_keywords_input)
            count.count_keyword()

            self.searching_process.setValue(50)

            output_writer = data_writer(count,event_data.SINGLE_OUTPUT_PATH_LINEEDIT_CONTENT)

            output_writer.write(self.System_Message_textBrowser.append)

            self.searching_process.setValue(100)

            if(output_writer.filepath == ''):
                return


            try:
                # delete old result report
                if os.path.exists(output_writer.filepath):
                    os.remove(output_writer.filepath)

                f = open(output_writer.filepath, 'a', encoding='utf-8')

                def write_file(text):
                    if (text != ' '):
                        f.write(text + '\n')
                    if (text == ' '):
                        f.write('\n')
                output_writer.write(write_file)

            except FileNotFoundError:
                self.System_Message_textBrowser.append('ERROR! Please check your output path')





































