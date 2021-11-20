import requests,bs4,re

html = requests.get('http://72.itmc.org.cn:80/JS001/open/show/zhaopin/index.html').content.decode('utf-8')
bs = bs4.BeautifulSoup(html, 'html.parser')
li_s = bs.select('#s_position_list ul li')
results = list()
for li in li_s:
    company = li['data-company']
    address = li.find(name='em').string
    address = re.match('(.*?)·', address).group(1)
    results.append((company, address))

count = 0
for result in results:
    if ('北京' in result) and ('字节跳动' in result):
        count += 1

print(count)
