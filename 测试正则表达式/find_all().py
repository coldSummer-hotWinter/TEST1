from urllib import request
from bs4 import BeautifulSoup
import re

# html = request.urlopen('http://www.pythonscraping.com/pages/page3.html')
# print(html.read().decode())  # 为什么使用过read()之后，不能在使用html变量了？

html = request.urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
# images = bs.find_all('img', {'scr': re.compile('\.\.\/img\/gifts\/img\d\.jpg')})
images = bs.find_all('img')  # 将所有img元素提取出来。
results = list()

print(images)
for image in images:
    result = re.match('\.\.\/img\/gifts\/img\d\.jpg', image['src'])  # 根据正则表达式，匹配img的src特性，并返回re.Match对象。
    if result is None:
        continue
    results.append(result.group())  # 即将匹配到的内容提取出来。
print(results)
