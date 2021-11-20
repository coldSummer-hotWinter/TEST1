from bs4 import BeautifulSoup
from urllib import request


url = 'https://www.zhihu.com/explore'
html = request.urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
# results = bs.select('.explore-tab .feed-item ExploreHomePage-specials')
results = bs.select('a')
print(results)
# for result in results:
#     question = result.find('h2').get_text()
#     author = result.find(class_='.author-link-line').get_text()
#     answer = result.find(class_='.content').get_text()
#     print(author, answer, question)
    # with open('zhihu.txt', 'w', encoding='utf-8') as file:
    #     content = '\n'.join([question, author, answer])
    #     seq = '\n'+'='*25+'\n'
    #     file.write(content)
    #     file.write(seq)



