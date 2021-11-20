import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0(Intel Mac OS X 10_11_4)AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/52.0.2743.116 Safari/537.36',
            'Host': 'github.com',
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        # response = self.session.get(self.login_url, headers=self.headers)
        # selector = etree.HTML(response.text)
        # token = selector.xpath('//div//input[2]/@value')[0]
        token = 'sddmzu2sHLr14r2XCubaYXf/6sasIfwGgl/p+GVXWD6EP6ruaam0ehEtVn7u+u2EOs0ZDJv8U8GFkbEJ+kPcyQ=='
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'authenticity_token': self.token(),
            'login': email,
            'password': password,
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class="news")]//div[contains(@class="alert")]')
        for item in dynamics:
            dynamic = ' '.format(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//input[@id="user_profile_name"]/option[@value!=""]/text()')
        print(name, email)


if __name__ == '__main__':
    login = Login()
    login.login(email='coldSummer-hotWinter', password='11267017zqh.')