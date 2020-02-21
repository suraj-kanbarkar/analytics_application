
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Firewall336",
  database="compare"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE matched(ID INT AUTO_INCREMENT PRIMARY KEY, uniqueid VARCHAR(20), calldate VARCHAR(20), src VARCHAR(15))")


mycursor.execute("CREATE TABLE un_matched(ID INT AUTO_INCREMENT PRIMARY KEY, uniqueid VARCHAR(20), calldate VARCHAR(20), src VARCHAR(15))")

#mycursor.commit()

#mycursor.close()


