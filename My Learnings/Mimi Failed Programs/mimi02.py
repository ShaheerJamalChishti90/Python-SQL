import mysql.connector

main_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='shaheersql',
    database='shaheer'
)

second_connection = main_connection.cursor()

name = str(input("Enter your name here: "))
age = int(input("Enter your age here: "))
height = int(input("Enter your height here: "))


a = "insert into i_love_mimi(name, age, height) values(%s, %s, %s)"
b = (name, age, height)


second_connection.execute(a, b)
main_connection.commit()
