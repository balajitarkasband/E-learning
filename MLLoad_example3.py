import pandas as pd 
import pymysql
db = pymysql
db = pymysql.connect(host = 'localhost',passwd = '',user = 'root', db='Elearning')
cursor = db.cursor()
sql = "select * from Users"
df = pd.read_sql_query(sql,db)
print(df.head(2))