# -*- coding: utf-8 -*-
# @Author: vition
# @Date:   2017-07-04 14:19:51
# @Last Modified by:   vition
# @Last Modified time: 2017-07-04 14:28:24
from distutils.core import setup

setup(
    name='workingDay',
    version='1.2.0',
    author='vition kuo',
    author_email='369709991@qq.com',
    packages=['WorkingDay', 'ChinaHoliday'],
    url='https://github.com/vition/workingDay',
    description='获取节假日的库，适用于中国',
    long_description=open('README.md').read(),
)