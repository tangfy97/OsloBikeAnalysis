import pymysql,time
import glob,os
import pandas as pd

# 1.Prepare, specify the directory
time_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # record the current timestamp
print('>> The current time is: ',time_start)
print('>> Start processing: ')
filelocation = r"/Users/feiyangtang/Desktop/OsloBikeAnalysis/processed_csv/"

# 2.Link DB
print('>> Connect MySQL...')
db = pymysql.connect(
      host='127.0.0.1',
      port=3306,
      user='root',
      passwd='osloisthebestcity',
      db='bike_test',
      charset='utf8')
# build cursor
cursor = db.cursor()
print ('>> Connected to the data table.')

# 3.Check local new file name
filenames=[]
os.chdir(filelocation) #given dir
for i in glob.glob("*.csv"): # Get all CSV file names under the specified target
    filenames.append(i[:-4]) # Filename does not contain ".csv"
count = len(filenames)
print('>> There are: ',count,' local files.') # The following is to print out each file name with "Num.**" as the serial number
for i in range(0,count): # Fill the number 0-9 with 0 to 2 digits, or use the zfill function or FORMAT to format
    if i<9:
        ii = i+1
        ij = '0'+str(ii)
    else:
        ij = i+1
    print(' - Num.', end='')
    print(ij, filenames[i])

# 4.Submit the data of the new file to mysql
print('>> Reading...')
# MySQL query
insert_sql = 'insert into bike_test (started_at,ended_at,duration,start_station_id,start_station_name,start_station_description,start_station_latitude,start_station_longitude,end_station_id,end_station_name,end_station_description,end_station_latitude,end_station_longitude) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
# Start file-by-file processing
for file_name in filenames:
    print(" + Now processing：", file_name,'（the ',filenames.index(file_name)+1,'-th file）')
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Record the time spent processing each file
    print(' - The current time is: ', time_now)
    data_csv = pd.read_csv(open(filelocation + file_name+'.csv')) # Use pandas to read csv files
    # print(data_csv.head(3)) # print top 3
    # print(data_csv.info()) # print info
    # print(len(data_csv.index)) # print index
    # print(data_csv.loc[2].values) # check one specificed row
    ii = 0 # Used to count the amount of data for each file
    for i in range(0,data_csv.shape[0]): # read by rows
        row = data_csv.loc[i].values # fetch i-th row
        #When running, comment print to improve speed
        #print(i,'>>:',data_csv.loc[i].values) # Print the i-th row of data
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