import pymysql
mydb = pymysql.connect(
      host='localhost',
      port=3306,
      user='root',
      passwd='osloisthebestcity',
      # 5XWh>w9wqV*a
      db='bike_test')
      # charset='utf8')

mycursor = mydb.cursor()

mycursor = mydb.cursor()

sql = "truncate table bike_test" ## cleanup

mycursor.execute(sql)

mydb.close()