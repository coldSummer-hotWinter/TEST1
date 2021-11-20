import re
import pandas as pd

# content = 'Hello 123 4567 World_this is'
# regex = '^Hello\s\d{3}\s\d{4}\s\w{10}\sis$'
# result = re.match(regex, content)
# print(result.group())
# print(result.span())
# print(type(result))

# content = 'Hello 1234567 World_this is'
# regex = '^Hello\s(\d+)\s(World)'
# result = re.match(regex, content)
# print(result.group(2))

# content = 'Hello 123 4567 World_this is a Demo'
# regex = '^Hello.*[a]'
# pattern = re.compile(regex)
# result = re.match(pattern, content)
# print(result.group())
# print(type(result))


chipo = pd.read_csv('data.csv', sep=',')


def sales_max():
    global chipo
    # 获取相应列
    name_s = chipo['item_name']
    quantity_s = chipo['quantity']
    price_s = chipo['item_price']
    # 从item_price提取单价，计算总价

    results = []
    for index, price in enumerate(price_s):
        price = eval(price[1:])
        quantity = quantity_s[index]
        total_price = price * quantity
        item_name = name_s[index]
        results.append((item_name, total_price))

    item_names = []
    total_sum = []
    for name in name_s:
        sum = 0
        if name not in item_names:
            for el in results:
                if name == el[0]:
                    sum += el[1]
            item_names.append(name)
            total_sum.append(sum)
    max_total_price = max(total_sum)
    max_index = total_sum.index(max_total_price)
    return item_names[max_index]


print(sales_max())

