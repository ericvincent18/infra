

import mysql.connector

mydb = mysql.connector.connect(
  host="",
  user="",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
