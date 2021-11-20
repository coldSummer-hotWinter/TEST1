from urllib import request, parse, error
from bs4 import BeautifulSoup
import json
import re
# 爬虫如何适时的写异常


def get_page():
    """
        通过搜索，获取漫画的页面。
    """
    # 获取搜所的漫画名和链接。
    def search_cartoon():
        cartoon_name = parse.quote(input('输入漫画名'))
        search_url = 'http://www.qiman5.com/search.php?keyword=' + cartoon_name
        try:
            html = request.urlopen(search_url)
        except TimeoutError:
            print('超时了，请检查网络问题')
            exit()
        except error.URLError as e:
            print(e.reason)
            exit()
        bs = BeautifulSoup(html, 'html.parser')
        tags = bs.select('.title')
        search_results = list()
        for tag in tags:
            cartoon_name = tag.a['title']
            cartoon_url = 'http://www.qiman5.com' + tag.a['href']
            search_result = {cartoon_name: cartoon_url}
            search_results.append(search_result)
        return search_results

    # 显示搜索漫画名和链接，并选择要求的漫画。
    def show_search_results(messages):
        for index, message in enumerate(messages):
            print('编号：{0}  漫画名： {1}'.format(index + 1, *message.keys()))
        while True:
            index = int(input('请输入编号')) - 1
            if 0 <= index <= len(messages) and index != int:
                break
            else:
                print('不按要求输入编号。请重输入')
        url = messages[index].values()
        html = request.urlopen(*url)
        bs = BeautifulSoup(html, 'html.parser')
        return bs

    msgs = search_cartoon()
    cartoon_page = show_search_results(msgs)
    return cartoon_page


def handle_page(data):
    """
        提取页面的信息，有漫画名、章节名、章节链接。
    """
    # 提取漫画的名字。
    title_tag = data.find('title').get_text()
    cartoon_name = re.match('(.*?)_.*', title_tag).group(1)

    # 获取漫画的章节名、章节链接。
    tags = data.select('#chapter-list1 .ib')
    if tags:
        results = list()
        for tag in tags:
            chapter_name = tag.get_text()
            chapter_url = 'http://www.qiman5.com' + tag['href']
            result = {chapter_name: chapter_url}
            results.append(result)
    else:
        print('没有章节内容')
        exit()
    return cartoon_name, results


def choice_output(name, data):
    def save_data(msgs):
        save_path = '漫画集中营/{0}{1}'.format(name, '.json')
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(msgs, indent=2, ensure_ascii=False))

    def show_data(msgs):
        for msg in msgs:
            print('链接：{1}\t章节名：{0}'.format(*msg.keys(), *msg.values()))

    while True:
        choice = input('仅保存选a, 仅显示选b, 保存和显示选c')
        if choice in ['a', 'b', 'c']:
            break
        else:
            print('不符合要求,请按要求输入')

    if choice == 'a':
        save_data(data)
    elif choice == 'b':
        show_data(data)
    elif choice == 'c':
        save_data(data)
        show_data(data)


def main():
    page = get_page()
    chap_name, handled_data = handle_page(page)
    choice_output(chap_name, handled_data)


if __name__ == '__main__':
    main()
