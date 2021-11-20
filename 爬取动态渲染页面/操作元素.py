from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')

# 模拟移动鼠标到目标元素的效果。
actions = ActionChains(browser)
head = browser.find_element_by_css_selector('[name="tj_briicon"]')
actions.move_to_element(head).perform()

time.sleep(5)
browser.close()
