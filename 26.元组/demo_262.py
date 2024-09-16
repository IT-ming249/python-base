#元组元素的获取方式
t=('python','word',98)
#方法一：通过索引
print(t[0])
print(t[1])
print(t[2])
#print(t[3]) 由于索引越界，这样会报错
print('-------')
#元组的遍历
for i in t:
    print(i)