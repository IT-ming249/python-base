#递归函数：函数自己调用自己
#组成部分：函数的调用与递归的终止条件
def fun(num):
    if num==1:
        return 1
    else:
        return num*fun(num-1)
print(fun(6))
#例子：计算斐波那契数列
print('---------')
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else :
        return fib(n-1)+fib(n-2)
print(fib(5))
#使用循环的方法;
a=0
b=1
sum=0
for i in  range(1,6):
    if i ==1:
        sum=1
    else:
        sum=a+b
        a=b
        b=sum

print(sum)