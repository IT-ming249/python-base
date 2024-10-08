#字符格式化操作：按一定格式输出的字符串
#方法一：%作占位符 %s字符串 %d整数 %f浮点数 跟C语言语言
name='战三'
age=5
print('我叫%s,今年%d岁'%(name,age))
print('------')
#方法二：{}作占位符
print('我叫{0}，今年{1}岁'.format(name,age))#数字代表索引
print(f"我叫{name},今年{age}岁")
print('--------')
print('%10d'%99)#调制个时候的宽度
print('%.3f'%3.1415926)#浮点数保留小数点后三位
print('%10.3f'%3.1415926)#同时调制宽度和精度
print('{0:.3}'.format(3.1415926))#此处0表示索引 .3表示一共是3位数
print('{0:.3f}'.format(3.1415926))#这样才是保留3位小数
print('{0:10.3f}'.format(3.1415926))#同时调制宽度和精度