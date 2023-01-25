import pymysql
import csv

print('>> Connect to MySQL...')
db = pymysql.connect(
      host='127.0.0.1',
      port=3306,
      user='root',
      passwd='osloisthebestcity',
      db='bike_test',
      charset='utf8')
# build cursor
cursor = db.cursor()
print ('>> Data table connected')
# sql = 'select * from bike_test '
sql='select start_station_id,end_station_id,start_station_name,end_station_name from bike_test'
cursor.execute(sql)


#This is to get the first data in the table
counts={}
rest=cursor.fetchall()
for item in rest:
    counts[item]=counts.get(item,0)+1
items=list(counts.items())
LL2 = sorted(items, key=lambda x: x[1], reverse=True)  # Sort by the second number of the tuple
#print("sorted():", LL2[0:50])
# print(items[1][1])
#print(type(items))
#print(type(rest))
print("Sort Success")

header = ('start_station_id', 'end_station_id', 'start_station_name', 'end_station_name', 'count')
csvfile=open('./start2end.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow(header)

for key in LL2:
    # print([key[0][0],key[0][1],key[0][2],key[0][3],key[1]])
    # print([key,LL2[key]])
    writer.writerow([key[0][0],key[0][1],key[0][2],key[0][3],key[1]])
csvfile.close()


# close db connection
db.close()