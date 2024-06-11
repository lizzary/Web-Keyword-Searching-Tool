from DrissionPage import  SessionPage

DEFAULT_STR_FILTER_LIST = ['nav','ez-toc']
#print the html element list in the format:<html element>   <content> or pure content
#input parameter:
#eles:<class 'DrissionPage._elements.session_element.SessionElement'> type
#detail_info(defalut True):when false->only print the content
#return: no return
def html_print(eles,detail_info = True):
    try:
        length = len(eles)
    except:
        print('MESSAGE/html_print:cannot print target ele')

    for i in range(length):
        if(detail_info == True):
            print(eles[i],end='  ')
        print(eles[i].text)


#delete the element in html element list which exist any words in str_list
#input parameter:
#eles:<class 'DrissionPage._elements.session_element.SessionElement'> type
#filter_str_list: target word list you want to search and delete form eles
#return: ele if delete successful, False for delete fail
def delete_eles_by_keyword(eles,filter_str_list):

    length = len(eles)
    if(length == 0):
        print('MESSAGE/delete_eles_by_keyword:empty eles')
        return False

    delete_list = []
    for i in range(length):
        for word in filter_str_list:
            if(word in str(eles[i])):
                delete_list.append(i)
    for i in delete_list[::-1]:
        eles.pop(i)

    return eles

def get_page_title(url):
    page = SessionPage()

    if(page.get(url) == False):
        print('MESSAGE/get_page_content:internet connection timeout')
        return False

    return page.ele("tag=h1").text


#get the web page content by using url
#input parameter:
#url: website url,https...
#filter_str_list:target word list you want to search and delete form ele
#return: one str if success, False if fail
def get_page_content(url,filter_str_list = DEFAULT_STR_FILTER_LIST):
    page = SessionPage()

    if(url == '' or page.get(url) == False):
        print('MESSAGE/get_page_content:internet connection timeout')
        return False

    main_page = page.ele('@data-widget_type:theme-post-content')
    main_page_element_list = main_page.eles('@!id=__ELE_TO_ELES__')
    main_page_element_list = delete_eles_by_keyword(main_page_element_list,filter_str_list)

    length = len(main_page_element_list)

    if(length == 0):
        print('MESSAGE/get_page_content:empty main_page_element_list')
        return False

    content_str = ''
    end_loop = False
    for i in main_page_element_list:
        if(end_loop == True):
            break
        temp = i.texts(True)
        if(temp != []):
            for word in temp:
                content_str += word
                if('FAQs' in word):
                    end_loop = True

    return content_str

if __name__ == '__main__':

    url = "https://projectmanager.com.tw/%e5%b0%88%e6%a1%88%e7%ae%a1%e7%90%86/%e5%b0%88%e6%a1%88%e7%ae%a1%e7%90%86%e6%98%af%e4%bb%80%e9%ba%bc/"
    url2 = "https://projectmanager.com.tw/%e5%b0%88%e6%a1%88%e7%ae%a1%e7%90%86/%e7%94%98%e7%89%b9%e5%9c%96/"
    url3 = "https://projectmanager.com.tw/%e5%b0%88%e6%a1%88%e7%ae%a1%e7%90%86/%e5%b0%88%e6%a1%88%e6%98%af%e4%bb%80%e9%ba%bc/"
    url4 = "https://projectmanager.com.tw/%e5%b0%88%e6%a1%88%e7%ae%a1%e7%90%86%e5%b7%a5%e5%85%b7/notion-%e6%95%99%e5%ad%b8/"
    print(get_page_content(url4))






