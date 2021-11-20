from selenium import webdriver
import time

browser = webdriver.Chrome()

# # \n 相当于按下回车。
# browser.get('https://www.baidu.com')
# input_el = browser.find_element_by_id('kw')
# input_el.send_keys('魅族\n')
#
# browser.get('http://www.qiman5.com')
# input_el = browser.find_element_by_id('searchtxt')
# input_el.send_keys('元尊\n')

# # 通过WebElement对象，选择元素。
# browser.get('https://www.baidu.com')
# # time.sleep(10)
# browser.implicitly_wait(3)
# input_el = browser.find_element_by_id('s_kw_wrap')
# input_texts = input_el.find_elements_by_tag_name('a')
# for text in input_texts:
#     print(text.text, text.get_attribute('href'))
# browser.close()

# # 通过属性获取元素。
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# input_el = browser.find_element_by_css_selector('[name="wd"]')
# print(input_el.get_attribute('name'))
# browser.close()

# # 通过和,增加多个获取条件。
# browser.get('https://www.baidu.com')
# input_el = browser.find_elements_by_css_selector('[name="rsv_spt"],[name="f"]')
# for _ in input_el:
#     print(_.get_attribute('type'))

# # 根据子元素在父元素里的顺序，获取子元素。
# browser.get('https://www.baidu.com')
# time.sleep(3)
# input_el = browser.find_elements_by_css_selector('a:nth-child(6)')
# for _ in input_el:
#     print(_, _.text, _.get_attribute('href'))
# browser.close()

# 通过波浪线、+，获取兄弟元素。
browser.get('https://www.baidu.com')
# el = browser.find_element_by_css_selector('#form input:nth-child(3)')
# browser.implicitly_wait(3)
time.sleep(3)
# el = browser.find_element_by_css_selector('#s_kw_wrap')
els = browser.find_elements_by_tag_name('span')
for _ in els:
    i = _.get_attribute('id')
    k = _.get_attribute('class')
    if i:
        print(i, k)
    else:
        print('2')
browser.close()
