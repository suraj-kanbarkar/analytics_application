
from library.class1 import neumath
import mysql.connector
import csv

df=neumath()

mydb = mysql.connector.connect(host='localhost',
    user='root',
    passwd='fycore',
    db='neumath')
cursor = mydb.cursor()

lead_and_mst = cursor.execute("CREATE TABLE lead_and_mst(select lead.ID, lead.lead_phone, lead.lead_state, lead.ddc_entered_on, lead.spaid_date, lead.outsource_agency, lead.teacher_state, lead.a, lead.b, lead.c, mst.Phone, mst.RID, mst.Disposition, mst.CallBack_DateTime, mst.FinalStatus from lead INNER JOIN mst on lead.ID = mst.ID)")

mydb.cursor(prepared = True)
result = cursor.execute(lead_and_mst,)
mydb.commit()
mydb.close()
print "Done"
