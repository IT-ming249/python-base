#函数参数的定义
#函数定义默认参数
#函数定义时，可以给形参设置默认值，只有默认值不符的时候，才需要传递实参
def fun(a,b=10): #b称为默认值参数
    print(a,b)
fun(100) #只传一个参数，那么b就会采用默认参数
fun(10,20)# 20将默认值10替换
print('-------')
#个数可变的位置参数
#定义函数时，事先无法确定，传递的实参个数时，使用可变的位置参数，使用*定义
#结果为一个元组
def fun1(*arg): #个数可变的位置参数，只能定义一个
    print(arg)
fun1(10)
fun1(10,20)
fun1(10,20,30)
print('---------')
#个数可变的关键字形参
#定义函数时，无法事先确定传递的关键字形参的个数时，使用**定义个数可变的关键字形参
#结果为一个字典
def fun2(**kwargs): #个数可变的关键字形参也只能定义一个
    print(kwargs)

fun2(a=10)
fun2(a=20,b=30,c=50)

def fun3(*a,**b):
    pass
def fun4(a,b,*,c,d):#这表示*以后的参数只能采用关键字参数进行传输
    pass
'''def fun4(**c,*d)：
pass  这样就会报错
在函数定义的过程中，既有个数可变的位置参数,又有个数可变的关键字形参时，要求个数可变的位置参数放在前面

*args是个元组
**kwargs是个字典'''
