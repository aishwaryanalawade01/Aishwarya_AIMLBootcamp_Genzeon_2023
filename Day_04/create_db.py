#steps:
'''
1.importing sqlite3
2.create a db
3.est connection with db
4.create a table in db - write a query
5.execute query
'''


import sqlite3


#step 2 & 3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

#step 4
'''
create table tablename(colname1 datatype constraints,col2 datatype constarints...)
constraints -> primary key,not null,check,unique,foreign key,...
'''

query='''
create table participants(g_id int primary key, name text not null, branch text not null,study text not null DEFAULT 'Btech')
'''

conn.execute(query)
conn.commit()
conn.close()