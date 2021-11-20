import bs4
import requests
import re

html = requests.get('http://72.itmc.org.cn:80/JS001/open/show/zhaopin/index.html').content.decode('utf-8')
bs = bs4.BeautifulSoup(html, 'html.parser')
li_s = bs.select('#s_position_list .item_con_list li')

results = list()
for li in li_s:
    result = list()
    # 获取职位名
    position_name = li.h3.string
    result.append(position_name)
    # 获取薪水
    money = li['data-salary']
    money = re.match('(.*?)-', money).group(1)
    result.append(money)
    # 获取学历
    xue_li = li.find(name='div', attrs={'class': 'li_b_l'}).text[-4:-2]
    result.append(xue_li)
    # 获取公司名
    company_name = li['data-company']
    result.append(company_name)
    # 获取地点
    address = li.find(name='em').string
    address = re.match('(.*?)·', address).group(1)
    result.append(address)

    results.append(result)

for result in results:
    print(result)