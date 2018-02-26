### 什么是 WorkingDay？
* 获取指定年份的所有工作日；
* 判断该对象中指定的某月天日是否属于工作日
* 根据中华人民共和国国务院发布的“部分节假日放假通知”为基础，重新修正工作日
* 返回的是一个字典，格式例如{1:[1,2,3],2:[4,5,6]}，表示1月份工作日1-3日，2月份工作日4-5日
* 开发环境Python 2.7.9

### 主要的文件

> 两个文件可以结合起来使用，以WorkingDay.py 为主，也可以单独使用

* WorkingDay.py 
    * 可以生成指定年份的一年所有工作日字典
    * 可以根据字典添加工作日和节假日
    * 结合ChinaHoliday获取国务院的节假日规定修正
    * 判断某天（年必须是实例化后本对象的year）是否为工作日
* ChinaHoliday.py
    * 根据国务院发布的节假日公告处理数据
    * 获取国务院发布的节假日放假日期（不含周六日），返回的也是字典
    * 获取国务院发布的因调休需要上班的日期，返回的也是字典

### 例子

#### WorkingDay

```
import WorkingDay

#返回的是经过国务院发布的节假日公告修正过的工作日字典
year=2017
year2017=WorkingDay.WorkingDay(year)
print year2017.china_holiday.get_workday

#添加工作日，指定的日期会增加到对象字典中
year2017.set_working({1:[1,2,3]})
print year2017.china_holiday.get_workday

#添加节假日，指定的日期会从字典中踢出
year2017.set_holiday({2:[1,2,3]})
print year2017.china_holiday.get_workday

#直接输出不含周六日的工作日字典
year2016=WorkingDay(2016)
print year2016.get_workday
```

#### ChinaHoliday
```
import ChinaHoliday

china=ChinaHoliday.ChinaHoliday(2016)
print china.get_working
print china.get_holiday
```