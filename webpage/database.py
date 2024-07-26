# import mysql.connector as mc
# conn =mc.connect(host='licalhost',user='root',password='database@9090')


import sqlite3
conn = sqlite3.connect("userdata.db")



# create_database_query = """
# create database userdata.db
# """
create_table_query = """
create table userecord (name varchar(25),age integer,address varchar(25),college varchar(25),branch varchar(25),roll_no integer,query_sub varchar(60))"""

cur = conn.cursor()
cur.execute(create_table_query)
print("You have successfully created database !....")

cur.close()
conn.close()


