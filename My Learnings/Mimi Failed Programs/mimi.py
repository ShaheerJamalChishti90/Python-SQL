import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mira',
    database = 'lesson'
)

# print(connection.connection_id)

mimi = connection.cursor()
# thv = 'create table shaheer (name varchar(50), age int, country varchar(50));'
# mimi.execute(thv)

taehyung = 'insert into shaheer(name, age, country) values (%x, %x, %x), (%x, %x, %x);'
a = ('shaheer', 100, 'Pakistan')
b = ('mimi', 22, 'Korea' )

mimi.execute(taehyung, a, b)
connection.commit()