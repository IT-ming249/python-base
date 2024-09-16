#条件表达式 是if...else..的简写
#从键盘录入整数，比较两个整数的大小
num_a=int(input('请输入一个数'))
num_b=int(input('输入另外一个数'))
'''if num_a>num_b:
    print(num_a,'更大')
else:
    print(num_b,'更大')'''
#条件表达式语法结构 x if 判断条件 else y (判断条件为真返回x,不为真返回y)
#接下来简写上面的if else
print("a更大") if num_a>num_b else print('b更大')