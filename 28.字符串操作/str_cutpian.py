#字符串切片操作
#字符串是不可变类型，没有增删改查操作，切片操作将产生新的对象
s='hello.Python'
s1=s[:5]#从索引0开始 完整写法s[start:stop:step] step的正负决定索引的检索方向
s2=s[6:]#从索引6到最后
s3='!'
new_str=s1+s3+s2
print(s1)
print(s2)
print(new_str)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(new_str))