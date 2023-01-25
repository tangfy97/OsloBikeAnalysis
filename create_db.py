import pymysql

# 1.Connect the database
db = pymysql.connect(
      host='localhost',
      port=3306,
      user='root',
      passwd='osloisthebestcity',
      # db='bike_test',
      charset='utf8')
# create cursor
cursor = db.cursor()
# SQL statement to create data
sql_db = 'create database if not exists bike_test;'
# execute SQL statement
cursor.execute(sql_db)
# specified database
cursor.execute('use bike_test;')
print ('>> Data table connected, processing...')

# 2.Add database header (created fields, do not use spaces)
sql = '''CREATE TABLE IF NOT EXISTS bike_test (
        `ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `started_at` CHAR(50),
        `ended_at` CHAR(50),
        `duration` CHAR(10),
        `start_station_id` CHAR(10),
        `start_station_name` CHAR(60),
        `start_station_description` CHAR(60),
        `start_station_latitude` CHAR(20),
        `start_station_longitude` CHAR(20),
        `end_station_id` CHAR(10),
        `end_station_name` CHAR(60),
        `end_station_description` CHAR(60),
        `end_station_latitude` CHAR(20),
        `end_station_longitude` CHAR(20)     
        )'''
cursor.execute(sql)

# 3.Submit and close link
cursor.close()
db.close()
print ('>> Done.')