import csv

contents = [
    ['190410217', '11267017zqh.'],
    ['190410220', 'shy010928.'],
    ['190410228', '898592106li@'],
    ['190410212', 'Zwy000624..'],
    ['190410215', 'Jsc15751083660.']
]

with open('账号信息.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(contents)

with open('账号信息.csv', 'r') as file:
    reader = csv.reader(file)
    messages = list()
    for i in reader:
        messages.append(i)

for i in messages:
    print(i[0], i[1])