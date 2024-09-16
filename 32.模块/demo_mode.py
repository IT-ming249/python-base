#模块 这个demo_mode就是一个模块，扩展名为.py的文件就是一个模块，模块可以包含，函数，类等很多东西。一系列的模块才构成了完整的Python程序
#模块的导入：
'''
方法一：import 模块名称 [as别名]
方法二：from 模块名称 import 函数/变量/类'''

import  math#按住ctrl+鼠标左键可以查看math里面的程序
print(id(math),type(math))
print(math)
print(math.pi)
print('-------------------')
print(dir(math))
print(math.pow(3,3))#3^3=27
print(math.ceil(9.001))#ceil向上取整
print(math.floor(9.99))#floor向下取整
print('-------------------')

from math import pi
print(pi)