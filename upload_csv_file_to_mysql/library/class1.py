
import mysql.connector
from mysql.connector import Error,MySQLConnection


class compare:
	#def __init__(self):
	
	def getconnection(self):
		conn = mysql.connector.connect(host='127.0.0.1',
                                       database='compare',
       	                               user='root',
        	                       password='Firewall336')
		if conn.is_connected():
                	print('Connected to MySQL database')
		return conn

	

	# Inserting into lead table	
	def insert_matched(self,uniqueid,calldate,src):
		conn = self.getconnection()
		QS = "insert into matched (uniqueid,calldate,src) VALUES (?,?,?)"
		cursor = conn.cursor(prepared = True)
		result = cursor.execute(QS, (uniqueid,calldate,src))
		conn.commit()
		conn.close()

	# Inserting into mst table	
	def insert_un_matched(self,uniqueid):
		conn = self.getconnection()
		QS = "insert into un_matched (uniqueid) VALUES (?)"
		cursor = conn.cursor(prepared = True)
		result = cursor.execute(QS, (uniqueid,))
		conn.commit()
		conn.close()
	
	# Delete from lead table
	def delete_lead(self, ID):
		con = self.getconnection()
		QS = "delete from lead WHERE ID = ?"
		cursor = con.cursor(prepared = True)
		print (QS)
		result = cursor.execute(QS, (ID,))
		con.commit()
		con.close()

	# Delete from mst table	
	def delete_mst(self, ID):
		con = self.getconnection()
		QS = "delete from mst WHERE ID = ?"
		cursor = con.cursor(prepared = True)
		print (QS)
		result = cursor.execute(QS, (ID,))
		con.commit()
		con.close()


	# Insert into lead table
	'''
	def insert_lead(self,ID,lead_phone,lead_state,ddc_entered_on,spaid_date,outsource_agency,teacher_state,a,b,c):
		conn = self.getconnection()
		QS = "INSERT INTO lead (,) SELECT id,name FROM mst;
 VALUES (?,?,?,?,?,?,?,?,?,?)"
		cursor = conn.cursor(prepared = True)
		result = cursor.execute (QS,(ID,lead_phone,lead_state,ddc_entered_on,spaid_date,outsource_agency,teacher_state,a,b,c))
		conn.commit()
		conn.close()
	'''

	def update_lead(self,ID,Age,Sex,Job,Housing,Saving_accounts,Checking_account,Credit_amount,Duration,Purpose):
		conn = self.getconnection()
		QS = "update VOILATION set %s = ? WHERE ID = ?" % (ID)
		print (QS)
		cursor = conn.cursor(prepared = True)
		result = cursor.execute(QS, (ID,Age,Sex,Job,Housing,Saving_accounts,Checking_account,Credit_amount,Duration,Purpose,))
		conn.commit()
		conn.close()


	def get_lead(self):
		con = self.getconnection()
		QS = "select * from lead "
		cursor = con.cursor(prepared=True)
		res = cursor.execute(QS)
		res=cursor.fetchall()
		con.close()
		print (res)
		return res
	
	def get_lead(self,ID):
		con = self.getconnection()
		QS = "select * from lead where ID=" + str(ID)
		cursor = con.cursor(prepared=True)
		res = cursor.execute(QS)
		res= cursor.fetchall()
		con.close()
		print (res)
		return res	
	
 		
