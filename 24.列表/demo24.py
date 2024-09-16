#列表相当于其它语言的数组
#先看看列表属性
lst=['hello','word',98,'hello']
print(id(lst))
print(type(lst))
print((lst))
print('列表存储的是列表中对象的引用')
print('列表对象的创建')
#方式一：使用【】
lst1=['hello','word',98]
#方式2：使用内置函数list
lst2=list(['hello','word',98])
print('-------')
print('列表的特点')
print('1.列表元素按顺序有序排序')
print('2.索引映射唯一一个数据')
print('3.列表可以存储重复数据')
print('4.任意数据类型可以混存')
print('5.根据需要动态分配内存回收（就是不用担心存多少个元素存不下）')
print(('--------'))
print('获取指定元素的索引')
print(lst.index('hello'))#如果列表中有相同的元素，只返回列表相同元素的第一个元素的索引
#也可以从指定范围查找
print(lst.index('hello',1,4))
print('---------')
print('获取列表中的单个元素')
print(lst[0],lst[-4])#有N个元素的话，正向索引为0到N-1，逆向索引为-N到-1
#print(lst[10])#索引不在上述的指定范围内则报错
print('---------')
print('获取列表中的多个元素-切片')
#语法结构：列表名[start:stop:step]--切片范围：[start,stop)左闭右开，步长不写的话默认为1
table=[1,2,3,4,5,6,7,8,9,10]
print(table[0:6:2])#切片切出来的是新的列表，id跟原列表不同了
print(table[:6:2])#start采用默认为0
print(table[0::1])#stop采用默认为最后一个元素的索引
print('当step为负数的时候')
print(table)
print(table[::-1])#步长采用负数时，切片的第一个元素默认为最后一个元素，切片的最后一个元素默认为切片的第一个元素
print(table[9:5:-1])
print('--------')
print('判断列表元素是否存在')#元素in（not in）列表名
lst3=[10,20,'python','hello']
print(10 in lst3)
print(10 not in lst3)
print(100 in lst3)
print(100 not in lst3)
print('----------')
print("列表元素的遍历")#for 迭代变量 in 列表名：
for i in lst3:
    print(i)
print('---------')
print('列表元素的添加操作')
#方法一：列表名。append（元素）向列表末尾添加一个元素，添加前后列表对象ID是相同的，没有创建新的列表对象
lst4=[10,20,30]
print('添加前',lst4)
lst4.append(100)
print('添加后',lst4)
print('-------')
#方法二：列表名.extend（）：在列表的末尾至少添加一个元素
lst5=['hello','word']
#lst5.append(lst4) #将列表lst4作为元素添加到列表末尾,添加的也可以是一个列表
lst5.extend(lst4)#向列表的末尾一次性添加多个元素
#lst5.extend('a','b')
print(lst5)
print('---------')
#方法三：列表名.insert（索引位置，元素）：在列表的任意位置插入元素
lst5.insert(0,77)
print(lst5)
print('---------')
#方法四：切片：在任意位置添加至少一个元素
lst6=[True,False,'hello']
lst5[1:]=lst6#表示吧lst5索引位置为1到最后的元素替换为lst6
print(lst5)
print('---------')
print('列表的删除操作')
#方法一：列表名.remove(元素)在列表中删除一个元素
lst7=[10,20,30,20,40,50]
lst7.remove(20)#如果有重复元素则只移除第一个
print(lst7)
print('----------')
#方法二：列表名.pop():删除指定索引位置上的元素
print('删除前：',lst7)
lst7.pop(1)
print('删除后：',lst7)
lst7.pop()#不指定索引则删除最后一个元素
print('不指定索引删除后',lst7)
print('--------')
#方法三：切片,一次至少删除一个元素，
lst8=[1,2,3,4,5,6]
print('原列表',lst8)
#不产生新列表对象的操作方法
lst8[0:2]=[]
print(lst8)
print('--------')
#clear()清空列表
#del()删除列表
lst8.clear()
print(lst8)
del lst8 #直接把列表对象删除了
#print(lst8)
print('-----')
print('列表元素的修改')
lst9=[1,2,3,4,5,6]
#方法一：一次修改一个值,利用索引
lst9[2]=20
print(lst9)
print('------')
#方法二：利用切片
lst00=[200,300,400]
lst9[1:3]=lst00
print(lst9)


