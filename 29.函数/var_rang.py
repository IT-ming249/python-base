#变量的作用域
#局部变量：函数内定义并且使用的变量，只在函数的内部生效
#全局变量：函数体外定义的变量，可作用于函数外
def fun(a,b):
    c=a+b#c为局部变量，a,b为形参作用域也是函数内部为局部变量
    print(c)

name='菜鸡'# 函数的内部和外部都能使用，为全局变量

def fun1():
    print(name)

fun1()

def fun2():
    global age #局部变量用global声明，就变成了全局变量
    age=20
    print(age)
fun2()
print(age)