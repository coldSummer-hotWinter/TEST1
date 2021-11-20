from bs4 import BeautifulSoup, UnicodeDammit

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

bs = BeautifulSoup(html_doc, 'html.parser')

# HTML文档标准化
# a = bs.prettify()
# print(a)

# 通过方法获取特性值
# for link in bs.find_all('a'):
#     print(link.get('class'))

# 获取元素
# tag = bs.a
# print(tag)

# 获取元素名
# tag = bs.p
# tag_name = tag.name
# print(tag_name)

# 通过属性获取特性值
# href = bs.a['href']
# prine = bs.a['href']
# print(href)
#
# bs.a['href'] = 'http://www.baichi.com'
# print(href)

# 获取内容
# for i in bs.strings:
#     print(i)

# 获取所有的元素
# result = bs.select('p b')
# print(result)

# 编码
dammit = UnicodeDammit('Sacr\xc3\xa9 bleu!')
print(dammit.unicode_markup)
print(dammit.original_encoding)