import sqlite3


#step 2 & 3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)


query='''update participants set name = "Nalawade" where g_id=101'''
conn.execute(query)
conn.commit()
conn.close()