#while循环
'''while 条件表达式
        循环体'
       ---------
4步循环法：
1.初始化变量
2.条件判断
3.循环体
4.改变变量'''
a=1
sum=0
while a<10:#(条件表达式为真的时候执行循环体)
    a=a+1
    print(a)

print('----------')
a=0
#练习题：求1:100之间偶数的和
while a<=100:
    #方法1
   # sum=sum+a
    #a=a+2
#方法2
 if a%2==0:
     sum=sum+a

 a=a+1
print(sum)