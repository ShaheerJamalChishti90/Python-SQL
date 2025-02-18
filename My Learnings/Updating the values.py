# Inserting multiple data into a table

import mysql.connector

main_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='shaheersql',
    database='shaheer'
)

second_connection = main_connection.cursor()

a = "update i_love_mimi set height = 180 where height = 125478;"

second_connection.execute(a)
main_connection.commit()
