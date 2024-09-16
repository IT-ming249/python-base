#字典
#字典是Python内置的数据结构之一，与列表一样是一个可变序列（增删改查不改变地址ID）
#以键值对的方式储存数据，是一个无序序列
#语法结构：字典名{'张三'：10，'李四'：20}
# '张三'：10是一个键值对 ：之前叫做键 ：之后叫做值 ，注意：由于哈希函数计算，键不可变（str就是不可变序列）
#---
print('字典的创建')
#方法一：使用花括号
sorces={'张三':50,'李四':60,'王五':70}
print(sorces)
print(type(sorces))
print('------')
#方法二：使用内置函数dict（）
students=dict(name='jack',age=20)#这个方法智能生成一个键值对
print(students)
print('-----')
print('字典中获取数据')
#方法一：字典名[键] 若查找的键不存在，该形式会报错
sorces={'张三':50,'李四':60,'王五':70}
print(sorces['张三'])
print('------')
#方法二：字典名.get(键)
print(sorces.get('张三'))
print(sorces.get('陈六'))#若查找的键不存在，会输出None
print(sorces.get('西八',99))#键‘西八’不存在，但可以通过这种方法设置默认的值，以便在键'西八'不存在的时候返回
print('-------')
print('键的判断')
#使用in 或者 not in 返回的是布尔值
sorces={'张三':50,'李四':60,'王五':70}
print('张三' in sorces)
print('张三' not in sorces)
print('-------')
print('字典元素的删除')
#del 字典名【键】
del sorces['张三']#删除指定的键值对
print(sorces)
#sorces.clear()#该操作为清空字典元素，会使这个字典编程空字典
print('--------')
print('字典元素的增加与修改')
#字典名【’添加的键‘】=值
sorces={'张三':50,'李四':60,'王五':70}
print('添加前',sorces)
sorces['陈六']=80
print('添加后',sorces)
sorces['陈六']=98
print('修改后',sorces)

