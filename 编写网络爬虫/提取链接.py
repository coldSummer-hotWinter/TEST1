from urllib import request
from bs4 import BeautifulSoup
import re

url = 'https://baike.baidu.com/item/%E5%87%AF%E6%96%87%C2%B7%E8%B4%9D%E8%82%AF/2728128?fromtitle=Kevin%20Bacon&fromid=4226999&fr=aladdin '
html = request.urlopen(url)

bs_html = BeautifulSoup(html, 'html.parser')
links = bs_html.find_all('a')


content = dict()
for link in links:
    regex = '[http|https].*'

    # 若访问元素里没有的特性，就会报错。应跳过。
    try:
        href = link['href']  # 访问元素里的属性，要用中括号，里面输入属性的字符串形式。
    except KeyError:
        continue
    http = re.match(regex, href, re.S)
    # 若特性值不符合匹配，返回None。应该跳过。
    if http is not None:
        content[http.group()] = link.get_text()


for key, value in content.items():
    print(key, value)

