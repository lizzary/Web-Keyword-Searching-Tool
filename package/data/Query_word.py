class Query_Word(object):
    def __init__(self,query_str):
        self.query_str = query_str
        self.matched_digit = 0
        self.matched_num = 0

    def check_digit(self,check):
        if self.query_str == '':
            return
        if self.query_str[self.matched_digit] != check :
            self.matched_digit = 0
            return


        if self.query_str[self.matched_digit] == check :
            self.matched_digit += 1

            if self.matched_digit == len(self.query_str) :
                self.matched_num += 1
                self.matched_digit = 0

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
        result.append(query_obj[i].matched_num)

    return result


