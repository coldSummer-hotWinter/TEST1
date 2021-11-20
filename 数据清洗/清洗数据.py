from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_n_gram(content, n):
    content = content.split(' ')
    output = list()
    for i in range(len(content) - n + 1):
        output.append(content[i: i+n])
    return output


html = urlopen('https://pypi.org/')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('title').get_text()
ngrams = get_n_gram(content, 2)
print('title is: '+content)
print('2-grams is: ', ngrams)
print('2-grams count is: '+str(len(ngrams)))
