import mysql.connector

def main():
  mydb = mysql.connector.connect(
    host="localhost",
    user="si699",
    password="password"
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE si699_table (id INT NOT NULL PRIMARY KEY, url VARCHAR(255), date DATETIME)")


if __name__=="__main__":
  main()
