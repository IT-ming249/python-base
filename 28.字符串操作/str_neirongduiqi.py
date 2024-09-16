#字符串对齐操作
s='hello,python'
#center()：居中对齐,第一个参数指定宽度，第二个参数指定填充符（可选）默认空格
print(s.center(20,'*'))
print(s.center(20))
#ljust()：左对齐,第一个参数指定宽度，第二个参数指定填充符（可选）默认空格
print(s.ljust(20,'*'))
print(s.ljust(20))
#rjust():右对齐,第一个参数指定宽度，第二个参数指定填充符（可选）默认空格
print(s.rjust(20,'*'))
print(s.rjust(20))
#zfill():右对齐，会使用0进行填充
print(s.zfill(20))
print('-8090'.zfill(10))



