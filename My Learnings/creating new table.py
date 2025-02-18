#Creating a new table and inserting some data into it

import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",       # Replace with your database host
    user="root",   # Replace with your MySQL username
    password="shaheersql", # Replace with your MySQL password
    database="mimi_company"  # Replace with your database name
)

mimi = connection.cursor() #this cursor func is neccessary to use sql with py
# love_mimi = "create table if not exists mimi_shaheer(name varchar(50), age int, country varchar(50));"
# mimi.execute(love_mimi)

name = str(input("Enter your name here: "))
age = int(input("Enter your age here: "))
country = str(input("Enter your country here: "))

love_mimi = "insert into mimi_shaheer(name, age, country) values(%s, %s, %s);"
a = (name, age, country)

mimi.execute(love_mimi, a)
connection.commit()




