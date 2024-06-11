from package.data import Crawler
class Query_Word(object):
    def __init__(self,query_str):
        self.__query_str = query_str
        self.__matched_digit = 0
        self.__matched_num = 0

    def get_matched_num(self):
        return self.__matched_num
    def check_digit(self,check):
        if self.__query_str == '':
            return
        if self.__query_str[self.__matched_digit] != check :
            self.__matched_digit = 0
            return


        if self.__query_str[self.__matched_digit] == check :
            self.__matched_digit += 1

            if self.__matched_digit == len(self.__query_str) :
                self.__matched_num += 1
                self.__matched_digit = 0

#count the frequency of the words in query_str_list
#input parameter:
#text: the original article
#query_str_list: the words you need to count, must be a list
#return: count num of the query_str_list with SAME list key
def count(text,query_str_list):

    length = len(query_str_list)
    query_obj = [Query_Word(word) for word in query_str_list]
    for word in text:
        for i in range(length):
            query_obj[i].check_digit(word)

    result = []
    for i in range(length):
        result.append(query_obj[i].get_matched_num())

    return result

if __name__ == "__main__":
    url = "https://projectmanager.com.tw/%e5%b0%88%e6%a1%88%e7%ae%a1%e7%90%86/%e5%b0%88%e6%a1%88%e7%ae%a1%e7%90%86%e6%98%af%e4%bb%80%e9%ba%bc/"
    a = "專案管理"
    b = "知識技能"
    c = "的"
    d ="我"
    e ="爱"
    content = Crawler.get_page_content(url)
    print(count(content,[a,b,c,d,e]))

