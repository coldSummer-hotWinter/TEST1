from bs4 import BeautifulSoup
import re

html = '''
<html>
<body>
	<table>
		<tr>
			<th scope="col">first</th>
			<th scope="col">second</th>
			<th scope="col" class="lalala">third</th>
		</tr>
		<tr>
			<th scope="row">拼音: </th>
			<td>zhang</td>
			<td>qin</td>
			<td>hua</td>
		</tr>
	</table>
</body>
</html>'''

# # 测试将HTML文档以字符串形式，传入BeautifulSoup()
# bs = BeautifulSoup(html, 'html.parser')
# results = bs.find_all('th')
# # print(results)
# # print(bs.th['scope'])
#
# for result in results:
#     if 'id' in result.attrs:
#         print(result.attrs['scope'])
#     else:
#         print('查无此特性', result.attrs)

bs = BeautifulSoup(html, 'html.parser')
# print(bs.th.parent, type(bs.th.parent))
for i in bs.th.next_siblings:
    print(i)
