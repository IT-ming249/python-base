s='hello python'
#字符串的替换
#repalce():第1个参数指定被替换的子串，第2个参数指定替换子串的字符串，第3个参数指定最大替换次数（可选）,替换之后返回字符串
print(s.replace('python','c++'))
print('---------')
#字符串合并
#join()：将列表或元组中的字符串合并成一个字符串
#连接列表
lst=['hello','python','java']
#lst=['hello','python','java',98]#用这个join会报错
print('/'.join(lst))
print(''.join(lst))
#连接元组
print('*'.join('python'))
