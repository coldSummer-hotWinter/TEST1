from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv


def entry(browser, user, password):
    """登陆账号"""
    user_name = browser.find_element_by_id('username')
    pass_word = browser.find_element_by_id('password')
    login = browser.find_element_by_css_selector('[name="login"]')
    user_name.send_keys(user)
    pass_word.send_keys(password)
    login.click()


def health_information_reporting_interface(browser):
    """进入健康信息填报界面"""
    first_frame = browser.find_element_by_xpath('//div[@id="mini-17$body$3"]/iframe')
    browser.switch_to.frame(first_frame)
    browser.switch_to.frame(3)
    img = browser.find_element_by_css_selector('[title="校内学生每日健康信息填报"]')
    img.click()


def report_information(browser):
    try:
        browser.switch_to.default_content()
        time.sleep(3)
        frame_el = browser.find_element_by_css_selector('.mini-panel-body iframe')
        browser.switch_to.frame(frame_el)
        time.sleep(3)
        el = browser.find_element_by_id('messageId')
    except NoSuchElementException:
        print('今天未填报，正在填报中。')

        # 转换frame
        browser.switch_to.parent_frame()
        frame1 = browser.find_element_by_xpath('//div[@id="mini-17$body$6"]/iframe')
        browser.switch_to.frame(frame1)
        frame2 = browser.find_element_by_xpath('//div[@id="mini-14$body$2"]/iframe')
        browser.switch_to.frame(frame2)
        time.sleep(4)

        # 第一部分填报
        el_span = browser.find_element_by_xpath('//span[@id="DRSTZK"]//span[@class="mini-buttonedit-icon"]')
        el_span.click()
        el_td = browser.find_element_by_xpath('//tr[@id="mini-15$0"]/td[@style]')
        el_td.click()
        el_label = browser.find_element_by_xpath('//div[@id="mini-19$1"]/label')
        el_label.click()

        # 第二部分填报，上午地点、时间
        el_SWDD = browser.find_element_by_xpath('//div[@id="toolbar_SWDD"]//span')
        el_SWDD.click()
        time.sleep(1)
        el_div_place = browser.find_element_by_xpath('//td[@id="1$cell$2"]/div')  # 地点
        el_div_place.click()
        el_input = browser.find_element_by_xpath('//span[@id="mini-190"]//input')
        el_input.send_keys('宿舍1-10栋')

        el_div_time = browser.find_element_by_xpath('//td[@id="1$cell$3"]/div')  # 时间
        el_div_time.click()
        time.sleep(2)
        el_input_time = browser.find_element_by_css_selector('#mini-193 > span > span > span.mini-buttonedit-button > span')
        el_input_time.click()
        time.sleep(1)
        el_data = browser.find_element_by_css_selector(
            '#mini-4 > tbody > tr:nth-child(2) > td > div > span:nth-child(2)')
        el_data.click()

        # 第二部分填报，中午地点
        el_ZWDD = browser.find_element_by_xpath('//div[@id="toolbar_ZWDD"]//span')
        el_ZWDD.click()
        time.sleep(1)
        el_div = browser.find_element_by_xpath('//td[@id="2$cell$5"]/div')
        el_div.click()
        el_input = browser.find_element_by_css_selector('#mini-195 > span > input')
        el_input.send_keys('宿舍1-10栋')

        # 第二部分填报，下午地点
        el_XWDD = browser.find_element_by_xpath('//div[@id="toolbar_XWDD"]//span')
        el_XWDD.click()
        time.sleep(1)
        el_div = browser.find_element_by_xpath('//td[@id="3$cell$8"]/div')
        el_div.click()
        el_input = browser.find_element_by_xpath('//span[@id="mini-198"]//input')
        el_input.send_keys('宿舍1-10栋')

        # 第二部分填报，晚上地点
        el_HTBD059F = browser.find_element_by_xpath('//div[@id="toolbar_HTBD059F"]//span')
        el_HTBD059F.click()
        time.sleep(1)
        el_div = browser.find_element_by_xpath('//td[@id="4$cell$11"]/div')
        el_div.click()
        el_input = browser.find_element_by_xpath('//span[@id="mini-201"]//input')
        el_input.send_keys('宿舍1-10栋')

        # 第三部分
        el_eat_place1 = browser.find_element_by_id('HT11E434$text')
        el_eat_place2 = browser.find_element_by_id('HTDD18DB$text')
        el_eat_place3 = browser.find_element_by_id('WCCZH$text')

        el_eat_place1.click()
        el_eat_place1.send_keys('无')
        el_eat_place2.send_keys('无')
        el_eat_place3.send_keys('无')

        # 提交信息
        submit_information(browser)
    else:
        print('今天已填报。')
        browser.close()


def submit_information(browser):
    """提交信息"""
    browser.switch_to.default_content()
    frame1 = browser.find_element_by_xpath('//div[@id="mini-17$body$6"]/iframe')
    browser.switch_to.frame(frame1)

    submit_el = browser.find_element_by_id('sendBtn')
    submit_el.click()
    sure_el = browser.find_element_by_css_selector('#mini-17 span')
    sure_el.click()
    print('成功提交信息。')


def run(user, password):
    browser = webdriver.Chrome()
    browser.get('https://i.njcit.cn/EIP/user/index.htm')

    # 登陆南信院的账号
    entry(browser, user, password)
    time.sleep(3)

    # 进入填报界面
    health_information_reporting_interface(browser)
    time.sleep(3)

    # 填报信息
    report_information(browser)


def main():
    with open('账号信息.csv', 'r') as file:
        reader = csv.reader(file)
        for i in reader:
            run(i[0], i[1])
            time.sleep(1)


if __name__ == '__main__':
    main()
