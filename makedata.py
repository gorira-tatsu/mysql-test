import mysql.connector
import random
import datetime
import hashlib


conn = mysql.connector.connect(
        host='localhost',
        user='tester',
        password='getwild',
        database='test'
        )

cursor = conn.cursor()


def random_name():
    names = ['めぐみ', 'あきら', 'かねだ', 'いちろう', 'はなこ', 'つむぎ', 'はるか', 'あおい', 'たろう']
    return names[random.randrange(0, 8)]


def random_time():
    year = random.randrange(2018, 2022)
    month = random.randrange(1, 12)
    day = random.randrange(1, 29)
    return datetime.date(year, month, day)


def random_password():
    return hashlib.sha256(str.encode(str(random.randrange(0, 100)))).hexdigest()


for i in range(0, 10000):
    cursor.execute('INSERT INTO testtable (`name`, `age`, `times`, `pass`) values ("{}", "{}", "{}", "{}")'.format(
        random_name(),
        random.randrange(0, 90),
        random_time(),
        random_password()
        ))
    conn.commit()

for j in range(10):
    cursor.execute('INSERT INTO testtable (name,times,pass,age) SELECT name,times,pass,age from testtable;')
    conn.commit()
