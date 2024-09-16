#用于结束此次循环，进入下一次，与if搭配使用
#要求输出1-50之间5的倍数
for i in range(1,51):
    if i%5!=0:
        continue
    print(i)