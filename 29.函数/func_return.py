#函数的返回值
#(1)如果函数没有返回值return 可以省略
#(2)函数返回值如果是一个，直接返回原值(是列表就返回列表，是整数就返回整数)
#(3)函数返回值如果是多个，返回结果为元组
#函数定义时是否设置返回值，视情况而定

def fun(num):
    odd=[]
    even=[]
    for i in num:
       if i%2==0:
        even.append(i)
       else:
        odd.append(i)
    return odd,even

rel=fun([1,2,3,4,5,6])
print(rel)

