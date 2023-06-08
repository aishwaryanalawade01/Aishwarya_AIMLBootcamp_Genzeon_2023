import sqlite3


'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)


query='''delete from participants where g_id=1'''

conn.execute(query)
conn.commit()
