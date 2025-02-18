import mysql.connector

main_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='shaheersql',
    database='shaheer'
)

second_connection = main_connection.cursor()

a = "select*from i_love_mimi;"

second_connection.execute(a)

result = second_connection.fetchall() #fetch means to catch something
for i in result:
    print(i)