import sqlite3


#step 2 & 3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)

'''
describe tablename - sql
pragma table_info(tablename) - sqlite3
'''
#conn is connection obj
#after storing in variable it becomes

details=conn.execute("pragma table_info(participants)")
print(details)

#transverse
for i in details:
    print(i)
