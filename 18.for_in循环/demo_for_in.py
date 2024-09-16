#for in循环
#in 从表达式中（序列，字符串等）中，依次取值，称为遍历
#for-in 遍历的对象必须是可迭代对象
#语法结构：
#for 自定义变量 in 可迭代对象:
#循环体

#case1
for item in 'Python':
    print(item)

print('---------')
#case2
for i in range(10):
    print(i)
print('---------')
#case3 若循环体中不需要自定义变量，可将自定义变量写成 _
for _ in range(10):
    print('i love study')
print('---------')
#case4 使用for循环计算1-100之间的偶数和
sum=0
for a in range(0,101,2):
    sum=sum+a
print(sum)

