from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)
browser.get('http://cdn1.python3.vip/files/selenium/test1.html')

# # 通过标签名选择元素。
# p_els = browser.find_elements_by_xpath('//div/p')
# for p in p_els:
#     print(p.text)


# # 通过属性选择元素。
# span_el = browser.find_element_by_xpath('//*[@id="newyork"]')  # 通过id特性，*代表任意的标签。
# print(span_el.text)
#
# p_el = browser.find_element_by_xpath('//*[@class="capital huge-city"]')  # 通过class特性，必须是全部的class特性值。
# print(p_el.text)
#
# link_els = browser.find_elements_by_xpath('//option[starts-with(@value, "小")]')  # 通过特性值的内容。
# for el in link_els:
#     print(el.text)

option_els = browser.find_elements_by_xpath('//select/option[3]')
for el in option_els:
    print(el.text)
browser.close()
