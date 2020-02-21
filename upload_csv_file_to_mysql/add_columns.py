
from library.class1 import neumath
import mysql.connector
import csv

df=neumath()

mydb = mysql.connector.connect(host='localhost',
    user='root',
    passwd='fycore',
    db='neumath')
cursor = mydb.cursor()

merge_mst_lead = cursor.execute("CREATE TABLE merge_mst_lead(SELECT ID, lead_phone, lead_state, ddc_entered_on, spaid_date, outsource_agency, teacher_state, a, b, c, RID, Disposition, FinalStatus FROM lead_and_mst)")

mydb.cursor(prepared = True)
result = cursor.execute(merge_mst_lead,)
mydb.commit()
mydb.close()
print "Done"
