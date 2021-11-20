import csv
from bs4 import BeautifulSoup


# # 必须先读取html文件！！！！
# with open('test_table.html', 'r', encoding='utf-8') as file:
#     content = file.read()
#
# bs = BeautifulSoup(content, 'html.parser')
# table = bs.find('table')
# rows = table.find_all('tr')
#
# csv_file = open('editors.csv', 'w+', encoding='utf-8')
# writer = csv.writer(csv_file)
# try:
#     for row in rows:
#         csv_row = []
#         for cell in row.find_all(['td', 'th']):
#             csv_row.append(cell.get_text())
#         writer.writerow(csv_row)
# finally:
#     csv_file.close()


# # 通过列表写入数据
# data = ['zhang', '二狗子', '狗腿子', '二愣子']
# datas = [['zhang', 8], ['二狗子', 90], ['狗腿子', 20], ['二愣子', 65]]
# with open('datas.csv', 'w', encoding='utf-8', newline='') as file:
#     write = csv.writer(file)
#     write.writerows(datas)


# # 通过字典写入数据
# with open('datas1.csv', 'w', encoding='utf-8', newline='') as file:
#     head = ['id', 'name', 'age']
#     writer = csv.DictWriter(file, fieldnames=head)
#     writer.writeheader()
#     writer.writerow({'id': '张', 'name': '001', 'age': '98'})


# 读取数据
with open('datas.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    print(reader)
    for i in enumerate(reader):
        print(i)