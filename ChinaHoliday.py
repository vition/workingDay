# -*- coding: utf-8 -*-
# @Author: vition
# @Date:   2017-07-04 09:47:07
# @Last Modified by:   vition
# @Last Modified time: 2017-07-04 14:13:43
import urllib2
import urllib
import datetime
import time
import re
import os

class ChinaHoliday(object):
	"""[summary]
	#根据国务院发布的节假日公告，获取数据分析
	#只能获取2010至今的节假日数据，2009年及之前的格式有点乱，忽略
	[description]
	"""
	def __init__(self,year=""):
		self.__workingDict={}
		self.__holidayDict={}
		self.__yearHtml={}
		self.set_year(year)


	def set_year(self,year=""):
		"""[summary]
		#主方法，根据年份查找国务院力的
		#为了节约带宽和加快速度，查找到的数据会在year文件夹保存，格式例如：2017html，当本地存在该文件则不会再去网上截取
		[description]
		
		Keyword Arguments:
			year {str} -- [description] (default: {""})
			#年参数要4位数 例如2017，如果为空默认获取当前年份
		
		"""
		if year<2010:
			print "对不起，只允许查2009年后的节假日"
			return False

		if year!="":
			self.__year=year
		else:
			self.__year=datetime.datetime.now().year	

		
		yearHtml=self.__yearHtml.get(self.__year,"None")


		if os.path.exists("year/%dhtml" % self.__year)==False:
			url="http://sousuo.gov.cn/s.htm?t=paper&advance=false&n=&sort=&timetype=&mintime=&maxtime=&q="+urllib.quote("%d年部分节假日安排" % self.__year);
			searchHtml=self.get_html(url)
			try:
				yearUrl=re.search("http://www.gov.cn/zhengce/content/%d-[0-9]{1,2}/[0-9]{1,9}/content_[0-9]*.htm" % (int(self.__year)-1),searchHtml).group()

				yearHtml=self.get_html(yearUrl)

				with open("year/%dhtml" % self.__year,"w") as newhtml:

					newhtml.write(yearHtml)

				self.__process_date(yearHtml)
	
			except:
				 print "别心急，你要查的%d还没公布呢！" % self.__year
				 return False
		
		else:
			with open("year/%dhtml" % self.__year,"r") as oldhtml:
				yearHtml=oldhtml.read()
			if yearHtml=="":
				os.remove("year/%dhtml" % self.__year)

				return False
			self.__process_date(yearHtml)
		# print yearUrl
	@property
	def get_working(self):
		"""
		#根据主方法处理过后，返回指定年的工作（调休的上班）格式
		{月:[日期1，日期2]}
		"""
		return self.__workingDict

	@property
	def get_holiday(self):
		"""
		#根据主方法处理过后，返回指定年的假日格式，不含周六日
		{月:[日期1，日期2]}
		"""
		return self.__holidayDict

	
	def get_html(self,url):
		"""
		#通过urllib2获取网页的文本
		"""
		req=urllib2.Request(url)
		req.add_header('Referer','http://sousuo.gov.cn/')
		req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
		reqs=urllib2.urlopen(req)
		return reqs.read()

	def __process_date(self,html):
		"""
		#用来处理公告页面里的数据
		"""
		clearHtml = re.compile(r'<[^>]+>',re.S)
		yaerStr = clearHtml.sub('',html)

		data=re.findall("[0-9]{1,2}月[0-9]{1,2}日[\末\与\周\连\放\假\补\调\休\共\天0-9\，\、\农\历\除\公\夕\星\期\六\日\一\二\三\四\五（\）\上\班\至]*\。",yaerStr)
		
		for noticline in data:
			if "上班" in noticline:
				dates=re.findall("([0-9]{1,2})月([0-9]{1,2})日",noticline)
				for x in dates:
					self.__day_append(self.__workingDict,int(x[0]),int(x[1]))
			else:
				if "共" in noticline:
					gong=re.search("共([0-9]{1,2})天",noticline).group(1)
					startDate=re.search("([0-9]{1,2})月([0-9]{1,2})日",noticline)
					theday=datetime.datetime.strptime("%d%02d%02d" % (self.__year,int(startDate.group(1)),int(startDate.group(2))),"%Y%m%d")
				
					for o in range(0,int(gong)):
						newDay=theday + datetime.timedelta(days = o)
						self.__day_append(self.__holidayDict,newDay.month,newDay.day)
				else:
					dates=re.findall("([0-9]{1,2})月([0-9]{1,2})日",noticline)
					for x in dates:
						self.__day_append(self.__holidayDict,int(x[0]),int(x[1]))


	def __day_append(slef,dicts,month,day):
		"""
		#添加各种数据，内部方法
		"""
		try:
			type(dicts[month])=="list"
		except:
			dicts[month]=[]
		finally:
			dicts[month].append(day)



if __name__ == "__main__":
	china=ChinaHoliday(2016)
	print china.get_working
	print china.get_holiday
