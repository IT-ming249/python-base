#while循环实例，同for
password=0
a=0;
while a<3:
    password = input('请输入密码')
    if password=='123':
        print("欢迎使用")
        break
    else:
        print('密码错误，请重新输入')
    a=a+1