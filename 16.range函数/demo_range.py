#内置函数range() 三种创建方式
#range()函数的返回值是一个迭代器对象，不管整数序列多长，内存仅仅存储start,stop,step，只有用到range对象时，才会计算序列中的相关元素
#range(stop):创建[0,stop)的整数序列，默认从0开始，步长为1
r=range(10)
print(r)
print(list(r))#list()列表函数用于查看range对象中的整数序列
print('------')
#range(start,stop):创建[start,stop)的整数序列,默认步长为1
w=range(1,10)
print(list(w))
print('------')
#range(start,stop,step)创建[start,stop)的整数序列,步长为step
q=range(1,10,2)
print(list(q))
#可以使用in 或 not in判断指定整数在序列中是否存在
print(10 in q)#返回布尔值
print(10 not in q)