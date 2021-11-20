import requests
from urllib import parse


def get_page(offset):
    params = {
        'offset': 'offset',
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
    }
    url = 'http://toubao.com/search_content/?'+parse.urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None