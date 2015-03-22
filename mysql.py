#coding=utf-8
import MySQLdb

db=MySQLdb.connect("localhost","root","123456","test")
cursor=db.cursor()
#cursor.execute("select * from name") 
#data=cursor.fetchone()
#data=cursor.fetchall()
#print data[1][0]

sql='insert into name(name,old) values("test",21)'
try:
	cursor.execute(sql)
	#db.commit()
	db.rollback()
	print "rollback"
except:
	print "error:"
	db.rollback()
db.close()
