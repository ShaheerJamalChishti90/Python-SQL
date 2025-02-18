import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",       # Replace with your database host
    user="root",   # Replace with your MySQL username
    password="shaheersql", # Replace with your MySQL password
)
print(connection.connection_id)


# Check connection
if connection.is_connected():
    print("Connected to MySQL database!")
    
# Close the connection
connection.close()
