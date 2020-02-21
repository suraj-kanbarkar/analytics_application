
from library.class1 import compare 
import mysql.connector
import csv
import time

df=compare()
'''
#insert
#df.create_VOILATION(1,"ka564325","/usr/abd/ghj.jpg","signaljump","in.h264")

#delete
#df.delete_VOILATION(1)

#update
val = "Sa564325"
ID = 1
df.update_VOILATION(ID,"LPN",val)

# read
df.get_VOILATION(1)
'''

# Inserting data into Table
with open('/home/imsg/PycharmProjects/grassroots/upload_data/upload_csv_file_to_mysql/data/matched.txt', 'rt') as text_file:
	#for row in text_file:
		#print(row)
	
	lines=text_file.readlines()
	for i, x in enumerate(lines):
		if i!=0:
			print(x)
			df.insert_matched(*x.split(','))


with open('/home/imsg/PycharmProjects/grassroots/upload_data/upload_csv_file_to_mysql/data/un_matched.txt', 'rt') as text_file:
	#for row in text_file:
		#print(row)
	
	lines=text_file.readlines()
	for i, x in enumerate(lines):
		if i ==0:
			continue
	
		if i >=1:
			print(x)
			df.insert_un_matched(*x.split(','))


start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

