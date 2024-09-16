#Python中的一些常用模块
import sys #与Python解释器及其环境操作的相关标准库
import time #与时间相关的各种函数的库
import os #提供了访问操作系统服务的标准库
import calendar  #提供日期相关的各种函数的标准库
import urllib.request #用于读取网上（服务器）的数据标准库
import _json #用于使用JSON序列化和反序列化对象
import math #跟数学有关的库
import decimal #用于进行精度控制运算
import logging #提供灵活记录事件，错误，调试等日志信息功能
print(sys.getsizeof(14))
print(sys.getsizeof(23))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('http://www.bilibili.com').read())