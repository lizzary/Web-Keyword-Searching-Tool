import pandas as pd
from package.data.Count import Count
from package.data import Crawler
import time

class data_reader(object):
    def __init__(self,filepath:str):
        self.filepath = filepath
        self.result_list:list[list[str|int|float]] = []#[ [<1st columns>],[<2nd columns>],...]

    #query_str_list may have 'nan' element, using 'nan' != 'nan' to determine whether the element is a 'nan' data
    def __is_nan(self,element):
        return element != element

    def try_to_read_excel_columns(self):
        try:
            df = pd.read_excel(self.filepath, header=None,dtype=str)
        except FileNotFoundError:
            return False

        if(df.empty == True):
            return False

        columns_list = df.columns.tolist()
        for column in columns_list:
            column_data = df[column].tolist()
            data = [element.lower() for element in column_data if self.__is_nan(element) == False]
            self.result_list.append(data)

        print('col',self.result_list)
        return True

class data_writer(object):
    def __init__(self,filepath:str,count_obj:Count):
        self.filepath = filepath+'/result.txt'
        self.URL = count_obj.URL
        self.available_URL = count_obj.available_URL
        self.page_title = ''
        self.keywords_list = count_obj.query_str_list
        self.keywords_searching_result_list = count_obj.result

        if(self.available_URL == True):
            self.page_title = Crawler.get_page_title(self.URL)

    def write(self, write_fun):

        if(self.available_URL == False):
            write_fun('----------------------------------------------------------------------')
            write_fun(' ')
            write_fun('無法訪問該網頁，請檢查域名和網絡鏈接')
            write_fun(' ')
            return True

        write_fun('----------------------------------------------------------------------')
        write_fun(' ')
        write_fun('標題：')
        write_fun(self.page_title)
        write_fun(' ')
        write_fun('關鍵詞：')


        if(self.keywords_list == [] or self.keywords_list == ['']):
            write_fun('#EMPTY KEYWORD#')
            return

        for i in range(len(self.keywords_list)):
            if(self.keywords_list[i] == []):
                continue
            if(self.keywords_searching_result_list[i] == 0):
                appear_num = 'NOT FOUND'
            else:
                appear_num = str(self.keywords_searching_result_list[i])
            write_fun(str(self.keywords_list[i])+' -> '+appear_num)
        write_fun(' ')

        t = time.localtime()
        write_fun('查詢日期：'+str(t.tm_year)+'/'+str(t.tm_mon)+'/'+str(t.tm_mday)+' '+str(t.tm_hour)+':'+str(t.tm_min))
        write_fun(' ')

        return True



