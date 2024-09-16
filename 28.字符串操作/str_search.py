print('字符串查询操作')
s='hello,hello'
#方法一：index()函数，寻找子字符串第一次出现的位置，找不到会报错
print(s.index('lo'))
#方法二：find()函数，寻找子字符串第一次出现的位置，找不到返回-1
print(s.find('lo'))
#方法三：rindex()函数，寻找子字符串最后一次出现的位置，找不到会报错
print(s.rindex('lo'))
#方法四：rfind()函数寻找子字符串第一次出现的位置，找不到返回-1
print(s.rfind('lo'))

