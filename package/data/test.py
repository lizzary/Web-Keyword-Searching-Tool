from package.ui.control.ui_bulider.MainPage import Main_Page
from PyQt6 import QtCore, QtGui, QtWidgets
from package.ui.control import event_data
from package.data import Crawler
from package.data.Data import *
from package.data.Count import Count
import numpy
import re
import os

if __name__ == '__main__':
    # a = "C:/Users/DELL/Desktop/文件/临时1/新建文件夹 (2)/input.xlsx"
    # b = "C:/Users/DELL/Desktop/文件/临时1/新建文件夹 (2)/keyword.xlsx"
    # o = "C:/Users/DELL/Desktop/文件/临时1/新建文件夹 (2)"
    #
    # if os.path.exists(o+'/result.txt'):
    #     os.remove(o+'/result.txt')
    #
    # url_file_reader = data_reader(a)
    # keyword_file_reader = data_reader(b)
    # url_file_reader.try_to_read_excel_columns()
    # keyword_file_reader.try_to_read_excel_columns()
    #
    # count_obj_list = [Count(i[0], k) for i, k in zip(url_file_reader.result_list, keyword_file_reader.result_list)]
    #
    # # 2d list
    # result_list = [obj.count_keyword() for obj in count_obj_list]
    #
    # length = len(url_file_reader.result_list)
    #
    # output_writer_list = [data_writer(o,count_obj) for count_obj in count_obj_list]
    #
    # # for i in output_writer_list:
    # #     i.try_to_write()
    # f = open(o + '/result.txt', 'a', encoding='utf-8')
    # def mywrite(text):
    #     if(text != ' '):
    #         f.write(text+'\n')
    #     if(text == ' '):
    #         f.write('\n')
    #
    # for i in output_writer_list:
    #     i.write(mywrite)
    aa = []
    print([a for a in aa])
    print(aa[0])

