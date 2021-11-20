import pymysql

# # 创建数据库
# db = pymysql.connect(host='localhost', user='root', password='123zqh', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version: ', data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET UTF8MB4')
# db.close()

# # 创建表
# db = pymysql.connect(host='localhost', user='root', password='123zqh', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, ' \
#       'age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

# # 插入数据1
# id = '190410218'
# user = 'leihebo'
# age = '50'
# db = pymysql.connect(host='localhost', user='root', password='123zqh', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
# except pymysql.err.ProgrammingError:
#     print('ProgrammingError (程序设计错误)')
#     db.rollback()
# except pymysql.err.IntegrityError:
#     print('IntegrityError (完整性误差)')
# else:
#     db.commit()
# db.close()

# # 插入数据2
# data = {
#     'id': '002',
#     'name': 'zqh',
#     'age': '90',
# }
# table = 'students'
# keys = ', '.join(data.keys())
# value_num = ', '.join(['%s'] * len(data))  # ???
# print(keys, value_num)
# # sql = 'INSERT INTO {0}({1}) values ({2})'.format(table, keys, value_num)
# sql = 'insert into {0}({1}) values ({2})'.format(table, keys, value_num)
# db = pymysql.connect(host='localhost', user='root', password='123zqh', port=3306, db='spiders')
# cursor = db.cursor()
# try:
#     cursor.execute(sql, tuple(data.values()))
# except pymysql.err.IntegrityError:
#     print('IntegrityError (完整性误差)')
#     db.rollback()
# except pymysql.err.ProgrammingError:
#     print('ProgrammingError (程序设计错误)')
#     db.rollback()
# else:
#     db.commit()
#     db.close()

# # 更新数据
# db = pymysql.connect(host='localhost', user='root', password='123zqh', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'UPDATE students SET age=%s WHERE id=%s'
# cursor.execute(sql, (25, '001'))
# db.commit()
# db.close()

# # 删除数据
# db = pymysql.connect(host='localhost', user='root', password='123zqh', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'DELETE FROM {0} WHERE {1}'.format('students', 'age<30')
# cursor.execute(sql)
# db.commit()
# db.close()

# 查询数据
db = pymysql.connect(host='localhost', user='root', password='123zqh', port=3306, db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age > 20'
cursor.execute(sql)
print(cursor.rowcount)
print(cursor.fetchone())

results = cursor.fetchall()
for result in results:
    print(result)
