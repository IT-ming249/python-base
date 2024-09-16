#break语句:用于结束循环结构，配合if使用
#从键盘录入密码，有三次机会，密码正确就结束循环
password=0
for i in [1,2,3]:
    password=input('请输入密码')
    if password=='123':
        print('欢迎使用')
        break
    else:
        print('密码错误，请重新输入')
print('-------')


