#集合生成式
#语法结构：{i*i(表示元素集合的表达式) for i(自定义变量) in range（）（可迭代对象） }
#把{}换成[]就是列表生成式了
set={i*2 for i in range(1,10)}
print(set,type(set))