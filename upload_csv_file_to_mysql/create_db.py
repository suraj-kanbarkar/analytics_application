
import mysql.connector

mydb = mysql.connector.connect(host="localhost",   
                 user="root",        
                 passwd="Firewall336")
cursor = mydb.cursor()

#file = open('...../EM.txt', 'r')
#file_content = file.read()
#file.close()


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE compare")

#mycursor.execute("CREATE TABLE lead(ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,Age VARCHAR(15),Sex VARCHAR(15),Job VARCHAR(15),Housing VARCHAR(15),Saving_accounts VARCHAR(15),Checking_account VARCHAR(15),Credit_amount VARCHAR(15),Duration VARCHAR(15),Purpose VARCHAR(15))")

mycursor.close()
