#python一切皆对象 所有的对象都有布尔值
#获取对象布尔值用内置函数bool()
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(''))
print(bool(""))#空字符串
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合
#除了以上对象的布尔值为False，其它对象的布尔值均为true
#用处举例
age=int(input('请输入年龄'))
if age:#Python中对象可以直接放在条件表达式中去做判断
    print(age)
else:#age=0的时候会走这条分支
    print('年龄是',age)
