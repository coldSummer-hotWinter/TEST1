from urllib import request, parse
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'host': 'm.weibo.cn',
    'referer': 'https://m.weibo.cn/u/2830678474',
    'user-agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
    'x-requested-with': 'XMLHttpRequest',
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1005052830678474',
        'page': page,
    }
    url = base_url + parse.urlencode(params)
    print(url)
    req = requests.get(url, headers=headers)
    print(req.json())
    for i in req.json():
        print(i)


# def parse_page(json):

get_page(1)