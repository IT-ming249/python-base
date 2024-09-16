#集合间的数学操作
s1={10,20,30,40}
s2={20,30,40,50,60}
print('交集')
print(s1.intersection(s2))
print(s1 & s2)#Python中这个操作与上一行等价
print('-------')
print('并集')
print(s1.union(s2))
print('--------')
print('差集也就是补集')
print(s1.difference(s2))
print('---------')
print('对称差集(两个集合的并集去掉交集)')
print(s1.symmetric_difference(s2))
