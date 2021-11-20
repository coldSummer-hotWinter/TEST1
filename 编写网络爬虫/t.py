from urllib import request, parse, robotparser


# txt = robotparser.RobotFileParser('http://www.baidu.com/robots.txt')
# txt.read()
# print(txt.can_fetch('Baiduspider', 'http://www.baidu.com'))
# print(txt.mtime())


req = request.Request('https://www.jianshu.com/robots.txt')
req.add_header('user-agent', 'Baiduspider')
html = request.urlopen(req).read().decode('utf-8').split('\n')
txt = robotparser.RobotFileParser()
txt.parse(html)
print(txt.can_fetch('user-agent', 'https://www.jianshu.com'))