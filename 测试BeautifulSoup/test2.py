from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

bs = BeautifulSoup(html, 'html.parser')
# name = bs.find_all('span', {'class': 'green'})
name = bs.find('span').next_siblings
# name = bs.find_all('span', {'class': 'green'}, recursive=True)
# name = bs.find_all(text='Prince Vasili Kuragin')   #换行符影响
# name = bs.find_all('span', {'class': 'green'}, recursive=True, limit=3)
# name = bs.find_all(class_='green')


for _ in name:
    print(_)

