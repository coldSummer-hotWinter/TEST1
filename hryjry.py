# import pandas as pd
#
# values = {
#     'word': ['a', 'b', 'd', 'e', 'f', 'k', 'd', 's', 'l'],
#     'num': [1, 5, 7, 6, 9, 3, 4, 5, 1]
# }
# index = [
#     ['A', 'A', 'A', 'C', 'C', 'C', 'B', 'B', 'B'],
#     [1, 3, 2, 5, 2, 7, 9, 12, 6]
# ]
# d = pd.DataFrame(values, index)
# # d1 = d.sort_index(key='num')
# d1 = d.sort_values(by='num')
# print(d)
# print(d1)


import requests, bs4, re


def job_find(company):
    # 从此处开始编写代码
    results = []
    for i in range(1, 5):
        if i == 1:
            html = requests.get('http://72.itmc.org.cn:80/JS001/open/show/zhaopin/index.html').content.decode('utf-8')
        else:
            html = requests.get(
                'http://72.itmc.org.cn:80/JS001/open/show/zhaopin/index_{}.html'.format(i)).content.decode('utf-8')
        bs = bs4.BeautifulSoup(html, 'html.parser')
        li_s = bs.select('.item_con_list li')
        for li in li_s:
            company_name = li['data-company']
            position = li.find(name='em').string
            position = re.match('(.*?)·', position).group(1)
            results.append((company_name, position))

    count = 0
    for result in results:
        if company == result[0] and '北京' == result[1]:
            count += 1

    return count


print(job_find('字节跳动'))
# import requests, re, bs4
#
#
# def job_find(company: str) -> int:
#     # 从此处开始编写代码
#     index = 0
#     list_name1 = []
#     list_name2 = []
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#     for i in range(5):
#         if i == 1:
#             html = requests.get('http://72.itmc.org.cn/JS001/open/show/zhaopin/index.html', headers=headers).content.decode('utf-8')
#         else:
#             html = requests.get('http://72.itmc.org.cn/JS001/open/show/zhaopin/index_{}.html'.format(i),
#                                 headers=headers).content.decode('utf-8')
#
#         soup = bs4.BeautifulSoup(html, 'html.parser')
#         for k in soup.find_all(name='a', attrs={'data-lg-tj-id': "8F00"}):
#             list_name1.append(k.string)
#         for j in soup.find_all(name='span', attrs={'class': 'add'}):
#             list_name2.append(j.text[1:3])
#     for k in range(len(list_name1)):
#         if list_name1[k] == company and list_name2[k] == '北京':
#             index += 1
#     return index
#
#
# print(job_find('字节跳动'))
