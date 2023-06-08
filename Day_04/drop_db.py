import sqlite3


#step 2 & 3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)


query='''drop table participants if exists'''
conn.execute(query)