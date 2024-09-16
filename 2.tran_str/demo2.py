##转义字符
#换行
print('hello\nword')
#沾满制表位
print('hello\tword')
#回车
print('hello\rword')#Word对hello进行了覆盖
#退一个格
print("hellow\bword")#w被退格删掉
#输出单引号
print('\'hellow word\'')
#原字符 不希望字符串中的转义字符起作用，就用原字符r或R 注意：使用时最后一个字符不能是反斜线
print(r'hellow\nword')