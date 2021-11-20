import requests
import re

# # 基本请求
# r = requests.get('http://httpbin.org/get')
# print(r.text)

# # 添加参数再请求
# dic = {
#     'name': 'mr.zhang',
#     'age': '0',
#     '国际': '玩笑',
# }
# r = requests.get('http://httpbin.org/get', params=dic)
# print(type(r.text))
# print(r.json())

# # 抓取网页
# head = {
#     'user-agent': 'Mozilla/5.0(Intel Mac OS X 10_11_4)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore', headers=head)
# # pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# pattern = 'explore-feed.*?question_link.*?>(.*?)</a>'
# titles = re.findall(pattern, r.text)
# print(titles)
# print(r.text)


# r = requests.get('http://www.qiman5.com/images/logo.png')
# # print(r.text)
# # print(r.content)
# with open('favicon.png', 'wb') as file:
#     file.write(r.content)


# # 使用post请求，添加form。
# dic = {
#     'name': 'mr.zhang',
#     'age': '0',
#     '国际': '玩笑',
# }
# r = requests.post('http://httpbin.org/post', data=dic)
# print(r.text)
# print(r.content)


# head = {
#     'user-agent': 'Mozilla/5.0(Intel Mac OS X 10_11_4)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# url = 'https://www.csdn.net/'
# # url = 'http://www.jianshu.com'
# html = requests.get(url, headers=head)
# if html.status_code == requests.codes.not_found:
#     print('找不到网页')
# else:
#     print(html.status_code)
#     print(html.cookies)
#     print(html.url)
#     print(html.headers)
