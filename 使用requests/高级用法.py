import requests
from urllib import request
from bs4 import BeautifulSoup
import re


# files = {'file': open('favicon.png', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)


# #cookies登陆
# head = {
#     'user-agent': 'Mozilla/5.0(Intel Mac OS X 10_11_4)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
#     # 'cookies': 'uuid_tt_dd=10_37481726760-1595382881575-118718; dc_session_id=10_1595382881575.927340; __gads=ID=b1da2447cb0d46dd:T=1595751290:S=ALNI_MYN_ljOETePLg1aDx9aF_Poezzd2w; Hm_lvt_c6819c09822e270229a7413a6be67a55=1595753004; Hm_up_c6819c09822e270229a7413a6be67a55=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; Hm_ct_c6819c09822e270229a7413a6be67a55=6525*1*10_37481726760-1595382881575-118718; UserName=qq_47175528; UserInfo=6affa5c502ee4a2a8b6fcc5de17fe3ba; UserToken=6affa5c502ee4a2a8b6fcc5de17fe3ba; UserNick=%E6%B1%BD%E6%B0%B4%E9%85%8D%E8%BE%A3%E6%9D%A1; AU=025; UN=qq_47175528; BT=1596073900943; p_uid=U000000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_47175528%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_37481726760-1595382881575-118718!5744*1*qq_47175528; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Flive.csdn.net%252Froom%252Fyzkskaka%252FwgOUuuyi%253Futm_source%253D1546214907%2522%252C%2522announcementCount%2522%253A0%257D; log_Id_pv=5; log_Id_view=10; log_Id_click=2; Hm_up_facf15707d34a73694bf5c0d571a4a72=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_47175528%22%2C%22scope%22%3A1%7D%7D; Hm_ct_facf15707d34a73694bf5c0d571a4a72=5744*1*qq_47175528!6525*1*10_37481726760-1595382881575-118718; dc_sid=3f420ead55f389ba97fa58e5f59f62c6; c_first_ref=default; c_first_page=https%3A//www.csdn.net/; c_segment=14; Hm_lvt_facf15707d34a73694bf5c0d571a4a72=1596684003,1596698796; Hm_lpvt_facf15707d34a73694bf5c0d571a4a72=1596698796; TY_SESSION_ID=86822656-6520-431a-b2fb-76400ac2f368; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1595751236,1595753004,1596073735,1596698816; c_page_id=https%3A//blog.csdn.net/qq_47175528; dc_tos=qemsr9; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1596698904'
# }
# req = requests.get('https://blog.csdn.net/qq_47175528', headers=head)
# html = req.text
# links = re.findall('<a.*?>.*?</a>', html, re.S)
# print(req.cookies)
# for link in links:
#     print(link)


# # 会话维持，不同的会话
# requests.get('http://httpbin.org/cookies/set/number/120')
# req = requests.get('http://httpbin.org/cookies')
# print(req.text)
#
# # 会话维持，一样的会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/120')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# # ssl证书验证
# req = requests.get('http://www.12306.cn', verify=False)
# print(req.text)


# # 代理设置
# proxies = {
#     'http': 'http://user:password@10.10.1.10:3128'
# }
# req = requests.get('https://www.taobao.com', proxies=proxies)
# print(req.text)


# # 超时设置
# r = requests.get('https://taobao.com', timeout=0.1)


# 身份验证
# r = requests.get('http://localhost:5000', auth=('user_name', 'password'))
# print(r.text)


# prepared request
url = 'http://httpbin.org/post'
head = {
    'user-agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
}
data = {
    'name': 'liuliuliu',
    'nation': 'china',
}
req = requests.Request('POST', url=url, headers=head, data=data)
s = requests.Session()
prepared = s.prepare_request(req)
r = s.send(prepared)
print(r.text)
