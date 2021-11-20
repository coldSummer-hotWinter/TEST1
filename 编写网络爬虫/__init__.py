from bs4 import BeautifulSoup
from urllib import request

# html = '''
# <html>
#     <body>
#         <p> lalla </p>
#         <p></p>
#         <p> haha </p>
#     </body>
# </html>
# '''
#
# bs = BeautifulSoup(html, 'html.parser')
# results = bs.find_all('p')
#
# print(len(results))
# for result in results:
#     print(result.get_text())
    # if result.get_text() is None:
    #     print('haven‘t text')
    # else:
    #     print(result.get_text())

html = request.urlopen('http://www.shuquge.com/txt/5809/32512977.html')
print(html.read())
