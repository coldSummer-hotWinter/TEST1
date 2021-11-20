from urllib import request

# text_page = request.urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
text_page = request.urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
content = text_page.read().decode('utf-8')
print(content)
