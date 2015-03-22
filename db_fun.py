#coding=utf-8
import MySQLdb

def add_data(number,name,old,sex):
	db=MySQLdb.connect("localhost","root","123456","test")
	cursor=db.cursor()
	sql='insert into students(name,old,id,sex) values('+'"'+name+'",'+'"'+old+'",'+'"'+number+'",'+'"'+sex+'"'+')'
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print "error"
		db.rollback()
	db.close()

#def delete_data():

def search_data(number):
	db=MySQLdb.connect("localhost","root","123456","test")
	cursor=db.cursor()
	sql='select * from students where id='+number
	try:
		cursor.execute(sql)
		data=cursor.fetchall()
		return data
	except:
		print "error"
	db.close()

def GetList():
	db=MySQLdb.connect("localhost","root","123456","test")
	cursor=db.cursor()
	sql='select id from students'
	try:
		cursor.execute(sql)
		data=cursor.fetchall()
		list=[0]*len(data)
		for i in data:
			list[0]=str(data[0][0])
			list[1]=str(data[1][0])
		return list
	except:
		print "error"
	db.close()
		
