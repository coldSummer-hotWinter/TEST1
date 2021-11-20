from urllib import parse

# test urlparse()
# result = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result, sep='\n')
# print(result[0], result.scheme)


# test urlunparse()
# url = ('http', 'www.baidu.com', '/index.html', 'user', 'id=5', 'comment')
# result = parse.urlunparse(url)
# print(type(result), result, sep='\n')

# test urlsplit()
# result = parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result, sep='\n')

# test urlunsplit()
# url = ('http', 'www.baidu.com', '/index.html', 'id=5', 'comment')
# result = parse.urlunsplit(url)
# print(type(result), result, sep='\n')

# test urljoin()
# print(parse.urljoin('http://baidu.com', 'FAQ.html'))
# print(parse.urljoin('http://baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# print(parse.urljoin('www.baidu.com', '?category=2#comment'))

# test urlencode()
# params = {'name': 'germany', 'age': '26'}
# base_url = 'http://baidu.com?'
# print(base_url, parse.urlencode(params), sep='')

# test parse_qs()
# url_params = 'name=germany&age=26'
# print(parse.parse_qs(url_params))

# test parse_qsl()
# url_params = 'name=germany&age=26'
# print(parse.parse_qsl(url_params))

# test quote()、unquote()
# url = 'http://baidu.com?wd='+parse.quote('壁纸')
# print(url)
# print(parse.unquote(url))


from urllib import robotparser, request
# test RobotFileParser()
# rp = robotparser.RobotFileParser()
# rp.parse(request.urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
# print(rp.can_fetch('Googlebot', 'http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('Googlebot', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
# print(rp.mtime())

# response = request.urlopen('https://www.baidu.com/robots.txt')
# print(response.read().decode())