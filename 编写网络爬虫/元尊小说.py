from bs4 import BeautifulSoup
from urllib import request
import re


def getContent(url_para):
    global chapters
    # 获取响应
    html = request.urlopen(url_para)

    # 提取当前章节
    bs = BeautifulSoup(html, 'html.parser')
    # 提取章节名
    name = bs.find('div', {'id': 'BookCon'}).h1.get_text()
    chapter = name + '\n\n'
    # 提取章节内容
    p_elements = bs.find_all('p')
    for p_element in p_elements:
        if 'class' in p_element.attrs:
            break
        if p_element.get_text() is not None:
            chapter += p_element.get_text()+'\n'
    chapters.append(chapter)
    #  提取下一章的链接
    url_next = getNextPage(bs)
    urls.append(url_next)
    if url_next is not None:
        getContent(url_next)
    else:
        if len(urls) > 1:
            print('爬到最后一章，链接是 ' + urls[-2])
        else:
            print('暂无更新')


def getNextPage(bs):
    next_page = bs.find('a', {'rel': 'next'})

    if next_page is None:
        return None
    elif next_page.get_text() == '下一章':
        next_href = 'http://www.ishisetianxia.com' + next_page.attrs['href']
        return next_href


def saveFile(contents):
    chapter_num = 1
    for content in contents:
        chapter_name_regex = '.*?\s(.*?)\n\n'
        chapter_name = re.search(chapter_name_regex, content)
        file_path = '元尊小说集/{0}{1}'.format(chapter_num, chapter_name.group(1))
        file_name = file_path + '.txt'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)

        chapter_num += 1


chapters = list()
urls = list()
# 提取章节
getContent('http://www.ishisetianxia.com/xs/28354.html')
# 保存文件
saveFile(chapters)
