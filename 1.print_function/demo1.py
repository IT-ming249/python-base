#输出数字
print(520)
#输出字符串
print('hellow word')
#输出含有运算符号的表达式，会计算
print(5*2)
print(4+2)
#将数据输出到文件中 注意点：1.所指定的盘存在 2.使用file=fp(文件指针变量)
fp=open('E:/py/py_study/test_python/1.print_function/text.txt','a+')#这个命令是将数据输出到text文件中，a+表示如果没有就创建,有就在后面追加内容
print('hehe',file=fp)
fp.close()
#不进行换行输出
print('hello',"Python")