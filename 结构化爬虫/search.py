from urllib import request
from bs4 import BeautifulSoup


def get_link(topic):
    url = 'https://pypi.org/search/?q={}'.format(topic)
    html = request.urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find_all('a')


links = get_link('requests')
if links is not None:
    for link in links:
        if 'href' in link.attrs:
            print(link.attrs['href'], link.get_text())