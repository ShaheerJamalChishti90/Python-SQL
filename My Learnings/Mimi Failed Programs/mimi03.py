import mysql.connector

main_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mira',
    database = 'lesson'
)

# print(connection.connection_id)

mimi = main_connection.cursor()

a = 'update shaheer set name = "shaheer1" where name = "taehyung"; '
mimi.execute(a)
main_connection.commit()