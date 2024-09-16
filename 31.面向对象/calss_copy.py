#类的赋值
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#变量的赋值：
cpu1=CPU()
cpu2=cpu1
print(cpu2)
print(cpu1)#这两个变量的地址是一样的，这说明只是形成了两个变量，实际上它俩指向同一个类对象
print('--------------------')


#浅拷贝:python的拷贝没有特殊说明的话，一般都是浅拷贝，这表示拷贝的时候，子对象的内容不拷贝，源对象和拷贝对象会引用同一个子对象
disk=Disk() #创建一个硬盘类对象
computer=Computer(cpu1,disk)#创建一个计算机类的对象
#开始浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)#可以看到源对象computer,computer2的地址不同，但它们的的子对象（cpu,disk）地址都是一样的
print('------------------------')


#深拷贝:使用copy模块中的deepcopy()函数，递归拷贝对象中包含的子对象，源对象与拷贝对象所有的子对象也不同
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)