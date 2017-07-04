# -*- coding: utf-8 -*-
# @Author: vition
# @Date:   2017-07-03 12:05:04
# @Last Modified by:   vition
# @Last Modified time: 2017-07-04 14:03:38
import datetime
import calendar
import ChinaHoliday

class WorkingDay(object):
	"""
		根据年份计算当前年每月要上班的日期
		#构造方法 的出来的日期是不包含节假日的工作日日期，不填写自动获取当前年份
		#方法 set_year 是通过输入一个新的年份来计算新的日期
		#方法 set_holiday 是通过设置国家规定的节假日来重新设定当年的工作日，参数holiday格式是字典{月份:[上班日期1，上班日期2]}，例如{10:[1,2,3,4,5,6,7,8]}
		#方法 set_working 有放假就有调休，这里是修正调休的日期，参数transfer的格式也是字典 参考setHoliday的格式
		#方法 is_working 根据指定日期(今年)判断是否为工作日 参数date 格式 mmdd 
		#每一个方法的操作都会操作 self.__yearWork，所以谨慎操作
	"""
	def __init__(self,year=""):
		self.__yearWork={}
		if year =="":
			self.__year=datetime.datetime.now().year
		else:
			self.__year=year
		
		self.set_year(self.__year)


	def set_year(self,year=""):
		"""[summary]
		#设置指定年的工作日，仅排除周六日
		[description]
		
		Keyword Arguments:
			year {str} -- [description] (default: {""})
			#如果year为空，默认使用当前年份
		"""
		
		if year!="":
			self.__year=year
		for month in range(1,13):
			monthDays=calendar.monthrange(self.__year,month)[1]
			monthList=[]
			for day in range(1,monthDays+1):
				dateStr="%d%d%d" % (self.__year,month,day)
				if datetime.datetime.strptime(dateStr,"%Y%m%d").weekday()<5:
					monthList.append(day)
					monthList.sort()
			self.__yearWork[month]=monthList

	
	def set_holiday(self,holiday):
		"""[summary]
		#设置放假的日期

		[description]
		
		Arguments:
			holiday {[type]} -- [description]
			#格式是字典{月份:[上班日期1，上班日期2]}，例如{10:[1,2,3,4,5,6,7,8]}
		"""
		for hol in holiday.items():
			for i in hol[1]:
				if i in self.__yearWork[hol[0]]:
					self.__yearWork[hol[0]].remove(i)
	#设置调休的日期
	def set_working(self,working):
		"""[summary]
		#设置放假的日期

		[description]
		
		Arguments:
			holiday {[type]} -- [description]
			#格式是字典{月份:[上班日期1，上班日期2]}，例如{10:[1,2,3,4,5,6,7,8]}
		"""
		for tran in working.items():
			for i in tran[1]:
				if i not in self.__yearWork[tran[0]]:
					self.__yearWork[tran[0]].append(i)
					self.__yearWork[tran[0]].sort()

	
	def is_working(self,date):
		"""[summary]
			#判断指定月日是否为工作日
		[description]
		
		Arguments:
			date {[type]} -- [description]
			#date的格式要4位，例如：0101，自动填充对象设定的年
		Returns:
			bool -- [description]
		"""

		theDate=datetime.datetime.strptime(self.__year+date,"%Y%m%d")
		if theDate.day in self.__yearWork[theDate.month]:
			return True
		return False

	@property
	def chian_holiday(self):
		china=ChinaHoliday.ChinaHoliday()
		china.set_year(self.__year)
		self.set_holiday(china.get_holiday)
		self.set_working(china.get_working)
		return self
	
	@property
	def get_workday(self):
		"""[summary]
			#返回指定年的工作日
		[description]
		
		Returns:
			[type] -- [description]
			#返回字典 例如{10:[1,2,3,4,5,6,7,8]}
		"""
		return self.__yearWork

if __name__ == "__main__":
	
	year=2016
	year2017=WorkingDay(year)
	print year2017.get_workday
	# print year2017.get_workday
	# print year2017.yearWork
	# print dir(datetime.time)
	# print "%s" % datetime.datetime.now().year
