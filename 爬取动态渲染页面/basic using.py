from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time


# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('基金')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(ec.presence_of_element_located((By.ID, 'content_left')))
#     # print(browser.current_url)
#     # print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# # 获取网页
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com/')
# page = browser.page_source
# browser.close()
# print(type(page))  # 返回字符串

# # 获取单个节点。
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_a = browser.find_element(By.ID, 'q')
# print(input_first, input_second, input_a, sep='\n')
# browser.close()

# # 获取多个节点。
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# lists = browser.find_elements(By.CLASS_NAME, 'J_Cat')
# # lists = browser.find_elements_by_css_selector('.service-bd li')
# # lists = browser.find_elements_by_css_selector('.service-bd')
# for _ in lists:
#     print(_)
# browser.close()

# # 节点交互
# browser = webdriver.Chrome()
# browser.get('http://taobao.com')
# input = browser.find_element_by_id('q')
# input.send_keys('爬虫')
# time.sleep(1)
# input.clear()
# input.send_keys('赚钱')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# # 动作链
# browser = webdriver.Chrome()
# url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# # 运行JavaScript,有可能selenium没有一些操作。
# browser = webdriver.Chrome()
# browser.get('https://zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# # 获取节点信息。
# browser = webdriver.Chrome()
# browser.get('https://zhihu.com/explore')
# try:
#     logo = browser.find_element_by_class_name('Tabs-link')
#     # logo = browser.find_element_by_id('zh-top-link-logo')
# except exceptions.NoSuchElementException:
#     print('找不到该节点。')
# else:
#     print(logo, logo.get_attribute('href'), sep='\n')  # 获取属性
#     print(logo.text)  # 获取文本
#     print('标签名：{0}  id：{1}  位置：{2} 大小：{3}'.format(logo.tag_name, logo.id, logo.location, logo.size))
# finally:
#     browser.close()

# 选项卡管理
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
new_window = browser.current_window_handle  # 保存现在的window对象。
time.sleep(2)

browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')

# # 前进后退
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')
# browser.get('http://taobao.com')
# browser.back()
# time.sleep(3)
# browser.forward()
# browser.close()

# # 切换frame
# browser = webdriver.Chrome()
# browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# browser.switch_to.frame('iframeResult')  # 输入name值、id值、iframe元素。
# try:
#     logo = browser.find_element_by_class_name('logo')
# except exceptions.NoSuchElementException:
#     print('no such element')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# browser.switch_to.default_content()  # 返回外层iframe
# print(logo, logo.text, sep='\n')

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--headless')
# client = webdriver.Chrome(options=chrome_option)
# client.get('https://www.baidu.com')
# # print(client.page_source)
# print(type(client))
