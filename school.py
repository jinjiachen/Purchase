#coding=utf-8
import MySQLdb
import wx
import db_fun

class frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'database',(10,10),(600,400))
		panel=wx.Panel(self)
		wx.StaticText(panel,-1,'学号:',(50,50))
		self.text1=wx.TextCtrl(panel,-1,'',(100,50))
		wx.StaticText(panel,-1,'姓名',(50,100))
		self.text2=wx.TextCtrl(panel,-1,'',(100,100))
		wx.StaticText(panel,-1,'年龄',(50,150))
		self.text3=wx.TextCtrl(panel,-1,'',(100,150))
		wx.StaticText(panel,-1,'性别',(50,200))
		self.text4=wx.TextCtrl(panel,-1,'',(100,200))
		self.show1=wx.StaticText(panel,-1,'',(250,100))
		button1=wx.Button(panel,-1,'录入',(50,250))
		button2=wx.Button(panel,-1,'查询',(250,250))
		list_id=db_fun.GetList()
		print type(db_fun.GetList())
		print list(db_fun.GetList())
#		list_id=['test']
		self.choice1=wx.Choice(panel,-1,pos=(250,200),size=(100,30),choices=list_id)

		self.Bind(wx.EVT_BUTTON,self.insert,button1)
		self.Bind(wx.EVT_BUTTON,self.search,button2)


	def insert(self,event):
		number=str(self.text1.GetValue())
		name=str(self.text2.GetValue())
		old=str(self.text3.GetValue())
		sex=str(self.text4.GetValue())
		db_fun.add_data(number,name,old,sex)
		
	def search(self,event):
		number=self.choice1.GetStringSelection()
		data=db_fun.search_data(number)
		for i in data:
			print("name=%s\nage=%s\nid=%s\nsex=%s\n"%(i[0],i[1],i[2],i[3])) 
			
		self.show1.SetLabel("姓名:"+i[0]+"\n年龄:"+i[1]+"\n学号:"+i[2]+"\n性别"+i[3])




if __name__=="__main__":
	app=wx.PySimpleApp()
	myframe=frame()
	myframe.Show()
	app.MainLoop()
	



