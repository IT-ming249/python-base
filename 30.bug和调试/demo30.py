#Bug常见类型：
#（1）粗心导致
#（2）思路不清晰 ：可以用print（）函数来观察中间输出值，或者注释掉部分代码再进行调试
#（3）异常处理机制，
'''try
可能出现异常的代码
except 异常类型
异常处理代码'''
try:
    a=int(input('请输入一个整数'))
    b=int(input('请再输入一个整数'))
    result=a/b
    print(result)
except ZeroDivisionError:#可以使用多个except来处理不同类型的异常，顺序为先子类后父类
    print('除数不能为0')
except ValueError:
    print('请确定输入的是整数')
except BaseException as e: #为了避免可能遗漏的异常类型最后可增加BaseException
    print(e)
else:#如果这串代码没有出现异常，就执行else
    print(result)
finally:
    print('无论程序是否异常都会执行这一条语句')