from package.data import Crawler
from package.data.Query_word import Query_Word

class Count(object):
    def __init__(self,URL:str,query_str_list:list[str]):
        self.URL = URL
        self.available_URL = False
        self.query_str_list = query_str_list
        self.result = []


    # if query_str_list is empty or wrong url, return false
    def count_keyword(self):

        text = Crawler.get_page_content(self.URL)
        if(text == False):
            self.available_URL = False
            return False
        else:
            self.available_URL = True

        if(self.query_str_list == []):
            return False

        query_obj = [Query_Word(word) for word in self.query_str_list]
        length = len(query_obj)

        self.result = []
        for word in text:
            for i in range(length):
                query_obj[i].check_digit(word)

        for i in range(length):
            self.result.append(query_obj[i].get_matched_num())


        return True









