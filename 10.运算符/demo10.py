##算术运算符
print('算术运算符')
print(1+1)#加法
print(1-1)#减法
print(2*6)#乘法
print(11/2)#除法
print(11//2)#整除
print(11%2)#取模 得到余数
print(2**3)#幂次运算 2的三次方
#算术运算符需要注意的东西
print(9//-4)#整除一正一负，是向下取整数的
print(-9//4)
print(9%-4) #公式 余数=被除数-除数*商
print(-9%4)
print("------下面是赋值运算符")
##赋值运算符 运算顺序从右到左
i=3+4
print(i)
#链式赋值 只有一个整数对象，即三个都是同一地址（id）
a=b=c=20
print(a,id(a),b,id(b),c,id(c))
#支持参数赋值，这相当于d=d+20 有+= -= *= /= //=
d=20
d+=20
print(d)
#支持解包赋值 等号左右两边变量数要相同
q,w,e=10,20,30
print(q,w,e)
#例子，交换两个变量，不用创建临时变量
print('交换前',q,w)
q,w=w,q
print('交换后',q,w)
print("------下面是比较运算符")##比较运算符返回布尔类型
a,b=10,20
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a==b)#分清楚赋值 = 和比较==（这个比较的是指） is比较的是标识符是否相等 is not比较的是标识符是否不相等
print(a is b)
print(a!=b)
print("------下面是布尔运算符")
a,b=1,2
print(a==1 and b==2)#T and T ->True
print(a==1 and b<2)#T and F ->F
print(a!=1 and b==2)#F and T->F
print('and运算符两个都为真才为真')
print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b!=2)
print('or运算符有一个为真就为真')
f1=True
f2=False
print(not(f1),not(f2))
print('not运算符对布尔操作数取反')
s='hello word'
print('h'in s)
print('h'not in s)
print('in not in 的功能看上面两行代码')
print('-------下面是位运算符')#数据转成2进制位进行运算
#按位与&
print(4&8)
#按位或|
print(4|8)
#左移运算符<<
print(4<<1)#向左移动一位，高位溢出舍弃，低位补0
#右移运算符>>
print(4>>1)#向右移动一位，低位溢出舍弃，高位补0
print('-------运算符的优先级')
print('从高到低：（）->算术->位->比较->布尔->赋值')

