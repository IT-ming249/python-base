#输出一个三行四列的矩阵
for i in range(3):
    for j in range(4):
        print('*',end='\t')#不换行
    print()#换行
print('---------')
#打印99乘法表

for a in range(1,10):
    b = 1
    while b<=a:
        print(a,'*',b,'=',a*b,end='\t')
        b=b+1
    print()
