import sqlite3


#step 2 & 3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

details = conn.execute('select * from participants')

for row in details:
    print(row)