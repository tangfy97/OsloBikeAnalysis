'''
STEPS:
1. We first import mysql.connector. After importing, we use the MySQL.connector.connect() function to connect to the MySQL database.
2. We create a cursor for the table.
3. We execute our function to find the average value of the table's duration column using the cursor.execute() function.
4. We create a variable called row and set it to cursor.fetchall().
5. We use a for loop and print out i[0], which represents the average value of the duration column.
6. After everything is finished, we close the database connection.

Conclusion:
With this approach, we can find the average of all rows in a column in a MySQL table using Python.
'''

import pymysql
print('>> Connect to MySQL...')
db = pymysql.connect(
      host='127.0.0.1',
      port=3306,
      user='root',
      passwd='osloisthebestcity',
      db='bike_test',
      charset='utf8')

cursor = db.cursor()
print ('>> Data table connected.')

retrieve = "Select AVG(duration) AS average from bike_test where YEAR(ended_at) = 2022 ;"

cursor.execute(retrieve)
rows = cursor.fetchall()
for i in rows:
    print("Average duration is :" + str(i[0]))
    #Average duration is :750.6513080041487



# close connection
db.close()