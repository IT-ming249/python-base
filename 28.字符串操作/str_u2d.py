#字符串大小写转换
s='hello,python'
#upper():字符串中的所有字母转成大写
a=s.upper()
print(a,id(a))#转成大写以后会产生新的字符串对象
print(s,id(s))
print('---------')
#lower()：字符串中所有字母转小写
b=s.lower()
print(b,id(b))#转成小写以后会产生新的字符串对象
print(s,id(s))
print(s==b)
print(s is b)
print('---------')
#swapcase():原来小写的变成大写，原来大写的变成小写
s2='hello,Python'
c=s2.swapcase()
print(c,id(c))
print(s2,id(s2))
print('------------')
#title():每个英文单词的首字母转大写，每个单词的剩余字符转小写
d=s2.title()
print(d)



