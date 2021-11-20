from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
image_location = bs.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve(image_location, 'logo.jpg')
