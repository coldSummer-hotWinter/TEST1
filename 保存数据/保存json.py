import json

people = {
    'name': '张',
    'sex': 'male',
    'nation': 'china',
    'lalal': 'erererer'
}

with open('t1.json', 'w', encoding='utf-8') as file:
    # json.dump(people, file, indent=2, ensure_ascii=False)
    file.write(json.dumps(people, indent=2))

with open('t1.json', 'a') as file:
    file.write(json.dumps(people, indent=2))