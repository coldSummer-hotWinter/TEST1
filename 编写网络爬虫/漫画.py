from urllib import request
from bs4 import BeautifulSoup
import re

results = dict()


def getHTML(url_para):
    global results
    # 获取HTML文档
    html = request.urlopen(url_para)

    # 提取数据
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('title').get_text()
    # 提取标题
    regex = '(.*?)\s-\s奇漫屋'
    clear_title = re.match(regex, title).group(1)
    print(1)
    results[clear_title] = url_para
    # 提取下页的链接
    link_next = bs.find('a', {'class': 'main_control_next'})

    try:
        url_next = 'http://www.qiman5.com' + link_next['href']
    except TypeError:
        pass
    else:
        # 进行下次提取
        getHTML(url_next)


getHTML('http://www.qiman5.com/15762/1149592.html')

for name, url in results.items():
    print(name, url)
