#现在在这个模块中导入刚刚创建的package1
#语法格式:  包名.模块名
import package1.module_A as ma #这个ma是别名 ,往后编程package1.module_A就叫ma了
#print(package1.module_A.a) 这样写代码有点长
print(ma.a)

#导入带有包的模块的注意事项:
#使用import导包时，只能跟包名/模块名 eg import clc
#使用from....import可以导入包，模块，函数，变量