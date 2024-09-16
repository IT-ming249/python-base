#object类 这个类是所有类的祖宗
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'我的名字是{self.name},今年{self.age}岁了'
stu=Student('张三',20)
print(dir(stu))
#Object里面有一个__str__()方法，用于返回一个''对象的描述'',该方法可以被重写
print(stu)#这条代码会默认调用__str__()方法 