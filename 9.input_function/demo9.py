##输入函数inpu()
score=input('想要多少分')#跟c的scanf差不多，''里为提示语，返回类型为str
print(score,type(score))
#高级应用
a=input('输入一个数')
b=input('再舒服一个数')
print(a+b)#这样只起到连接作用
print(int(a)+int(b))#通过类型转换这样才能相加