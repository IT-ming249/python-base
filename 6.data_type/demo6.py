#数据类型
#整数类型 （可以表示正数，负数，0） 默认十进制 二进制以0b开头 八进制以0o开头 16进制以0x开头
a=98;
print(a,type(a))
print('二进制',0b100110)
print('八进制',0o772)
print('十六进制',0x01ff88)
print('\n')
#浮点型
b=0.2
print(b,type(b))
n1=1.1
n2=2.2
print(n1+n2)#使用浮点数计算会出现小数位数不确定的情况,这种情况不多，知道一些就好
#解决方法
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
print('\n')
#布尔类型
#True为真 False为假
f1=True
f2=False
print(f1,type(f1),f2,type(f2))
#python中布尔类型可以转成整数计算
print(f1+1,f2+1)
print('\n')
#字符串类型
str1='我爱学习'#单引号
print(str1,type(str))
str2="我爱学习"#双引号
print(str2,type(str2))
str3='''我爱学习
说真的'''#三引号可以是三个单引号，也可以是三个双引号，三引号可以换行实现，单双就不行
print(str3,type(str3))