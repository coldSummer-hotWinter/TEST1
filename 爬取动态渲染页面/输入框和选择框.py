from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://cdn1.python3.vip/files/selenium/test2.html')

# # 选择单选框
# radio_els = browser.find_elements_by_css_selector('#s_radio [name="teacher"]')
# for input_el in radio_els:
#     print(input_el.get_attribute('value'))
# choice_input = radio_els[1]  # 获取目标元素
# choice_input.click()  # 选择目标元素
# browser.close()

# # 选择复选框
# check_box_els = browser.find_elements_by_css_selector('#s_checkbox input[name="teacher"]')
# for check_box_el in check_box_els:
#     # 先将已选的选项清除。
#     if check_box_el.get_attribute('checked') == 'checked':  # 为什么使用默认值不行？？？？
#         check_box_el.click()
#         print('已选的选项清除')
#     if check_box_el.get_attribute('value') == '小雷老师':
#         check_box_el.click()
#
# time.sleep(5)
# print(browser.find_element_by_css_selector('#s_checkbox input[checked="checked"]').get_attribute('value'))
# browser.close()

# select单选框。可以直接获取，不用再创建一个Select类。
select_el = browser.find_element_by_css_selector('#ss_single > option[value="小雷老师"]')
select_el.click()
