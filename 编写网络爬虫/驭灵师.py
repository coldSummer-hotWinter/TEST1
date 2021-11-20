from urllib import request
from bs4 import BeautifulSoup
import re
import json


def getContent(url_para):
    global content

    html = request.urlopen(url_para)
    bs = BeautifulSoup(html, 'html.parser')

    # 提取话的名字
    title = bs.find('title').get_text()  #
    regex = '(.*?)\s-\s奇漫屋'
    name = re.match(regex, title).group(1)
    content[name] = url_para

    # 提取下一话的链接
    next = bs.find('a', {'id': 'mainControlNext'})
    if next is not None:
        if 'href' in next.attrs:  #
            url_next = 'http://www.qiman5.com' + next.attrs['href']
            getContent(url_next)


content = dict()
getContent('http://www.qiman5.com/15762/1098437.html#page_18')
with open('save_caricature.json', 'w', encoding='utf-8') as file:
    json.dump(content, file)
