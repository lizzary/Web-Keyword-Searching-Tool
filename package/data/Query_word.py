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


