from package.data import Crawler
from package.data.Query_word import Query_Word

class Count(object):
    def __init__(self,URL:str,query_str_list:list[str]):
        self.URL:str = URL
        self.available_URL:bool = False
        self.query_str_list:list[str] = query_str_list
        self.query_str_result_list:list[str] = []
        self.internal_link_url_list: list[str] = []
        self.keyword_list_with_internal_link: list[str] = []


    def count_keyword(self):

        text = Crawler.get_page_content(self.URL)
        if(text == False):
            self.available_URL = False
            return self
        else:
            self.available_URL = True

        if(self.query_str_list == []):
            return self

        query_obj = [Query_Word(word) for word in self.query_str_list]
        length = len(query_obj)

        self.query_str_result_list = []
        for word in text:
            for i in range(length):
                query_obj[i].check_digit(word)

        for i in range(length):
            self.query_str_result_list.append(query_obj[i].matched_num)


        return self

    def count_internal_link(self):
        if(self.available_URL == True):
            self.internal_link_url_list,self.keyword_list_with_internal_link = Crawler.get_internal_link(self.URL)
        return self









