import pandas as pd
from package.data.Count import Count
from package.data import Crawler
from package.ui.control import event_data
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
            df = pd.read_excel(self.filepath, header=None,dtype=str)  # 设置header参数为None，使用默认的列索引作为列名称
        except FileNotFoundError:
            return False

        if(df.empty == True):
            return False

        columns_list = df.columns.tolist()
        for column in columns_list:
            column_data = df[column].tolist()
            data = [element.lower() for element in column_data if self.__is_nan(element) == False]
            self.result_list.append(data)

        return True

class data_writer(object):
    def __init__(self,count_obj:Count,folderpath:str):
        self.filepath = folderpath + '/result.txt'
        self.URL = count_obj.URL
        self.available_URL = count_obj.available_URL
        self.page_title = ''
        self.keywords_list = count_obj.query_str_list
        self.keywords_searching_result_list = count_obj.query_str_result_list
        self.internal_link_words_list:list[str] = count_obj.keyword_list_with_internal_link
        self.internal_link_url_list:list[str] = count_obj.internal_link_url_list

        if(self.available_URL == True):
            self.page_title = Crawler.get_page_title(self.URL)
            self.filepath = folderpath + '/' + self.__replace_special_chars(self.page_title,' ') + '.txt'

    def __replace_special_chars(self,text, replacement):
        special_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
        for char in special_chars:
            text = text.replace(char, replacement)
        return text

    def write(self, write_fun):

        if(self.available_URL == False):
            write_fun('----------------------------------------------------------------------')
            write_fun(' ')
            write_fun('無法搜索到指定對象，請檢查域名和網絡連接')
            write_fun(' ')
            return True

        write_fun('----------------------------------------------------------------------')
        write_fun(' ')
        write_fun('標題: ')
        write_fun(self.page_title)
        write_fun(' ')
        write_fun('關鍵詞: ')


        if(self.keywords_list == [] or self.keywords_list == ['']):
            write_fun('#EMPTY KEYWORD#')
            write_fun(' ')
        else:
            for i in range(len(self.keywords_list)):
                if(self.keywords_list[i] == []):
                    continue
                if(self.keywords_searching_result_list[i] == 0):
                    appear_num = 'NOT FOUND'
                else:
                    appear_num = str(self.keywords_searching_result_list[i])
                write_fun(str(self.keywords_list[i])+' -> '+appear_num)
            write_fun(' ')

        if( event_data.COUNT_INTERNAL_LINK == True):
            write_fun('內部鏈接統計: ')
            if(self.internal_link_words_list == [] or self.internal_link_url_list == []):
                write_fun('#EMPTY INTERNAL LINK')
                write_fun(' ')
            else:
                for i in range(len(self.internal_link_url_list)):
                    write_fun('內部鏈接: ' + self.internal_link_url_list[i])
                    write_fun('被引總數: ' + str( len(self.internal_link_words_list[i]) ) )
                    write_fun('引用條目: ' + '1.' + self.internal_link_words_list[i][0])
                    for j in range(1,len(self.internal_link_words_list[i])):
                        write_fun('                '+str(j+1) +'.' + self.internal_link_words_list[i][j])
                    write_fun(' ')


        t = time.localtime()
        write_fun('查詢日期：'+str(t.tm_year)+'/'+str(t.tm_mon)+'/'+str(t.tm_mday)+' '+str(t.tm_hour)+':'+str(t.tm_min))
        write_fun(' ')

        return True



