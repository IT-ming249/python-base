#函数传参内存分析
def fun(arg1,arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    arg1=100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)

n1=11#整数是不可变对象
n2=[10,20,30]#列表是可变对象
print('调用前',n1)
print('调用前',n2)
print('-------')
fun(n1,n2)#实参名称可以与形参不一样
print('调用后',n1)#如果是不可变对象，在函数体修改不会影响实参的值
print('调用后',n2)#如果是可变对象，在函数体内的修改会影响到实参的值