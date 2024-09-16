#封装
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车人变形')

#类的外面可以直接使用类的属性和方法，这样就体现出了类的封装
car=Car('宝马X5')
print(car.brand)
print('-------------')


class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #年龄不希望被类的外部使用，所以加了__
    def show(self):
        print(self.name,self.__age)#年龄可以再类里面使用


stu=Student('张三',20)
stu.show()
print(stu.name)
#print(stu.__age) 这样是用不了的
print(dir(stu))#这里面有name,没有age ,但是age在_Student__age里边
print(stu._Student__age)#在类的外部可以通过_Student__age 对年龄进行访问 （Python的封装就是个君子协定而已，缺乏真正的封装性 ）