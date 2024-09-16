#函数
'''函数的创建：
def 函数名(输入参数)
return xxx'''
def add(a,b): #a,b是形式参数，形参的位置在函数定义处
    c=a+b
    return c
#调用及其传参方式
result=add(1,2) #1和2是实际参数值，位置在函数的调用处 这里是位置传参
resul1=add(b=1,a=2)#这种是关键字实参，会根据等号左侧的关键字进行传参
print(result)
print(resul1)