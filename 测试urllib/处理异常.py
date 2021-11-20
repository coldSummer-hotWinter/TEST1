from urllib import request, error

try:
    # response = request.urlopen('https://cuiqingcai.com/index.html')
    response = request.urlopen('http://www.baidu.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print(response.reason)
    for head in response.getheaders():
        print(head)
