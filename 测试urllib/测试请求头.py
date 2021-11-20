from urllib import request, parse

# 直接设置请求头信息
# url = 'http://httpbin.org/post'
#
# headers = {
#     'User-Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org',
#     'user-agent': 'google'
# }
#
# dic = {
#     'name': 'Germey',
#     'age': '1000'
# }
#
# data = bytes(parse.urlencode(dic), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode())
#
# # req = request.Request('http://httpbin.org/get')
# response = request.urlopen(req)
# print(response.read().decode())


# 添加请求头信息
# req = request.Request('http://httpbin.org/post', method='POST')
# req.add_header('Host', 'httpbin.org')
# response = request.urlopen(req)
# print(response.read().decode())


# 测试序列化参数，反序列化参数。
data = 'name=zhangqinhua&age=6666'
dic = parse.parse_qs(data)
t = parse.parse_qsl(data)
print(dic, t, sep='\n')