import mysql.connector
mylist=[]
print('heiiiiii')

cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='employee')
print('hello')

cursor=cnx.cursor()
query='select * from member;'
cursor.execute(query)
for (Name,Weight,Height) in cursor:
    mylist.append((Name,Weight,Height))

mylist=sorted(mylist,key=lambda x:(-x[2],x[1]))

for name,weight,height in mylist:
    print(name,height,weight)

cnx.close()
