#列表的排序方法
#方法一：使用sort函数，默认升序排序
lst=[6,5,4,3,2,1]
print('排序前',lst,id(lst))
lst.sort()#不指定关键字,默认reverse=False 升序排序
print('排序后',lst,id(lst))
#排序并不产生新的列表，是在原来的列表上面进行的
#通过指定关键字参数，可以将列表进行降序排序
lst.sort(reverse=True)
print(lst)
print('-------')
#方法二：使用sorted函数进行排序
new_lst=sorted(lst)
print(new_lst,id(new_lst))#sorted函数进行排序会产生新的列表
#实现降序排序
rnew_lst=sorted(lst,reverse=True)
print(rnew_lst)