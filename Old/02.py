import requests
import re
import requests.packages.urllib3


def close_message():
        requests.packages.urllib3.disable_warnings()
# url='https://www.taichung.gov.tw/10179/12034/'

def connect_website(url):

    html = requests.get(url, verify=False).text

    regex04a = r'\(\d{2}\)\d{4}-?\d{4}' #區域號碼2位 4位 可以沒有'-' 取4位
    regex04b = r'\d{2}-\d{4}-?d{4}'
    regex0800 = r'0800-\d{6}'

    result = re.findall(regex04a, html)
    result += re.findall(regex04b, html)
    result += re.findall(regex0800, html)

    return result


if __name__ ==  "__main__":

    url = 'https://www.taichung.gov.tw/10179/12034/'

    close_message()
    result = connect_website(url)

    for tel in result:
        print(tel)



# 常用的正則表示式
#     . : 任意字元
#     \d: 0~9
#     \D: 非0~9
#     \s: \t, \n, \f, \r, \x0B
#     \S: 非\t, \n, \f, \r, \x0B
#     \w: a~z, A~Z, 0~9
#     \b: 英文單字的邊界
#     \B: 非英文單字的邊界
# ================================
#     x?      :x出現0~1次 (先採用1個，再用0個)
#     x*      :x出現0~n次 (先採用n個，再次用n-1個,...)