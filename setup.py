# -*- coding: utf-8 -*-
# @Author: vition
# @Date:   2017-07-04 14:19:51
# @Last Modified by:   vition
# @Last Modified time: 2017-07-04 14:22:00
from distutils.core import setup

setup(
    name='workingDay',
    version='1.2.0',
    author='vition kuo',
    author_email='369709991@qq.com',
    packages=['towelstuff', 'towelstuff.test'],
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='https://github.com/vition/workingDay',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
    ],
)