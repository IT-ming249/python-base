#特殊属性
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name ):
        self.name=name

#创建C类的对象
x=C('jack') #C类型的实例对象
print(x.__dict__) #实例对象的属性字典
print(C.__dict__) #类对象的属性字典
print('-----------------')
print(x.__class__) #输出了对象所属的类
print(C.__bases__) #输出父类类型，储存在一个元组里面
print(C.__base__)  #输出继承括号中的第一个父类
print(C.__mro__)   #输出类的存储结构  最左边的是孙子，最右边的是爷爷
print(A.__subclasses__())#输出A的子类
print('-------------------')


#特殊方法
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other): #想要实现两个对象的相加必须编写这个特殊方法
        return  self.name+other.name
    def __len__(self):#想要输出对象的长度，需要写__len__的特殊方法,这不是重写，没有父类
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2 #通过重写__add__方法实现了两个对象的加法运算（因为在类Student中编写__add__()特殊方法）
print(s)
c=stu1.__add__(stu2)
print(c)
print('----------------------')
lst=[1,2,3,4]
print(len(lst))#此处了呢()是内置函数，用于计算列表lst的长度
print(lst.__len__())
print(len(stu1))#想要输出对象的长度，需要写__len__的特殊方法
print('-----------------------')


class Person:
    def __new__(cls, *args, **kwargs):#new用于创建对象
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象id为：{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):#init用于初始化对象
        print('__init__方法被调用了，self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))
#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的地址为:{0}'.format(id(p1)))
#想知道这些地址的值为什么是这样，就使用debug调试来看底层执行原理