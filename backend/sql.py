import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="si699",
  password="password"
)

print(mydb)
