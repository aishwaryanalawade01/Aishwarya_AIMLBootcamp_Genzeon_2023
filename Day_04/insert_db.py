import sqlite3


#step 2 & 3
'Bootcamp2023.db'
conn=sqlite3.connect('Bootcamp2023.db')
print(conn)


'''
insert into tablename values('','')
'''

#conn.execute("insert into participants values(101,'Ash','ETC','BE','ash@gmail.com')")
conn.execute("insert into participants values(1 , 'Shubham' , 'Civil' , 'B-Tech' , 'mhaske@gmail.com')")
conn.commit()
conn.close()


#use update to change name to full name