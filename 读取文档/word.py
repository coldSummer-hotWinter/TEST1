from zipfile import ZipFile
from urllib import request
from bs4 import BeautifulSoup
from io import BytesIO


word_file = request.urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
word_file = BytesIO(word_file)  # 将word文档读成二进制文件对象
document = ZipFile(word_file)  # 解压文件
xml_content = document.read('word/document.xml')  # 读取文件
print(xml_content.decode('utf-8'))


# word_file = request.urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
# word_file = BytesIO(word_file)  # 将word文档读成二进制文件对象
# document = ZipFile(word_file)  # 解压文件
# xml_content = document.read('word/document.xml')  # 读取文件
#
# word_obj = BeautifulSoup(xml_content, 'xml')
# text_strings = word_obj.find_all('w:t')
#
# for text_elem in text_strings:
#     print(text_elem.text)
