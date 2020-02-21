import csv

leads_data = open('/home/imsg/PycharmProjects/grassroots/upload_data/upload_csv_file_to_mysql/data/matched.txt', 'w')
mst_data=open('/home/imsg/PycharmProjects/grassroots/upload_data/upload_csv_file_to_mysql/data/un_matched.txt', 'w')

# Create LEADS.txt
with open('/home/imsg/PycharmProjects/grassroots/upload_data/upload_csv_file_to_mysql/data/matched.csv',"rt") as leads_file:
	for row in leads_file:
    		leads_data.write(row)

# Create MST.txt
with open('/home/imsg/PycharmProjects/grassroots/upload_data/upload_csv_file_to_mysql/data/un_matched.csv',"rt") as mst_file:
	for row in mst_file:
    		mst_data.write(row)


