from DrissionPage import  SessionPage
from package.data.Query_word import Query_Word

DEFAULT_STR_FILTER_LIST = ['nav','ez-toc']
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

    if not main_page:
        return False

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
        temp:str = i.texts(True)
        if(temp != []):
            for word in temp:
                content_str += word.lower()
                if('FAQs' in word):
                    end_loop = True

    return content_str

def get_internal_link(url):
    page = SessionPage()

    if(url == '' or page.get(url) == False):
        print('MESSAGE/get_internal_link:internet connection timeout')
        return [],[]

    main_page = page.ele('@data-widget_type:theme-post-content')
    try:
        found_html_list_1 = main_page.eles('@@href:https://marketer.com.tw@@rel:noopener')
        found_html_list_2 = main_page.eles('@@href:https://websitebuilder.com.tw@@rel:noopener')
        found_html_list_3 = main_page.eles('@@href:https://projectmanager.com.tw@@rel:noopener')

        found_html_list = found_html_list_1 + found_html_list_2 + found_html_list_3

        internal_link_type_list:list[str] = []
        keyword_list_with_internal_link:list[list[str]] = []

        for i in found_html_list:
            if ('go' in i.link):
                continue
            if (i.link not in internal_link_type_list):
                internal_link_type_list.append(i.link)

        for internal_link_type in internal_link_type_list:
            keyword = []
            for found_html in found_html_list:
                if(internal_link_type == found_html.link):
                    keyword.append(found_html.text)
            keyword_list_with_internal_link.append(keyword)
        return internal_link_type_list,keyword_list_with_internal_link

    except Exception:
        return [],[]






