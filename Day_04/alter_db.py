import sqlite3


#step 2 & 3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)


'''
add column - mailid
ALTER table tablename add column column_name datatype constarints
'''

conn.execute('''
alter table participants add column mail_id text not null''')