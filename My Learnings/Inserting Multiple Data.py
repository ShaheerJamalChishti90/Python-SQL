# Inserting multiple data into a table

import mysql.connector

main_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='shaheersql',
    database='shaheer'
)

second_connection = main_connection.cursor()

a = "insert into i_love_mimi(name, age, height) values(%s, %s, %s)"
b = [("Mirani", 25, 158), ("Aisyah", 34, 154), ("Mimi", 22, 165)]


second_connection.executemany(a, b)
main_connection.commit()
