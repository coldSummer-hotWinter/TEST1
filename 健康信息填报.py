from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def entry(browser):
    """登陆账号"""
    user_name = browser.find_element_by_id('username')
    pass_word = browser.find_element_by_id('password')
    login = browser.find_element_by_css_selector('[name="login"]')
    user_name.send_keys('190410217')
    pass_word.send_keys('11267017zqh.')
    login.click()


def health_information_reporting_interface(browser):
    """进入健康信息填报界面"""
    first_frame = browser.find_element_by_xpath('//div[@id="mini-17$body$3"]/iframe')
    browser.switch_to.frame(first_frame)
    browser.switch_to.frame(3)
    img = browser.find_element_by_tag_name('img')
    img.click()


def report_information(browser):
    """输入填报的信息"""
    def whether_report(browser1):
        """判断是否填报过了"""
        try:
            prompt_el = browser1.find_element_by_id('mini-16$content')
        except NoSuchElementException:
            print('今天未填报，正在填报中。')
        else:
            print('今天已填报。')
            exit()

    # 转换到相应的frame。
    browser.switch_to.default_content()
    first_frame = browser.find_element_by_xpath('//div[@id="mini-17$body$6"]/iframe')
    browser.switch_to.frame(first_frame)
    whether_report(browser)
    second_frame = browser.find_element_by_xpath('//div[@id="mini-14$body$2"]/iframe')
    browser.switch_to.frame(second_frame)

    # 获取要填报的信息元素。
    province_el = browser.find_element_by_id('XZHS$text')
    city_el = browser.find_element_by_id('XZHSS$text')
    county_el = browser.find_element_by_id('XZHQ$text')
    radio_els = browser.find_elements_by_xpath('//div[@index="1"]/input[@type="radio"]')

    # 输入填报信息。
    province_el.send_keys('江苏省\n')
    time.sleep(1)
    city_el.send_keys('徐州市\n')
    time.sleep(1)
    county_el.send_keys('睢宁县')
    county_el.click()
    time.sleep(1)
    for radio_el in radio_els:
        radio_el.click()


def submit_information(browser):
    """提交信息"""
    browser.switch_to.parent_frame()
    submit_el = browser.find_element_by_id('sendBtn')
    submit_el.click()
    sure_el = browser.find_element_by_css_selector('#mini-17 span')
    sure_el.click()
    print('成功提交信息。')


def main():
    # 创建WebDriver对象。
    # option = webdriver.ChromeOptions()
    # option.add_argument('--headless')
    # browser = webdriver.Chrome(options=option)
    browser = webdriver.Chrome()
    browser.get('https://i.njcit.cn/EIP/user/index.htm')

    # 登陆南信院的账号
    entry(browser)
    time.sleep(3)

    # 进入填报界面
    health_information_reporting_interface(browser)
    time.sleep(3)

    # 填报信息
    report_information(browser)

    # 提交信息
    submit_information(browser)


if __name__ == '__main__':
    main()
