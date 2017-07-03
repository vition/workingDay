# -*- coding: utf-8 -*-
# @Author: vition
# @Date:   2017-07-03 12:05:04
# @Last Modified by:   vition
# @Last Modified time: 2017-07-03 14:17:34
import datetime
import calendar

class WorkingDay(object):
	"""
		根据年份计算当前年每月要上班的日期
		#构造方法 的出来的日期是不包含节假日的工作日日期，不填写自动获取当前年份
		#方法 initWorkday 是通过输入一个新的年份来计算新的日期
		#方法 setHoliday 是通过设置国家规定的节假日来重新设定当年的工作日，参数holiday格式是字典{月份:[上班日期1，上班日期2]}，例如{10:[1,2,3,4,5,6,7,8]}
		#方法 setTransfer 有放假就有调休，这里是修正调休的日期，参数transfer的格式也是字典 参考setHoliday的格式
		#方法 isWorking 根据指定日期(今年)判断是否为工作日 参数date 格式 mmdd 
		#每一个方法的操作都会操作 self.yearWork，所以谨慎操作
	"""
	def __init__(self,year=""):
		if year =="":
			self.year=datetime.datetime.now().year
		else:
			self.year=year
		
		self.initWorkday(year)

	#设置年度默认的工作日
	def initWorkday(self,year=""):
		self.yearWork={}
		if year!="":
			self.year=year
		for month in range(1,13):
			monthDays=calendar.monthrange(self.year,month)[1]
			monthList=[]
			for day in range(1,monthDays+1):
				dateStr="%d%d%d" % (self.year,month,day)
				if datetime.datetime.strptime(dateStr,"%Y%m%d").weekday()<5:
					monthList.append(day)
			self.yearWork[month]=monthList

	#设置放假的日期
	def setHoliday(self,holiday):
		self.holiday=holiday
		for hol in self.holiday.items():
			for i in hol[1]:
				if i in self.yearWork[hol[0]]:
					self.yearWork[hol[0]].remove(i)
	#设置调休的日期
	def setTransfer(self,transfer):
		self.transfer=transfer
		for tran in self.transfer.items():
			for i in tran[1]:
				if i not in self.yearWork[tran[0]]:
					self.yearWork[tran[0]].append(i)

	#判断指定月日是否为工作日
	def isWorking(self,date):
		theDate=datetime.datetime.strptime(date,"%m%d")
		if theDate.day in self.yearWork[theDate.month]:
			return True
		return False
		

if __name__ == "__main__":
	year2017=WorkingDay(2017)
	holiday={1:[1,2,27,28,29,30,31],2:[1,2],4:[2,3,4,29,30],5:[1,28,29,30],10:[1,2,3,4,5,6,7,8]}
	transfer={1:[22],2:[4],4:[1],5:[27],9:[30]}
	year2017.setHoliday(holiday)
	year2017.setTransfer(transfer)
	m=7
	d=2
	print year2017.isWorking("%d%d"%(m,d)) 
	# print year2017.yearWork
	# print dir(datetime.time)
	# print "%s" % datetime.datetime.now().year
