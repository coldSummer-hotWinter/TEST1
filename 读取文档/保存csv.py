from urllib import request
from io import StringIO
import csv

# data = request.urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
# data_file = StringIO(data)
# csv_reader = csv.reader(data_file)
# for row in csv_reader:
#     print(row)


data = request.urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
data_file = StringIO(data)
print(data_file)
csv_reader = csv.DictReader(data_file)
print(csv_reader.fieldnames)
for row in csv_reader:
    print(row)

