from urllib import request, parse

dic = parse.urlencode({'hello': 'world'})
data = bytes(dic, encoding='utf-8')
response = request.urlopen('http://httpbin.org/post', data=data)
print(type(dic))
print(response.read().decode())