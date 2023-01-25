import pymysql,time
import glob,os
import pandas as pd

# 1.prepare, specify the dir
time_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # record timing
print('>> The current time is: ',time_start)
print('>> Start processing: ')

# 2.connect to DB
print('>> Connecting to MySQL...')
db = pymysql.connect(
      host='127.0.0.1',
      port=3306,
      user='root',
      passwd='osloisthebestcity',
      db='bike_test',
      charset='utf8')
# build cursor
cursor = db.cursor()
print ('>> Data table connected.')


# 3.Submit the data of the new file to mysql
print('>> Reading...')
# MySQL query
insert_sql = 'insert into bike_test (started_at,ended_at,duration,start_station_id,start_station_name,start_station_description,start_station_latitude,start_station_longitude,end_station_id,end_station_name,end_station_description,end_station_latitude,end_station_longitude) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
# start processing single file
data_csv = pd.read_csv('./processed_csv/update.csv') # read using Pandas
# print(data_csv.head(3)) # top3
# print(data_csv.info()) # info
# print(len(data_csv.index)) # index
# print(data_csv.loc[2].values) # one specific row
ii = 0 
for i in range(0,data_csv.shape[0]): # read by row
    row = data_csv.loc[i].values # fetch i-th row
    #print(i,'>>:',data_csv.loc[i].values) # print i-th row
    cursor.execute(insert_sql, (str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]),
    str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12])))
    ii = i + 1
print(' - number of submissions: ',ii,'.')

# 5.Finishing
db.commit() # commit
db.close() # close db
cursor.close() # close cursor
time_finish = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # record the current timestamp
print('>> The current time is: ',time_finish)
print('\n',end='')
print('>> Done.') #completed